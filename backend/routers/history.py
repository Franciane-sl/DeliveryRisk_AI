from fastapi import APIRouter, HTTPException, status

from backend.schemas import PredictionHistoryItem
from backend.services.history_service import (
    get_prediction_history,
    get_prediction_details,
    remove_prediction,
)

history_router = APIRouter(tags=["History"])


@history_router.get(
    "/predictions",
    response_model=list[PredictionHistoryItem]
)
def list_predictions():
    return get_prediction_history()


@history_router.get(
    "/predictions/{prediction_id}",
    response_model=PredictionHistoryItem
)
def get_prediction(prediction_id: int):
    prediction = get_prediction_details(prediction_id)

    if prediction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Previsão não encontrada."
        )

    return prediction


@history_router.delete(
    "/predictions/{prediction_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_prediction(prediction_id: int):
    deleted = remove_prediction(prediction_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Previsão não encontrada."
        )
