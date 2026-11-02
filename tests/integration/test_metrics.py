
from fastapi.testclient import TestClient

from backend.main import app


def test_get_metrics():
    with TestClient(app) as client:
        response = client.get("/metrics")

    assert response.status_code == 200

    data = response.json()

    assert data["projeto"] == "DeliveryRisk AI"

    assert data["modelo_selecionado"]["algoritmo"] == "Random Forest"

    assert data["modelo_selecionado"]["experimento"] == 4

    assert "accuracy" in data["avaliacao_validacao"]
    assert "precision" in data["avaliacao_validacao"]
    assert "recall" in data["avaliacao_validacao"]
    assert "f1" in data["avaliacao_validacao"]
    assert "roc_auc" in data["avaliacao_validacao"]

    assert "accuracy" in data["avaliacao_teste"]
    assert "f1" in data["avaliacao_teste"]

    assert len(data["robustez_temporal"]) == 3

    assert data["serializacao"]["previsoes_preservadas"] is True
    assert data["serializacao"]["probabilidades_preservadas"] is True
