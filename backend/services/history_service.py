
import logging

from backend.repositories.prediction_repository import (
    save_prediction,
    get_predictions,
    get_prediction_by_id,
    delete_prediction,
)

logger = logging.getLogger(__name__)


# Salva uma previsão no histórico
def save_prediction_history(
    prediction,
    prediction_label,
    delay_probability,
    input_data
):
    logger.info("Salvando previsão no histórico.")

    prediction_id = save_prediction(
        prediction=prediction,
        prediction_label=prediction_label,
        delay_probability=delay_probability,
        input_data=input_data
    )

    logger.info(
        "Previsão salva com sucesso. ID: %s.",
        prediction_id
    )

    return prediction_id


# Retorna o histórico completo de previsões
def get_prediction_history():
    logger.info("Consultando histórico de previsões.")

    predictions = get_predictions()

    logger.info(
        "Consulta do histórico concluída. Registros encontrados: %s.",
        len(predictions)
    )

    return predictions


# Retorna os detalhes de uma previsão pelo ID
def get_prediction_details(prediction_id):
    logger.info(
        "Consultando previsão no histórico. ID: %s.",
        prediction_id
    )

    prediction = get_prediction_by_id(prediction_id)

    if prediction is None:
        logger.warning(
            "Previsão não encontrada no histórico. ID: %s.",
            prediction_id
        )

    return prediction


# Remove uma previsão do histórico
def remove_prediction(prediction_id):
    logger.info(
        "Solicitação de exclusão de previsão. ID: %s.",
        prediction_id
    )

    deleted = delete_prediction(prediction_id)

    if deleted:
        logger.info(
            "Previsão excluída com sucesso. ID: %s.",
            prediction_id
        )
    else:
        logger.warning(
            "Previsão não encontrada para exclusão. ID: %s.",
            prediction_id
        )

    return deleted
