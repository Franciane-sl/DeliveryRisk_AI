
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parents[2]
METRICS_PATH = BASE_DIR / "reports" / "metrics.json"


# Carrega as métricas de avaliação do modelo
def get_model_metrics():
    logger.info("Carregando métricas do modelo.")

    if not METRICS_PATH.exists():
        logger.error("Arquivo de métricas não encontrado: %s", METRICS_PATH)
        raise FileNotFoundError("Arquivo de métricas não encontrado.")

    try:
        with open(METRICS_PATH, "r", encoding="utf-8") as file:
            metrics = json.load(file)

        logger.info("Métricas do modelo carregadas com sucesso.")
        return metrics

    except json.JSONDecodeError as exc:
        logger.exception("Arquivo de métricas possui formato JSON inválido.")
        raise ValueError(
            "O arquivo de métricas possui formato JSON inválido."
        ) from exc
