from unittest.mock import MagicMock
from urllib.parse import urlsplit

import pytest
import requests
from fastapi.testclient import TestClient

from frontend.api_client import APIClient
from backend.main import app
from backend.dependencies import get_pipeline
import backend.database.connection as db_connection


@pytest.fixture
def valid_payload():
    return {
        "quantidade_itens": 2,
        "valor_total_produtos": 150.0,
        "frete_total": 25.0,
        "quantidade_produtos_distintos": 2,
        "quantidade_vendedores_distintos": 1,
        "quantidade_categorias_distintas": 2,
        "product_weight_g_medio": 500.0,
        "product_length_cm_medio": 20.0,
        "product_height_cm_medio": 10.0,
        "product_width_cm_medio": 15.0,
        "quantidade_estados_vendedores_distintos": 1,
        "quantidade_cidades_vendedores_distintas": 1,
        "ano_compra": 2018,
        "mes_compra": 5,
        "dia_mes_compra": 15,
        "dia_semana_compra": 2,
        "hora_compra": 14,
        "customer_zip_code_prefix": 12345,
        "customer_city": "sao paulo",
        "customer_state": "SP",
        "categoria_produto_mais_frequente": "beleza",
        "seller_state_mais_frequente": "SP",
        "seller_city_mais_frequente": "sao paulo",
        "fim_de_semana_compra": False,
    }


@pytest.fixture
def fastapi_client(tmp_path, monkeypatch):
    db_path = tmp_path / "test_delivery_risk.db"

    monkeypatch.setattr(
        db_connection,
        "DATABASE_PATH",
        db_path,
    )

    monkeypatch.setattr(
        db_connection,
        "DATABASE_DIR",
        tmp_path,
    )

    pipeline = MagicMock()
    pipeline.classes_ = [0, 1]
    pipeline.predict.return_value = [1]
    pipeline.predict_proba.return_value = [[0.20, 0.80]]

    app.dependency_overrides[get_pipeline] = lambda: pipeline

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_pipeline, None)


@pytest.fixture
def api_client(fastapi_client, monkeypatch):
    def request_adapter(method, url, timeout=None, **kwargs):
        parsed_url = urlsplit(url)

        path = parsed_url.path

        if parsed_url.query:
            path += f"?{parsed_url.query}"

        response = fastapi_client.request(
            method=method,
            url=path,
            **kwargs,
        )

        response.ok = response.status_code < 400

        return response

    monkeypatch.setattr(
        requests,
        "request",
        request_adapter,
    )

    return APIClient(
        base_url="http://testserver",
        timeout=10,
    )

class TestAPIIntegration:

    def test_get_health(self, api_client):
        resultado = api_client.get_health()

        assert resultado["status"] == "healthy"
        assert resultado["model_loaded"] is True

    def test_create_prediction(
        self, api_client, valid_payload
    ):
        resultado = api_client.predict(valid_payload)

        assert resultado["prediction_id"] > 0
        assert resultado["prediction"] == 1
        assert resultado["prediction_label"] == "Atraso previsto"
        assert resultado["delay_probability"] == 0.80

    def test_get_predictions(
        self, api_client, valid_payload
    ):
        api_client.predict(valid_payload)

        resultado = api_client.get_predictions()

        assert isinstance(resultado, list)
        assert len(resultado) == 1

    def test_get_prediction_by_id(
        self, api_client, valid_payload
    ):
        previsao = api_client.predict(valid_payload)

        prediction_id = previsao["prediction_id"]

        resultado = api_client.get_prediction(prediction_id)

        assert isinstance(resultado, dict)
        assert resultado
        assert resultado["input_data"] == valid_payload

    def test_delete_prediction(
        self, api_client, valid_payload
    ):
        previsao = api_client.predict(valid_payload)

        prediction_id = previsao["prediction_id"]

        resultado = api_client.delete_prediction(prediction_id)

        assert resultado is None
        assert api_client.get_predictions() == []

    def test_get_metrics(self, api_client):
        resultado = api_client.get_metrics()

        assert isinstance(resultado, dict)
        assert resultado
