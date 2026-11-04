
from pathlib import Path
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Diretório para salvar os gráficos da análise exploratória.

PASTA_IMAGENS = (
    Path(__file__).resolve().parents[2]
    / "images"
    / "eda"
)


# Funções para a análise exploratória.

def resumir_datasets(datasets):

    resumo = []

    for nome, df in datasets.items():
        resumo.append({
            "dataset": nome,
            "linhas": df.shape[0],
            "colunas": df.shape[1],
            "valores_ausentes": int(df.isnull().sum().sum()),
            "registros_duplicados": int(df.duplicated().sum())
        })

    resultado = pd.DataFrame(resumo)

    return resultado


def inspecionar_dados(df, nome="dataset"):

    print("\n" + "=" * 25 + f" Inspeção: {nome} " + "=" * 25)

    print("\nDimensões do dataset:")
    print(f"Linhas: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")

    print("\nColunas:")
    print(list(df.columns))

    print("\nTipos de dados:")
    print(df.dtypes)

    print("\nInformações gerais:")
    df.info()

    print("\nEstatísticas descritivas:")
    print(df.describe(include="all").T)

    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())

    print("\nQuantidade de registros duplicados:")
    print(df.duplicated().sum())

    print("\n" + "=" * 25 + " Fim da inspeção " + "=" * 25)


def analisar_valores_ausentes(df, nome="dataset"):
    ausentes = df.isnull().sum()

    resumo = pd.DataFrame({
        "quantidade_ausentes": ausentes,
        "percentual_ausentes": (ausentes / len(df)) * 100
    })

    resumo = resumo.sort_values(
        by="quantidade_ausentes",
        ascending=False
    )

    return resumo


def analisar_ausencias_por_categoria(
    df,
    colunas,
    categoria,
):
 
    resultados = {}

    for coluna in colunas:
        grupo = df.groupby(categoria, dropna=False)

        quantidade_ausentes = grupo[coluna].apply(
            lambda serie: serie.isna().sum()
        )

        total_registros = grupo.size()

        resultado = pd.DataFrame({
            "quantidade_ausentes": quantidade_ausentes,
            "total_registros": total_registros,
        })

        resultado["percentual_ausentes"] = (
            resultado["quantidade_ausentes"]
            / resultado["total_registros"]
            * 100
        )

        resultados[coluna] = resultado.sort_values(
            by="quantidade_ausentes",
            ascending=False,
        )

    return resultados


def inspecionar_ausencias_por_status(
    df,
    status,
    colunas,
    coluna_status="order_status",
    colunas_adicionais=None,
):
   
    mascara_status = df[coluna_status].eq(status)
    mascara_ausencias = df[colunas].isna().any(axis=1)

    colunas_adicionais = colunas_adicionais or []

    colunas_resultado = list(dict.fromkeys(
        [coluna_status, *colunas_adicionais, *colunas]
    ))

    return df.loc[
        mascara_status & mascara_ausencias,
        colunas_resultado,
    ]


def inspecionar_registros_com_ausencias(
    df,
    colunas,
    coluna_id,
):

    mascara = df[colunas].isna().any(axis=1)

    return df.loc[
        mascara,
        [coluna_id, *colunas],
    ]

def analisar_duplicatas(df, nome="dataset"):

    quantidade = int(df.duplicated().sum())

    percentual = (
        quantidade / len(df) * 100
        if len(df) > 0
        else 0
    )

    print(f"\nAnálise de duplicatas: {nome}")
    print(f"Registros duplicados: {quantidade}")
    print(f"Percentual de duplicatas: {percentual:.2f}%")

    return quantidade


def analisar_chaves(df, nome, coluna):
   
    if coluna not in df.columns:
        raise ValueError(
            f"A coluna '{coluna}' não existe no dataset '{nome}'."
        )

    ausentes = int(df[coluna].isnull().sum())
    duplicados = int(df[coluna].duplicated().sum())
    valores_unicos = int(df[coluna].nunique())

    print(f"\nAnálise da coluna identificadora: {nome}.{coluna}")
    print(f"Valores ausentes: {ausentes}")
    print(f"Valores duplicados: {duplicados}")
    print(f"Valores únicos: {valores_unicos}")

    return {
        "dataset": nome,
        "coluna": coluna,
        "valores_ausentes": ausentes,
        "valores_duplicados": duplicados,
        "valores_unicos": valores_unicos
    }


def grafico_valores_ausentes(datasets):

    dados = []

    for nome, df in datasets.items():
        percentuais = df.isnull().mean() * 100

        for coluna, percentual in percentuais.items():
            if percentual > 0:
                dados.append({
                    "coluna": f"{nome}.{coluna}",
                    "percentual_ausentes": percentual
                })

    fig, ax = plt.subplots(figsize=(12, 7))

    if not dados:
        ax.text(
            0.5,
            0.5,
            "Nenhum valor ausente identificado",
            ha="center",
            va="center"
        )
        ax.set_axis_off()

    else:
        resultado = pd.DataFrame(dados).sort_values(
            "percentual_ausentes",
            ascending=True
        )

        ax.barh(
            resultado["coluna"],
            resultado["percentual_ausentes"]
        )

        ax.set_title("Percentual de Valores Ausentes por Coluna")
        ax.set_xlabel("Valores ausentes (%)")
        ax.set_ylabel("Dataset e coluna")

    fig.tight_layout()

    _salvar_grafico(fig, "valores_ausentes.png")

    plt.show()


def analisar_chave_composta(df, nome, colunas):
    
    valores_ausentes = df[colunas].isna().any(axis=1).sum()

    valores_duplicados = df.duplicated(subset=colunas).sum()

    combinacoes_unicas = df[colunas].drop_duplicates().shape[0]

    resultado = {
        "dataset": nome,
        "colunas": colunas,
        "valores_ausentes": int(valores_ausentes),
        "valores_duplicados": int(valores_duplicados),
        "combinacoes_unicas": int(combinacoes_unicas),
        "total_registros": len(df),
    }

    print(f"Análise da chave composta: {nome}.{', '.join(colunas)}")
    print(f"Registros com valores ausentes na chave: {valores_ausentes}")
    print(f"Combinações duplicadas: {valores_duplicados}")
    print(f"Combinações únicas: {combinacoes_unicas}")
    print(f"Total de registros: {len(df)}")

    return resultado



def grafico_distribuicao_numericas(df, nome="dataset", bins=30):

    variaveis = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if not variaveis:
        print(f"Nenhuma variável numérica encontrada em '{nome}'.")
        return

    quantidade = len(variaveis)
    colunas = min(3, quantidade)
    linhas = int(np.ceil(quantidade / colunas))

    fig, axes = plt.subplots(
        linhas,
        colunas,
        figsize=(6 * colunas, 4 * linhas),
        squeeze=False
    )

    for indice, coluna in enumerate(variaveis):
        ax = axes.flat[indice]
        valores = df[coluna].dropna()

        if valores.empty:
            ax.set_title(f"{coluna} (sem valores)")
            ax.set_axis_off()
            continue

        sns.histplot(
            data=valores,
            bins=bins,
            ax=ax
        )

        ax.set_title(coluna)
        ax.set_xlabel(coluna)
        ax.set_ylabel("Quantidade")

    for indice in range(quantidade, len(axes.flat)):
        axes.flat[indice].set_visible(False)

    fig.suptitle(
        f"Distribuição das Variáveis Numéricas - {nome}",
        y=1.02
    )

    fig.tight_layout()

    _salvar_grafico(
        fig,
        f"distribuicao_numericas_{_normalizar_nome(nome)}.png"
    )

    plt.show()


def grafico_distribuicao_categoricas(
    df,
    nome="dataset",
    colunas=None,
    top_n=10
):

    if colunas is None:
        colunas = df.select_dtypes(
            include=["object", "category", "string"]
        ).columns.tolist()

    else:
        colunas = list(colunas)

        inexistentes = [
            coluna for coluna in colunas
            if coluna not in df.columns
        ]

        if inexistentes:
            raise ValueError(
                f"Colunas não encontradas em '{nome}': {inexistentes}"
            )

    if not colunas:
        print(f"Nenhuma variável categórica encontrada em '{nome}'.")
        return

    quantidade = len(colunas)
    colunas_layout = min(2, quantidade)
    linhas = int(np.ceil(quantidade / colunas_layout))

    fig, axes = plt.subplots(
        linhas,
        colunas_layout,
        figsize=(14, 5 * linhas),
        squeeze=False
    )

    for indice, coluna in enumerate(colunas):
        ax = axes.flat[indice]

        frequencias = (
            df[coluna]
            .fillna("(Ausente)")
            .astype(str)
            .value_counts()
            .head(top_n)
            .sort_values(ascending=True)
        )

        ax.barh(
            frequencias.index,
            frequencias.values
        )

        ax.set_title(f"Categorias mais frequentes: {coluna}")
        ax.set_xlabel("Quantidade de registros")
        ax.set_ylabel(coluna)

    for indice in range(quantidade, len(axes.flat)):
        axes.flat[indice].set_visible(False)

    fig.suptitle(
        f"Distribuição das Variáveis Categóricas - {nome}",
        y=1.02
    )

    fig.tight_layout()

    _salvar_grafico(
        fig,
        f"distribuicao_categoricas_{_normalizar_nome(nome)}.png"
    )

    plt.show()


def grafico_correlacao(df, nome="dataset"):

    variaveis_numericas = df.select_dtypes(
        include="number"
    )

    if variaveis_numericas.shape[1] < 2:
        print(
            f"Não há variáveis numéricas suficientes em '{nome}' "
            "para calcular correlações."
        )
        return

    correlacao = variaveis_numericas.corr()

    fig, ax = plt.subplots(
        figsize=(
            max(10, correlacao.shape[1] * 0.8),
            max(8, correlacao.shape[0] * 0.7)
        )
    )

    sns.heatmap(
        correlacao,
        annot=correlacao.shape[1] <= 12,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        vmin=-1,
        vmax=1,
        ax=ax
    )

    ax.set_title(f"Matriz de Correlação - {nome}")

    fig.tight_layout()

    _salvar_grafico(
        fig,
        f"correlacao_{_normalizar_nome(nome)}.png"
    )

    plt.show()


# Funções auxiliares.

def _salvar_grafico(fig, nome_arquivo):

    PASTA_IMAGENS.mkdir(parents=True, exist_ok=True)

    caminho = PASTA_IMAGENS / nome_arquivo

    fig.savefig(
        caminho,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Gráfico salvo em: {caminho}")


def _normalizar_nome(nome):

    nome = nome.lower().strip()
    nome = re.sub(r"[^\w-]+", "_", nome)

    return nome
