
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from pipeline.src.tratamento import validar_colunas


COLUNAS_IDENTIFICADORES = [
    "order_id",
    "customer_id",
    "customer_unique_id",
]

COLUNAS_POSTERIORES_A_COMPRA = [
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_status",
]

COLUNAS_ALVO_AUXILIARES = [
    "delivery_delayed",
    "alvo_elegivel",
]

COLUNAS_CATEGORICAS_FORCADAS = [
    "customer_zip_code_prefix",
]

def definir_features(
    df,
    coluna_alvo="delivery_delayed",
):
  
    validar_colunas(df, [coluna_alvo], "base integrada")

    colunas_excluidas = (
        COLUNAS_IDENTIFICADORES
        + COLUNAS_POSTERIORES_A_COMPRA
        + COLUNAS_ALVO_AUXILIARES
        + [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_estimated_delivery_date",
        ]
    )

    colunas_excluidas_existentes = [
        coluna
        for coluna in colunas_excluidas
        if coluna in df.columns
    ]

    X = df.drop(
        columns=colunas_excluidas_existentes
    ).copy()

    y = df[coluna_alvo].copy()

    relatorio = {
        "coluna_alvo": coluna_alvo,
        "features_selecionadas": X.columns.tolist(),
        "colunas_excluidas": colunas_excluidas_existentes,
        "quantidade_features": X.shape[1],
    }

    validar_features(X, coluna_alvo=coluna_alvo)

    return X, y, relatorio


def criar_atributos_temporais(
    df,
    coluna_data="order_purchase_timestamp",
    remover_data_original=True,
):
    
    validar_colunas(df, [coluna_data], "base de pedidos")

    resultado = df.copy()

    datas = pd.to_datetime(
        resultado[coluna_data],
        errors="coerce",
    )

    resultado["ano_compra"] = datas.dt.year
    resultado["mes_compra"] = datas.dt.month
    resultado["dia_mes_compra"] = datas.dt.day
    resultado["dia_semana_compra"] = datas.dt.dayofweek
    resultado["hora_compra"] = datas.dt.hour

    resultado["fim_de_semana_compra"] = (
        datas.dt.dayofweek.isin([5, 6])
        .where(datas.notna(), pd.NA)
        .astype("boolean")
    )

    if remover_data_original:
        resultado = resultado.drop(columns=[coluna_data])

    return resultado


def separar_tipos_features(X):

    colunas_categoricas_forcadas = [
        coluna
        for coluna in COLUNAS_CATEGORICAS_FORCADAS
        if coluna in X.columns
    ]

    colunas_numericas = [
        coluna
        for coluna in X.select_dtypes(include=["number"]).columns
        if coluna not in colunas_categoricas_forcadas
    ]

    colunas_categoricas = X.select_dtypes(
        include=["object", "string", "category", "bool", "boolean"]
    ).columns.tolist()

    colunas_categoricas = list(
        dict.fromkeys(
            colunas_categoricas + colunas_categoricas_forcadas
        )
    )

    colunas_classificadas = (
        set(colunas_numericas)
        | set(colunas_categoricas)
    )

    colunas_nao_classificadas = [
        coluna
        for coluna in X.columns
        if coluna not in colunas_classificadas
    ]

    if colunas_nao_classificadas:
        raise TypeError(
            "Existem colunas que não foram classificadas como "
            f"numéricas ou categóricas: {colunas_nao_classificadas}"
        )

    return colunas_numericas, colunas_categoricas


def criar_pipeline_preprocessamento(
    colunas_numericas,
    colunas_categoricas,
    escalonar_numericas=True,
):
   
    colunas_numericas = list(colunas_numericas)
    colunas_categoricas = list(colunas_categoricas)

    sobrepostas = (
        set(colunas_numericas)
        & set(colunas_categoricas)
    )

    if sobrepostas:
        raise ValueError(
            "As seguintes colunas foram classificadas como "
            f"numéricas e categóricas: {sorted(sobrepostas)}"
        )

    transformacoes = []

    if colunas_numericas:
        etapas_numericas = [
            ("imputador", SimpleImputer(strategy="median")),
        ]

        if escalonar_numericas:
            etapas_numericas.append(
                ("escalonador", StandardScaler())
            )

        pipeline_numerico = Pipeline(
            steps=etapas_numericas
        )

        transformacoes.append(
            (
                "numericas",
                pipeline_numerico,
                colunas_numericas,
            )
        )

    if colunas_categoricas:
        pipeline_categorico = Pipeline(
            steps=[
                (
                    "imputador",
                    SimpleImputer(strategy="most_frequent"),
                ),
                (
                    "codificador",
                    OneHotEncoder(handle_unknown="ignore"),
                ),
            ]
        )

        transformacoes.append(
            (
                "categoricas",
                pipeline_categorico,
                colunas_categoricas,
            )
        )

    if not transformacoes:
        raise ValueError(
            "Nenhuma coluna numérica ou categórica foi informada."
        )

    return ColumnTransformer(
        transformers=transformacoes,
        remainder="drop",
        verbose_feature_names_out=False,
    )


def validar_features(
    X,
    coluna_alvo="delivery_delayed",
):
   
    if not isinstance(X, pd.DataFrame):
        raise TypeError("X deve ser um pandas.DataFrame.")

    if X.columns.duplicated().any():
        colunas_duplicadas = (
            X.columns[X.columns.duplicated()].tolist()
        )

        raise ValueError(
            f"Existem nomes de colunas duplicados: {colunas_duplicadas}"
        )

    colunas_proibidas = set(
        COLUNAS_IDENTIFICADORES
        + COLUNAS_POSTERIORES_A_COMPRA
        + COLUNAS_ALVO_AUXILIARES
        + [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_estimated_delivery_date",
        ]
    )

    colunas_encontradas = sorted(
        colunas_proibidas.intersection(X.columns)
    )

    if coluna_alvo in X.columns:
        colunas_encontradas.append(coluna_alvo)

    if colunas_encontradas:
        raise ValueError(
            "Foram encontradas colunas que não devem ser utilizadas "
            f"como features: {colunas_encontradas}"
        )

    return {
        "quantidade_linhas": len(X),
        "quantidade_features": X.shape[1],
        "colunas": X.columns.tolist(),
        "valores_ausentes_total": int(
            X.isna().sum().sum()
        ),
        "colunas_com_ausencias": (
            X.columns[X.isna().any()].tolist()
        ),
        "features_validas": True,
    }


def filtrar_pedidos_elegiveis(
    df,
    coluna_elegibilidade="alvo_elegivel",
    coluna_alvo="delivery_delayed"
):

    colunas_necessarias = [
        coluna_elegibilidade,
        coluna_alvo
    ]

    validar_colunas(
        df,
        colunas_necessarias,
        nome_dataset="base integrada"
    )

    mascara = (
        df[coluna_elegibilidade].eq(True)
        & df[coluna_alvo].notna()
    )

    base_elegivel = df.loc[mascara].copy()

    print(
        "Dimensões da base elegível:",
        base_elegivel.shape
    )

    print("\nDistribuição do alvo:")
    print(
        base_elegivel[coluna_alvo].value_counts().sort_index()
    )

    print("\nTaxa de atraso:")
    print(
        round(base_elegivel[coluna_alvo].mean(), 4)
    )

    return base_elegivel
