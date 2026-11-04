
import logging

from fastapi import APIRouter, Request

logger = logging.getLogger(__name__)

health_router = APIRouter(tags=["Health"])


# Verifica a saúde da API e a disponibilidade do pipeline
@health_router.get("/health")
def health_check(request: Request):
    pipeline_loaded = hasattr(request.app.state, "pipeline")

    if pipeline_loaded:
        logger.info("Health check realizado. Pipeline disponível.")
    else:
        logger.warning("Health check realizado. Pipeline indisponível.")

    return {
        "status": "healthy" if pipeline_loaded else "unhealthy",
        "model_loaded": pipeline_loaded
    }
