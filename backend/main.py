
import logging
from contextlib import asynccontextmanager
from pathlib import Path

import joblib
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from backend.core.logging_config import setup_logging
from backend.core.exception_handlers import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler,
)
from backend.database.models import create_predictions_table
from backend.routers.health import health_router
from backend.routers.predictions import prediction_router
from backend.routers.history import history_router
from backend.routers.metrics import metrics_router

# Configuração dos logs
setup_logging()
logger = logging.getLogger(__name__)


# Caminho para a raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho para o pipeline serializado
MODEL_PATH = BASE_DIR / "models" / "delivery_risk_pipeline.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Iniciando DeliveryRisk AI.")

    try:
        create_predictions_table()
        logger.info("Banco de dados inicializado com sucesso.")

        if not MODEL_PATH.exists():
            logger.critical("Arquivo do modelo não encontrado: %s", MODEL_PATH)
            raise FileNotFoundError("Arquivo do modelo não encontrado.")

        app.state.pipeline = joblib.load(MODEL_PATH)
        logger.info("Pipeline carregado com sucesso.")

        yield

    except Exception:
        logger.exception("Erro durante o ciclo de vida da aplicação.")
        raise

    finally:
        if hasattr(app.state, "pipeline"):
            del app.state.pipeline

        logger.info("Aplicação encerrada.")


app = FastAPI(
    title="DeliveryRisk AI",
    description="API para previsão de risco de atraso em entregas.",
    version="1.0.0",
    lifespan=lifespan,
    exception_handlers={
        StarletteHTTPException: http_exception_handler,
        RequestValidationError: validation_exception_handler,
        Exception: general_exception_handler,
    },
)


# Registro dos roteadores
app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(history_router)
app.include_router(metrics_router)

# Para executar a API:
# uvicorn backend.main:app --reload