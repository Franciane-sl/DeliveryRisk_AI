import sys
from pathlib import Path
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

ROOT_DIR = Path(__file__).resolve().parents[3]
FRONTEND_DIR = ROOT_DIR / "frontend"
PAGES_DIR = FRONTEND_DIR / "pages"

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

if str(FRONTEND_DIR) not in sys.path:
    sys.path.insert(0, str(FRONTEND_DIR))

from frontend.api_client import APIClientError


def executar_pagina(nome_pagina):


    caminho = PAGES_DIR / nome_pagina

    return AppTest.from_file(str(caminho)).run(timeout=30)

DADOS_PREVISOES = [
    {
        "id": 1,
        "prediction": 1,
        "prediction_label": "Atraso previsto",
        "delay_probability": 0.75,
        "created_at": "2026-10-20T10:30:00",
    },
    {
        "id": 2,
        "prediction": 0,
        "prediction_label": "Sem atraso previsto",
        "delay_probability": 0.25,
        "created_at": "2026-10-21T11:30:00",
    },
]

DADOS_PREVISAO = {
    "prediction_id": 1,
    "prediction": 1,
    "prediction_label": "Atraso previsto",
    "delay_probability": 0.75,
    "message": "Existe risco de atraso na entrega.",
    "created_at": "2026-10-20T10:30:00",
    "input_data": {
        "quantidade_itens": 2,
        "quantidade_produtos_distintos": 2,
        "quantidade_vendedores_distintos": 1,
        "quantidade_categorias_distintas": 1,
        "quantidade_estados_vendedores_distintos": 1,
        "quantidade_cidades_vendedores_distintas": 1,
        "valor_total_produtos": 150.0,
        "frete_total": 20.0,
        "product_weight_g_medio": 500.0,
        "product_length_cm_medio": 20.0,
        "product_height_cm_medio": 10.0,
        "product_width_cm_medio": 15.0,
        "ano_compra": 2018,
        "mes_compra": 5,
        "dia_mes_compra": 10,
        "dia_semana_compra": 3,
        "hora_compra": 14,
        "customer_zip_code_prefix": 12345,
        "customer_city": "sao paulo",
        "customer_state": "SP",
        "categoria_produto_mais_frequente": "beleza",
        "seller_state_mais_frequente": "SP",
        "seller_city_mais_frequente": "sao paulo",
        "fim_de_semana_compra": False,
    },
}


@patch("frontend.api_client.APIClient")
def test_visao_geral_com_dados(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.return_value = DADOS_PREVISOES

    at = executar_pagina("visao_Geral.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_visao_geral_sem_previsoes(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.return_value = []

    at = executar_pagina("visao_Geral.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_visao_geral_com_erro_na_api(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.side_effect = APIClientError(
        "Erro de conexão com a API."
    )

    at = executar_pagina("visao_Geral.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_nova_previsao_carrega_formulario(mock_api_client):

    at = executar_pagina("nova_Previsao.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_nova_previsao_com_erro_na_api(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.predict.side_effect = APIClientError(
        "Erro ao gerar previsão."
    )

    at = executar_pagina("nova_Previsao.py")

    assert not at.exception

@patch("frontend.api_client.APIClient")
def test_historico_com_previsoes(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.return_value = DADOS_PREVISOES
    mock_api.get_prediction.return_value = DADOS_PREVISAO

    at = executar_pagina("historico.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_historico_sem_previsoes(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.return_value = []

    at = executar_pagina("historico.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_historico_com_erro_na_api(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.side_effect = APIClientError(
        "Erro ao carregar histórico."
    )

    at = executar_pagina("historico.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_historico_detalhes_de_previsao(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.return_value = DADOS_PREVISOES
    mock_api.get_prediction.return_value = DADOS_PREVISAO

    at = executar_pagina("historico.py")

    assert not at.exception


@patch("frontend.api_client.APIClient")
def test_historico_exclusao_com_erro_na_api(mock_api_client):

    mock_api = mock_api_client.return_value
    mock_api.get_predictions.return_value = DADOS_PREVISOES
    mock_api.get_prediction.return_value = DADOS_PREVISAO
    mock_api.delete_prediction.side_effect = APIClientError(
        "Erro ao excluir previsão."
    )

    at = executar_pagina("historico.py")

    assert not at.exception


def test_arquivos_das_paginas_existentes():

    assert (PAGES_DIR / "visao_Geral.py").is_file()
    assert (PAGES_DIR / "nova_Previsao.py").is_file()
    assert (PAGES_DIR / "historico.py").is_file()


def test_arquivo_principal_streamlit_existente():

    caminho = FRONTEND_DIR / "streamlit_app.py"

    assert caminho.is_file()
