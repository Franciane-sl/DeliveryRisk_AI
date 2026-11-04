
from pathlib import Path

import pandas as pd


def carregar_dataset(caminho):
   
    caminho = Path(caminho)

    try:
        return pd.read_csv(caminho)

    except FileNotFoundError as erro:
        raise FileNotFoundError(
            f"O arquivo '{caminho}' não foi encontrado. "
            "Verifique se o caminho está correto."
        ) from erro

    except pd.errors.EmptyDataError as erro:
        raise ValueError(
            f"O arquivo '{caminho}' está vazio."
        ) from erro

    except pd.errors.ParserError as erro:
        raise ValueError(
            f"Não foi possível interpretar o arquivo CSV "
            f"'{caminho}': {erro}"
        ) from erro

    except Exception as erro:
        raise RuntimeError(
            f"Ocorreu um erro ao carregar o dataset "
            f"'{caminho}': {erro}"
        ) from erro


def carregar_datasets(caminho_dados="data/raw"):

    diretorio = Path(caminho_dados)

    arquivos = {
        "orders": "olist_orders_dataset.csv",
        "order_items": "olist_order_items_dataset.csv",
        "customers": "olist_customers_dataset.csv",
        "products": "olist_products_dataset.csv",
        "sellers": "olist_sellers_dataset.csv",
    }

    datasets = {}

    for nome, arquivo in arquivos.items():
        caminho = diretorio / arquivo

        print(f"Carregando dataset: {arquivo}")

        datasets[nome] = carregar_dataset(caminho)

        print(
            f"Dataset '{nome}' carregado com sucesso: "
            f"{datasets[nome].shape[0]} linhas e "
            f"{datasets[nome].shape[1]} colunas."
        )

    print("\nTodos os datasets foram carregados com sucesso!")

    return datasets
