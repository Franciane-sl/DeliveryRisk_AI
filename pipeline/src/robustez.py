
import joblib
import numpy as np
import pandas as pd

from pathlib import Path

from pipeline.src.avaliacao import avaliar_classificacao

def validar_dados_avaliacao(
    X_train,
    y_train,
    X_val,
    y_val,
    X_test,
    y_test,
):
    conjuntos = {
        "treino": (X_train, y_train),
        "validação": (X_val, y_val),
        "teste": (X_test, y_test),
    }

    colunas_referencia = list(X_train.columns)

    for nome, (X, y) in conjuntos.items():

        if X.empty or y.empty:
            raise ValueError(
                f"O conjunto de {nome} não pode estar vazio."
            )

        if len(X) != len(y):
            raise ValueError(
                f"X e y do conjunto de {nome} possuem "
                "quantidades diferentes de registros."
            )

        if not X.index.equals(y.index):
            raise ValueError(
                f"Os índices de X e y do conjunto de {nome} "
                "não estão alinhados."
            )

        if not y.isin([0, 1]).all():
            raise ValueError(
                f"O alvo do conjunto de {nome} "
                "deve conter apenas as classes 0 e 1."
            )

        if list(X.columns) != colunas_referencia:
            raise ValueError(
                f"O conjunto de {nome} possui colunas "
                "diferentes das utilizadas no treino."
            )

    return {
        "status": "validado",
        "quantidade_features": len(colunas_referencia),
        "quantidade_treino": len(X_train),
        "quantidade_validacao": len(X_val),
        "quantidade_teste": len(X_test),
    }


def comparar_generalizacao(metricas_validacao, metricas_teste):

    metricas_comparaveis = [
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc",
    ]

    resultados = []

    for metrica in metricas_comparaveis:

        if metrica not in metricas_validacao:
            continue

        if metrica not in metricas_teste:
            continue

        valor_validacao = metricas_validacao[metrica]
        valor_teste = metricas_teste[metrica]

        diferenca = valor_teste - valor_validacao

        resultados.append({
            "metrica": metrica,
            "validacao": valor_validacao,
            "teste": valor_teste,
            "diferenca_absoluta": diferenca,
            "diferenca_percentual": (
                (diferenca / valor_validacao) * 100
                if valor_validacao != 0
                else None
            ),
        })

    if not resultados:
        raise ValueError(
            "Não existem métricas comuns para comparação."
        )

    return pd.DataFrame(resultados)


def analisar_distribuicao_erros(y_real, y_predito):

    metricas, matriz = avaliar_classificacao(
        y_real=y_real,
        y_predito=y_predito,
    )

    tn, fp, fn, tp = matriz.ravel()

    total = len(y_real)

    return {
        "total_registros": total,
        "acertos": int(tn + tp),
        "erros": int(fp + fn),
        "verdadeiros_negativos": int(tn),
        "falsos_positivos": int(fp),
        "falsos_negativos": int(fn),
        "verdadeiros_positivos": int(tp),
        "percentual_acertos": (tn + tp) / total * 100,
        "percentual_erros": (fp + fn) / total * 100,
        "percentual_falsos_positivos": fp / total * 100,
        "percentual_falsos_negativos": fn / total * 100,
    }


def avaliar_robustez_temporal(
    pipeline,
    X_test,
    y_test,
    datas,
    quantidade_periodos=3,
    limiar=0.50,
):
    if len(X_test) == 0:
        raise ValueError("O conjunto de teste está vazio.")

    if len(X_test) != len(y_test) or len(X_test) != len(datas):
        raise ValueError(
            "X_test, y_test e datas devem possuir o mesmo tamanho."
        )

    if quantidade_periodos < 2:
        raise ValueError(
            "Informe pelo menos dois períodos temporais."
        )

    if not 0 <= limiar <= 1:
        raise ValueError("O limiar deve estar entre 0 e 1.")

    datas = pd.to_datetime(datas, errors="coerce")

    if datas.isna().any():
        raise ValueError(
            "Existem datas ausentes ou inválidas."
        )

    if not y_test.isin([0, 1]).all():
        raise ValueError(
            "O alvo deve conter apenas as classes 0 e 1."
        )

    probabilidades = pipeline.predict_proba(X_test)[:, 1]

    dados = pd.DataFrame({
        "data": datas.to_numpy(),
        "alvo": np.asarray(y_test),
        "indice": np.arange(len(X_test)),
        "probabilidade": probabilidades,
    })

    dados = dados.sort_values("data").reset_index(drop=True)

    dados["periodo"] = pd.qcut(
        dados["data"].rank(method="first"),
        q=quantidade_periodos,
        labels=False,
    )

    dados["previsao"] = (
        dados["probabilidade"] >= limiar
    ).astype(int)

    resultados = []

    for periodo, grupo in dados.groupby("periodo", sort=True):

        y_real_periodo = grupo["alvo"].to_numpy()
        y_predito_periodo = grupo["previsao"].to_numpy()
        probabilidades_periodo = grupo["probabilidade"].to_numpy()

        metricas, _ = avaliar_classificacao(
            y_real=y_real_periodo,
            y_predito=y_predito_periodo,
            probabilidades=probabilidades_periodo,
        )

        resultados.append({
            "periodo": int(periodo) + 1,
            "data_inicio": grupo["data"].min(),
            "data_fim": grupo["data"].max(),
            "quantidade_pedidos": len(grupo),
            "taxa_atraso_real": float(
                np.mean(y_real_periodo) * 100
            ),
            **metricas,
        })

    return pd.DataFrame(resultados)

def serializar_pipeline(pipeline, caminho):

    if pipeline is None:
        raise ValueError("O pipeline não foi informado.")

    if not hasattr(pipeline, "predict"):
        raise TypeError(
            "O objeto informado não possui método predict."
        )

    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(pipeline, caminho)

    return {
        "caminho": str(caminho),
        "tamanho_bytes": caminho.stat().st_size,
        "tamanho_mb": caminho.stat().st_size / (1024 ** 2),
    }


def carregar_pipeline(caminho):

    caminho = Path(caminho)

    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo do pipeline não encontrado: {caminho}"
        )

    return joblib.load(caminho)
