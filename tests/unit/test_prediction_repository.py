import json
import pytest

import backend.database.connection as db_connection
from backend.database.models import create_predictions_table
from backend.repositories.prediction_repository import (
    save_prediction,
    get_predictions,
    get_prediction_by_id,
    delete_prediction,
)

# Cria um banco SQLite isolado para cada teste
@pytest.fixture
def database(tmp_path, monkeypatch):

    db_path = tmp_path / "test_delivery_risk.db"

    monkeypatch.setattr(db_connection, "DATABASE_PATH", db_path)
    monkeypatch.setattr(db_connection, "DATABASE_DIR", tmp_path)

    create_predictions_table()

    return db_path

# Dados simulados de entrada
def create_valid_input():

    return {
        "quantidade_itens": 2,
        "valor_total_produtos": 150.0,
        "frete_total": 25.0,
        "customer_city": "sao paulo",
        "customer_state": "SP"
    }

# Verifica se uma previsão é salva corretamente
def test_save_prediction(database):

    input_data = create_valid_input()

    prediction_id = save_prediction(
        1,
        "Atraso previsto",
        0.85,
        input_data
    )

    assert prediction_id > 0

    prediction = get_prediction_by_id(prediction_id)

    assert prediction["prediction"] == 1
    assert prediction["prediction_label"] == "Atraso previsto"
    assert prediction["delay_probability"] == 0.85
    assert prediction["created_at"] is not None

    saved_input = prediction["input_data"]

    assert saved_input == input_data

# Verifica se todas as previsões são consultadas
def test_get_predictions(database):

    input_data = create_valid_input()

    save_prediction(
        0,
        "Sem atraso previsto",
        0.20,
        input_data
    )

    save_prediction(
        1,
        "Atraso previsto",
        0.85,
        input_data
    )

    predictions = get_predictions()

    assert len(predictions) == 2
    assert predictions[0]["prediction"] == 1
    assert predictions[1]["prediction"] == 0

# Verifica o comportamento quando o ID não existe
def test_get_prediction_by_id_not_found(database):

    prediction = get_prediction_by_id(999)

    assert prediction is None

# Verifica se uma previsão é excluída corretamente
def test_delete_prediction(database):

    prediction_id = save_prediction(
        1,
        "Atraso previsto",
        0.85,
        create_valid_input()
    )

    deleted = delete_prediction(prediction_id)

    assert deleted is True
    assert get_prediction_by_id(prediction_id) is None

# Verifica o comportamento ao excluir um ID inexistente
def test_delete_prediction_not_found(database):

    deleted = delete_prediction(999)

    assert deleted is False
