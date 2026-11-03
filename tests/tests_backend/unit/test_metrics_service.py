from backend.services.metrics_service import get_model_metrics


def test_get_model_metrics():
    metrics = get_model_metrics()

    assert metrics["projeto"] == "DeliveryRisk AI"

    assert metrics["modelo_selecionado"]["algoritmo"] == "Random Forest"

    assert metrics["modelo_selecionado"]["experimento"] == 4

    assert "accuracy" in metrics["avaliacao_teste"]

    assert "f1" in metrics["avaliacao_validacao"]

    assert len(metrics["robustez_temporal"]) == 3

    assert metrics["serializacao"]["previsoes_preservadas"] is True
