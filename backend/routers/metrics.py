
import logging

from fastapi import APIRouter, HTTPException, status

from backend.services.metrics_service import get_model_metrics

logger = logging.getLogger(__name__)

metrics_router = APIRouter(tags=["Metrics"])


# Retorna as métricas de avaliação do modelo
@metrics_router.get(
    "/metrics",
    responses={
        500: {
            "description": "Erro ao carregar as métricas do modelo."
        }
    }
)
def get_metrics():
    logger.info("Consultando métricas do modelo.")

    try:
        metrics = get_model_metrics()

        logger.info("Métricas do modelo carregadas com sucesso.")

        return metrics

    except (FileNotFoundError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível carregar as métricas do modelo."
        )
