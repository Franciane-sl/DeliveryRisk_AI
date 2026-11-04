import time

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
)
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def definir_configuracoes_modelos():

    return {
        "Logistic Regression": [
            {"C": 0.01, "class_weight": "balanced"},
            {"C": 0.1, "class_weight": None},
            {"C": 0.1, "class_weight": "balanced"},
            {"C": 1.0, "class_weight": None},
            {"C": 1.0, "class_weight": "balanced"},
            {"C": 10.0, "class_weight": "balanced"},
        ],
        "Random Forest": [
            {
                "n_estimators": 100,
                "max_depth": 5,
                "class_weight": None,
            },
            {
                "n_estimators": 100,
                "max_depth": 10,
                "class_weight": None,
            },
            {
                "n_estimators": 200,
                "max_depth": 5,
                "class_weight": None,
            },
            {
                "n_estimators": 100,
                "max_depth": 10,
                "class_weight": "balanced",
            },
            {
                "n_estimators": 200,
                "max_depth": 5,
                "class_weight": "balanced",
            },
            {
                "n_estimators": 200,
                "max_depth": 10,
                "class_weight": "balanced",
            },
        ],
        "Gradient Boosting": [
            {"n_estimators": 50, "learning_rate": 0.01},
            {"n_estimators": 50, "learning_rate": 0.1},
            {"n_estimators": 100, "learning_rate": 0.01},
            {"n_estimators": 100, "learning_rate": 0.1},
            {"n_estimators": 200, "learning_rate": 0.01},
            {"n_estimators": 200, "learning_rate": 0.1},
        ],
    }


def criar_modelo(nome_modelo, parametros, random_state=42):

    if nome_modelo == "Logistic Regression":
        return LogisticRegression(
            C=parametros["C"],
            class_weight=parametros["class_weight"],
            max_iter=1000,
            random_state=random_state,
        )

    if nome_modelo == "Random Forest":
        return RandomForestClassifier(
            n_estimators=parametros["n_estimators"],
            max_depth=parametros["max_depth"],
            class_weight=parametros["class_weight"],
            random_state=random_state,
            n_jobs=-1,
        )

    if nome_modelo == "Gradient Boosting":
        return GradientBoostingClassifier(
            n_estimators=parametros["n_estimators"],
            learning_rate=parametros["learning_rate"],
            random_state=random_state,
        )

    raise ValueError(f"Modelo não reconhecido: {nome_modelo}")


def criar_pipeline_modelo(
    nome_modelo,
    parametros,
    colunas_numericas,
    colunas_categoricas,
    random_state=42,
):
    

    if nome_modelo == "Gradient Boosting":
        transformador_numerico = Pipeline(
            steps=[
                ("imputacao", SimpleImputer(strategy="median")),
            ]
        )

        transformador_categorico = Pipeline(
            steps=[
                (
                    "imputacao",
                    SimpleImputer(strategy="most_frequent"),
                ),
                (
                    "codificacao",
                    OneHotEncoder(
                        handle_unknown="ignore",
                        min_frequency=0.01,
                        sparse_output=False,
                    ),
                ),
            ]
        )

    else:
        transformador_numerico = Pipeline(
            steps=[
                ("imputacao", SimpleImputer(strategy="median")),
                ("escalonamento", StandardScaler()),
            ]
        )

        transformador_categorico = Pipeline(
            steps=[
                (
                    "imputacao",
                    SimpleImputer(strategy="most_frequent"),
                ),
                (
                    "codificacao",
                    OneHotEncoder(handle_unknown="ignore"),
                ),
            ]
        )

    pre_processador = ColumnTransformer(
        transformers=[
            (
                "numericas",
                transformador_numerico,
                colunas_numericas,
            ),
            (
                "categoricas",
                transformador_categorico,
                colunas_categoricas,
            ),
        ],
    )

    modelo = criar_modelo(
        nome_modelo=nome_modelo,
        parametros=parametros,
        random_state=random_state,
    )

    return Pipeline(
        steps=[
            ("pre_processamento", pre_processador),
            ("modelo", modelo),
        ]
    )


def treinar_modelo(modelo, X_treino, y_treino):
    
    if not X_treino.index.equals(y_treino.index):
        raise ValueError(
            "Os índices de X_treino e y_treino não estão alinhados."
        )

    inicio = time.perf_counter()

    modelo.fit(X_treino, y_treino)

    tempo_treinamento = time.perf_counter() - inicio

    return modelo, tempo_treinamento


def prever_modelo(modelo, X):

    inicio = time.perf_counter()

    previsoes = modelo.predict(X)
    probabilidades = modelo.predict_proba(X)[:, 1]

    tempo_predicao = time.perf_counter() - inicio

    return previsoes, probabilidades, tempo_predicao


def executar_experimentos(
    nome_modelo,
    configuracoes,
    X_train,
    y_train,
    X_val,
    y_val,
    colunas_numericas,
    colunas_categoricas,
    random_state=42,
):

    if not X_train.index.equals(y_train.index):
        raise ValueError("Os índices de treino não estão alinhados.")

    if not X_val.index.equals(y_val.index):
        raise ValueError("Os índices de validação não estão alinhados.")

    if list(X_train.columns) != list(X_val.columns):
        raise ValueError(
            "Treino e validação devem possuir as mesmas colunas "
            "na mesma ordem."
        )

    if X_train.empty or X_val.empty:
        raise ValueError(
            "Os conjuntos de treino e validação não podem estar vazios."
        )

    if y_train.nunique() != 2 or y_val.nunique() != 2:
        raise ValueError(
            "Treino e validação precisam conter as duas classes do alvo."
        )

    if not configuracoes:
        raise ValueError(
            "A lista de configurações não pode estar vazia."
        )

    resultados = []

    for numero, parametros in enumerate(configuracoes, start=1):
        print(
            f"{nome_modelo} — experimento "
            f"{numero}/{len(configuracoes)}: {parametros}"
        )

        pipeline = criar_pipeline_modelo(
            nome_modelo=nome_modelo,
            parametros=parametros,
            colunas_numericas=colunas_numericas,
            colunas_categoricas=colunas_categoricas,
            random_state=random_state,
        )

        pipeline, tempo_treinamento = treinar_modelo(
            modelo=pipeline,
            X_treino=X_train,
            y_treino=y_train,
        )

        previsoes, probabilidades, tempo_predicao = prever_modelo(
            modelo=pipeline,
            X=X_val,
        )

        acuracia = accuracy_score(y_val, previsoes)
        precisao = precision_score(
            y_val,
            previsoes,
            zero_division=0,
        )
        recall = recall_score(
            y_val,
            previsoes,
            zero_division=0,
        )
        f1 = f1_score(
            y_val,
            previsoes,
            zero_division=0,
        )
        roc_auc = roc_auc_score(y_val, probabilidades)

        resultados.append(
            {
                "modelo": nome_modelo,
                "experimento": numero,
                "hiperparametros": parametros.copy(),
                "accuracy": acuracia,
                "precision": precisao,
                "recall": recall,
                "f1": f1,
                "roc_auc": roc_auc,
                "tempo_treinamento_s": tempo_treinamento,
                "tempo_predicao_s": tempo_predicao,
                "pipeline": pipeline,
            }
        )

        print(
            f"Acurácia: {acuracia:.4f} | "
            f"Precisão: {precisao:.4f} | "
            f"Recall: {recall:.4f} | "
            f"F1: {f1:.4f} | "
            f"ROC-AUC: {roc_auc:.4f} | "
            f"Treinamento: {tempo_treinamento:.2f}s | "
            f"Predição: {tempo_predicao:.2f}s"
        )

    return resultados


def registrar_resultados(resultados):
   

    if not resultados:
        raise ValueError("A lista de resultados está vazia.")

    tabela = pd.DataFrame(
        [
            {
                chave: valor
                for chave, valor in resultado.items()
                if chave != "pipeline"
            }
            for resultado in resultados
        ]
    )

    return tabela.sort_values(
        by="f1",
        ascending=False,
    ).reset_index(drop=True)

