
import json
import tempfile
import time
import tracemalloc
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def consolidar_resultados(resultados):
    if resultados is None:
        raise ValueError("Os resultados não foram informados.")

    if isinstance(resultados, pd.DataFrame):
        if resultados.empty:
            raise ValueError("A tabela de resultados está vazia.")
        tabela = resultados.copy()
    else:
        if len(resultados) == 0:
            raise ValueError("A lista de resultados está vazia.")
        tabela = pd.DataFrame(resultados)

    colunas_obrigatorias = {
        "modelo",
        "experimento",
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc",
        "tempo_treinamento_s",
        "tempo_predicao_s",
    }

    colunas_ausentes = colunas_obrigatorias - set(tabela.columns)

    if colunas_ausentes:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {sorted(colunas_ausentes)}"
        )

    tabela = tabela.drop(
        columns=["pipeline"],
        errors="ignore",
    )

    return tabela.sort_values(
        by="f1",
        ascending=False,
    ).reset_index(drop=True)



def comparar_modelos(resultados, metrica="f1"):

    metricas_validas = {
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc",
    }

    if metrica not in metricas_validas:
        raise ValueError(
            f"Métrica inválida: {metrica}. "
            f"Escolha entre {sorted(metricas_validas)}."
        )

    tabela = consolidar_resultados(resultados)

    return tabela.sort_values(
        by=metrica,
        ascending=False,
    ).reset_index(drop=True)


def resumir_melhores_modelos(resultados, metrica="f1"):

    tabela = comparar_modelos(resultados, metrica=metrica)

    return (
        tabela.drop_duplicates(subset="modelo", keep="first")
        .reset_index(drop=True)
    )


def avaliar_classificacao(y_real, y_predito, probabilidades=None):

    y_real = np.asarray(y_real)
    y_predito = np.asarray(y_predito)

    if len(y_real) == 0:
        raise ValueError("Os valores reais não podem estar vazios.")

    if len(y_real) != len(y_predito):
        raise ValueError(
            "Os valores reais e previstos devem ter o mesmo tamanho."
        )

    if not np.isin(y_real, [0, 1]).all():
        raise ValueError("O alvo real deve conter apenas as classes 0 e 1.")

    if not np.isin(y_predito, [0, 1]).all():
        raise ValueError(
            "As previsões devem conter apenas as classes 0 e 1."
        )

    matriz = confusion_matrix(
        y_real,
        y_predito,
        labels=[0, 1],
    )

    tn, fp, fn, tp = matriz.ravel()

    metricas = {
        "accuracy": accuracy_score(y_real, y_predito),
        "precision": precision_score(
            y_real, y_predito, zero_division=0
        ),
        "recall": recall_score(
            y_real, y_predito, zero_division=0
        ),
        "f1": f1_score(
            y_real, y_predito, zero_division=0
        ),
        "verdadeiros_negativos": int(tn),
        "falsos_positivos": int(fp),
        "falsos_negativos": int(fn),
        "verdadeiros_positivos": int(tp),
    }

    if probabilidades is not None:
        probabilidades = np.asarray(probabilidades)

        if len(probabilidades) != len(y_real):
            raise ValueError(
                "As probabilidades devem ter o mesmo tamanho do alvo."
            )

        if not np.isfinite(probabilidades).all():
            raise ValueError("As probabilidades contêm valores inválidos.")

        if len(np.unique(y_real)) == 2:
            metricas["roc_auc"] = roc_auc_score(
                y_real,
                probabilidades,
            )
        else:
            metricas["roc_auc"] = float("nan")

    return metricas, matriz


def gerar_matrizes_confusao(resultados, X_val, y_val):

    matrizes = {}

    for resultado in resultados:
        pipeline = resultado.get("pipeline")

        if pipeline is None:
            continue

        previsoes = pipeline.predict(X_val)

        matriz = confusion_matrix(
            y_val,
            previsoes,
            labels=[0, 1],
        )

        chave = (
            f"{resultado['modelo']}"
            f"_experimento_{resultado['experimento']}"
        )

        matrizes[chave] = pd.DataFrame(
            matriz,
            index=["Real_0", "Real_1"],
            columns=["Previsto_0", "Previsto_1"],
        )

    if not matrizes:
        raise ValueError(
            "Nenhum pipeline foi encontrado nos resultados."
        )

    return matrizes


def plotar_matriz_confusao(
    matriz,
    titulo="Matriz de confusão",
    salvar_em=None,
):

    import matplotlib.pyplot as plt
    from sklearn.metrics import ConfusionMatrixDisplay

    valores = (
        matriz.to_numpy()
        if isinstance(matriz, pd.DataFrame)
        else np.asarray(matriz)
    )

    if valores.shape != (2, 2):
        raise ValueError("A matriz deve ter dimensão 2x2.")

    fig, ax = plt.subplots(figsize=(6, 5))

    exibicao = ConfusionMatrixDisplay(
        confusion_matrix=valores,
        display_labels=["Sem atraso", "Com atraso"],
    )

    exibicao.plot(
        ax=ax,
        values_format="d",
        colorbar=False,
    )

    ax.set_title(titulo)
    fig.tight_layout()

    if salvar_em is not None:
        caminho = Path(salvar_em)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(caminho, dpi=150, bbox_inches="tight")

    return fig, ax


def avaliar_limiares(
    pipeline,
    X_val,
    y_val,
    limiares=(0.10, 0.20, 0.30, 0.40, 0.45, 0.50, 0.55, 0.60),
):

    if len(X_val) == 0 or len(y_val) == 0:
        raise ValueError("A validação não pode estar vazia.")

    if len(X_val) != len(y_val):
        raise ValueError(
            "X_val e y_val devem possuir o mesmo número de registros."
        )

    limiares = list(limiares)

    if not limiares:
        raise ValueError("Informe pelo menos um limiar.")

    if any(not 0 <= limiar <= 1 for limiar in limiares):
        raise ValueError("Todos os limiares devem estar entre 0 e 1.")

    if len(np.unique(y_val)) != 2:
        raise ValueError(
            "A validação precisa conter as duas classes do alvo."
        )

    probabilidades = pipeline.predict_proba(X_val)[:, 1]
    resultados_limiares = []

    for limiar in limiares:
        previsoes = (probabilidades >= limiar).astype(int)

        metricas, _ = avaliar_classificacao(
            y_val,
            previsoes,
            probabilidades=probabilidades,
        )

        quantidade_alertas = int(previsoes.sum())

        resultados_limiares.append(
            {
                "limiar": float(limiar),
                **metricas,
                "quantidade_alertas": quantidade_alertas,
                "percentual_alertas": (
                    quantidade_alertas / len(previsoes) * 100
                ),
            }
        )

    return pd.DataFrame(resultados_limiares).sort_values(
        by="limiar"
    ).reset_index(drop=True)


def analisar_custos_erros(
    y_real,
    y_predito,
    custo_falso_positivo=None,
    custo_falso_negativo=None,
):
    

    metricas, _ = avaliar_classificacao(y_real, y_predito)

    resultado = {
        "falsos_positivos": metricas["falsos_positivos"],
        "falsos_negativos": metricas["falsos_negativos"],
    }

    custos_informados = (
        custo_falso_positivo is not None,
        custo_falso_negativo is not None,
    )

    if any(custos_informados) and not all(custos_informados):
        raise ValueError(
            "Informe os custos dos dois tipos de erro ou nenhum deles."
        )

    if all(custos_informados):
        if custo_falso_positivo < 0 or custo_falso_negativo < 0:
            raise ValueError("Os custos não podem ser negativos.")

        resultado["custo_falso_positivo_total"] = (
            resultado["falsos_positivos"] * custo_falso_positivo
        )

        resultado["custo_falso_negativo_total"] = (
            resultado["falsos_negativos"] * custo_falso_negativo
        )

        resultado["custo_total_estimado"] = (
            resultado["custo_falso_positivo_total"]
            + resultado["custo_falso_negativo_total"]
        )

    return resultado


def comparar_tempos(resultados, quantidade_pedidos):

    if quantidade_pedidos <= 0:
        raise ValueError("A quantidade de pedidos deve ser positiva.")

    tabela = consolidar_resultados(resultados)

    tabela["quantidade_pedidos_avaliados"] = quantidade_pedidos

    tabela["latencia_por_pedido_ms"] = (
        tabela["tempo_predicao_s"] / quantidade_pedidos
    ) * 1000

    tabela["pedidos_por_segundo_aprox"] = (
        quantidade_pedidos / tabela["tempo_predicao_s"].replace(0, np.nan)
    )

    return tabela[
        [
            "modelo",
            "experimento",
            "tempo_treinamento_s",
            "tempo_predicao_s",
            "quantidade_pedidos_avaliados",
            "latencia_por_pedido_ms",
            "pedidos_por_segundo_aprox",
        ]
    ]


def medir_latencia_pipeline(pipeline, X, repeticoes=5):
   
    if len(X) == 0:
        raise ValueError("O conjunto de entrada está vazio.")

    if repeticoes < 1:
        raise ValueError("repeticoes deve ser pelo menos 1.")


    pipeline.predict(X.iloc[:1])

    tempos = []

    for _ in range(repeticoes):
        inicio = time.perf_counter()
        pipeline.predict(X)
        tempos.append(time.perf_counter() - inicio)

    tempo_medio = float(np.mean(tempos))

    return {
        "quantidade_pedidos": len(X),
        "repeticoes": repeticoes,
        "tempo_medio_lote_s": tempo_medio,
        "latencia_media_por_pedido_ms": (
            tempo_medio / len(X) * 1000
        ),
        "tempo_minimo_lote_s": float(np.min(tempos)),
        "tempo_maximo_lote_s": float(np.max(tempos)),
    }


def medir_tamanho_modelo(pipeline):

    with tempfile.TemporaryDirectory() as diretorio:
        caminho = Path(diretorio) / "pipeline.joblib"
        joblib.dump(pipeline, caminho)
        tamanho_bytes = caminho.stat().st_size

    return {
        "tamanho_modelo_bytes": tamanho_bytes,
        "tamanho_modelo_mb": tamanho_bytes / (1024 ** 2),
    }


def medir_memoria_pico(funcao, *args, **kwargs):

    if tracemalloc.is_tracing():
        raise RuntimeError(
            "Já existe uma medição tracemalloc em andamento."
        )

    tracemalloc.start()

    try:
        resultado = funcao(*args, **kwargs)
        _, pico_bytes = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()

    return {
        "resultado": resultado,
        "pico_memoria_rastreada_bytes": pico_bytes,
        "pico_memoria_rastreada_mb": pico_bytes / (1024 ** 2),
    }


def selecionar_modelo_candidato(
    resultados,
    metrica="f1",
    recall_minimo=None,
):

    metricas_validas = {
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc",
    }

    if metrica not in metricas_validas:
        raise ValueError(
            f"Métrica inválida: {metrica}. "
            f"Escolha entre {sorted(metricas_validas)}."
        )

    if recall_minimo is not None and not 0 <= recall_minimo <= 1:
        raise ValueError("recall_minimo deve estar entre 0 e 1.")

    candidatos = [
        resultado
        for resultado in resultados
        if resultado.get("pipeline") is not None
        and pd.notna(resultado.get(metrica))
    ]

    if recall_minimo is not None:
        candidatos = [
            resultado
            for resultado in candidatos
            if resultado.get("recall", 0) >= recall_minimo
        ]

    if not candidatos:
        raise ValueError(
            "Nenhum candidato atende aos critérios informados."
        )

    melhor = max(
        candidatos,
        key=lambda resultado: resultado[metrica],
    )

    return melhor.copy()



def salvar_tabela(tabela, caminho, index=False):


    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)

    tabela.to_csv(
        caminho,
        index=index,
        encoding="utf-8",
    )

    return caminho


def _converter_json(valor):

    if isinstance(valor, dict):
        return {
            str(chave): _converter_json(item)
            for chave, item in valor.items()
        }

    if isinstance(valor, (list, tuple)):
        return [_converter_json(item) for item in valor]

    if isinstance(valor, (np.integer,)):
        return int(valor)

    if isinstance(valor, (np.floating,)):
        return float(valor) if np.isfinite(valor) else None

    if isinstance(valor, np.ndarray):
        return valor.tolist()

    if isinstance(valor, Path):
        return str(valor)

    if pd.isna(valor) if not isinstance(valor, (dict, list, tuple, np.ndarray)) else False:
        return None

    return valor


def salvar_relatorio_json(relatorio, caminho):

    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)

    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(
            _converter_json(relatorio),
            arquivo,
            ensure_ascii=False,
            indent=4,
            allow_nan=False,
        )

    return caminho


def salvar_resultados_avaliacao(
    resultados,
    diretorio="reports/metrics",
    quantidade_pedidos=None,
):

    diretorio = Path(diretorio)
    diretorio.mkdir(parents=True, exist_ok=True)

    tabela = consolidar_resultados(resultados)

    salvar_tabela(
        tabela,
        diretorio / "comparacao_experimentos.csv",
    )

    melhores = resumir_melhores_modelos(resultados)

    salvar_tabela(
        melhores,
        diretorio / "melhores_modelos.csv",
    )

    arquivos = {
        "comparacao": str(diretorio / "comparacao_experimentos.csv"),
        "melhores_modelos": str(diretorio / "melhores_modelos.csv"),
    }

    if quantidade_pedidos is not None:
        tempos = comparar_tempos(resultados, quantidade_pedidos)

        salvar_tabela(
            tempos,
            diretorio / "desempenho_computacional.csv",
        )

        arquivos["desempenho_computacional"] = str(
            diretorio / "desempenho_computacional.csv"
        )

    return arquivos
