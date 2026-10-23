import numpy as np
import pandas as pd


def validar_colunas(df, colunas, nome_dataset="dataset"):
   
    colunas_ausentes = [
        coluna for coluna in colunas
        if coluna not in df.columns
    ]

    if colunas_ausentes:
        raise ValueError(
            f"O dataset '{nome_dataset}' não possui as "
            f"colunas obrigatórias: {colunas_ausentes}."
        )

    return True


def converter_colunas_para_data(
    df,
    colunas,
    nome_dataset="dataset"
):
   
    validar_colunas(df, colunas, nome_dataset)

    df_tratado = df.copy()
    relatorio = []

    for coluna in colunas:
        valores_originais = df_tratado[coluna]

        ausentes_antes = int(valores_originais.isna().sum())

        datas_convertidas = pd.to_datetime(
            valores_originais,
            errors="coerce"
        )

        invalidas = (
            valores_originais.notna()
            & datas_convertidas.isna()
        )

        relatorio.append({
            "dataset": nome_dataset,
            "coluna": coluna,
            "ausentes_antes": ausentes_antes,
            "datas_invalidas": int(invalidas.sum()),
            "ausentes_depois": int(
                datas_convertidas.isna().sum()
            )
        })

        df_tratado[coluna] = datas_convertidas

    return df_tratado, pd.DataFrame(relatorio)


def normalizar_texto(
    df,
    colunas=None,
    nome_dataset="dataset"
):
    
    df_tratado = df.copy()

    if colunas is None:
        colunas = df_tratado.select_dtypes(
            include=["object", "string"]
        ).columns.tolist()

    validar_colunas(df_tratado, colunas, nome_dataset)

    for coluna in colunas:
        serie = df_tratado[coluna]

        mascara_textual = serie.map(
            lambda valor: isinstance(valor, str)
        )

        valores_textuais = serie.loc[mascara_textual].str.strip()

        valores_textuais = valores_textuais.replace(
            "", pd.NA
        )

        df_tratado.loc[
            mascara_textual, coluna
        ] = valores_textuais

    return df_tratado


def validar_chaves(
    df,
    colunas,
    nome_dataset="dataset",
    chave_unica=True
):
    
    validar_colunas(df, colunas, nome_dataset)

    valores_ausentes = int(
        df[colunas].isna().any(axis=1).sum()
    )

    duplicados = int(
        df.duplicated(subset=colunas, keep=False).sum()
    )

    quantidade_chaves_duplicadas = int(
        df.duplicated(subset=colunas, keep="first").sum()
    )

    resultado = {
        "dataset": nome_dataset,
        "colunas_chave": colunas,
        "total_registros": len(df),
        "registros_com_chave_ausente": valores_ausentes,
        "registros_em_chaves_duplicadas": duplicados,
        "ocorrencias_duplicadas_alem_da_primeira":
            quantidade_chaves_duplicadas,
        "chave_unica_valida": (
            valores_ausentes == 0 and duplicados == 0
        )
    }

    if chave_unica and not resultado["chave_unica_valida"]:
        print(
            f"Atenção: a chave {colunas} do dataset "
            f"'{nome_dataset}' apresenta inconsistências."
        )

    return resultado


def validar_valores_numericos(
    df,
    colunas,
    nome_dataset="dataset"
):
    
    validar_colunas(df, colunas, nome_dataset)

    relatorio = []

    for coluna in colunas:
        serie = df[coluna]

        ausentes = int(serie.isna().sum())

        valores_numericos = pd.to_numeric(
            serie,
            errors="coerce"
        )

        invalidos = int(
            (serie.notna() & valores_numericos.isna()).sum()
        )

        mascara_numerica = valores_numericos.notna()

        infinitos = int(
            (
                mascara_numerica
                & ~np.isfinite(valores_numericos)
            ).sum()
        )

        relatorio.append({
            "dataset": nome_dataset,
            "coluna": coluna,
            "valores_ausentes": ausentes,
            "valores_nao_numericos": invalidos,
            "valores_infinitos": infinitos
        })

    return pd.DataFrame(relatorio)


def resumir_qualidade_dados(
    df,
    nome_dataset="dataset"
):
    """
    Resume dimensões, tipos, ausências e duplicatas do DataFrame.

    Retorna um dicionário com indicadores gerais e um DataFrame
    com o detalhamento por coluna.
    """
    resumo_geral = {
        "dataset": nome_dataset,
        "total_linhas": len(df),
        "total_colunas": len(df.columns),
        "linhas_totalmente_duplicadas": int(
            df.duplicated().sum()
        ),
        "total_celulas_ausentes": int(
            df.isna().sum().sum()
        )
    }

    resumo_colunas = pd.DataFrame({
        "coluna": df.columns,
        "tipo_dado": [
            str(tipo) for tipo in df.dtypes
        ],
        "valores_ausentes": [
            int(quantidade)
            for quantidade in df.isna().sum()
        ],
        "percentual_ausente": [
            round(float(percentual), 2)
            for percentual in (
                df.isna().mean() * 100
            )
        ],
        "valores_distintos": [
            int(df[coluna].nunique(dropna=True))
            for coluna in df.columns
        ]
    })

    return resumo_geral, resumo_colunas
