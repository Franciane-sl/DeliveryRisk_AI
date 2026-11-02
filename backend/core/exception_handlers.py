
import logging

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse


logger = logging.getLogger(__name__)


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):
    error_names = {
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        409: "Conflict",
        422: "Unprocessable Entity",
        500: "Internal Server Error",
        503: "Service Unavailable",
    }

    if exc.status_code >= 500:
        logger.error(
            "Erro HTTP %s na rota %s: %s",
            exc.status_code,
            request.url.path,
            exc.detail
        )
    else:
        logger.warning(
            "Requisição HTTP %s na rota %s: %s",
            exc.status_code,
            request.url.path,
            exc.detail
        )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": error_names.get(
                exc.status_code,
                "HTTP Error"
            ),
            "message": str(exc.detail)
        },
        headers=exc.headers
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    logger.warning(
        "Erro de validação na rota %s. Quantidade de erros: %s",
        request.url.path,
        len(exc.errors())
    )

    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "message": "Os dados enviados são inválidos."
        }
    )


async def general_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
        "Erro interno não tratado na rota %s.",
        request.url.path
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Ocorreu um erro interno ao processar a solicitação."
        }
    )
