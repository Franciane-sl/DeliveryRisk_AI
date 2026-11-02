from fastapi import APIRouter, Depends, status

from backend.dependencies import get_pipeline
from backend.schemas import PredictionInput, PredictionOutput
from backend.services.prediction_service import predict_delivery_risk
from backend.services.history_service import save_prediction_history


prediction_router = APIRouter(tags=["Predictions"])


# Realiza a previsão de risco de atraso na entrega
@prediction_router.post(
    "/predict",
    response_model=PredictionOutput,
    status_code=status.HTTP_200_OK
)
def predict(
    input_data: PredictionInput,
    pipeline=Depends(get_pipeline)
):
    result = predict_delivery_risk(pipeline, input_data)

    prediction = result["prediction"]

    prediction_label = (
        "Atraso previsto"
        if prediction == 1
        else "Sem atraso previsto"
    )

    prediction_id = save_prediction_history(
        prediction=prediction,
        prediction_label=prediction_label,
        delay_probability=result["delay_probability"],
        input_data=input_data.model_dump(mode="json")
    )

    return PredictionOutput(
        prediction_id=prediction_id,
        prediction=prediction,
        prediction_label=prediction_label,
        delay_probability=result["delay_probability"],
        message="Previsão realizada e salva no histórico."
    )
