import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from backend.main import app
from backend.dependencies import get_pipeline
import backend.database.connection as db_connection


def create_valid_payload():
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
        "fim_de_semana_compra": False
    }


@pytest.fixture
def client(tmp_path, monkeypatch):
    db_path = tmp_path / "test_delivery_risk.db"

    monkeypatch.setattr(
        db_connection,
        "DATABASE_PATH",
        db_path
    )

    monkeypatch.setattr(
        db_connection,
        "DATABASE_DIR",
        tmp_path
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