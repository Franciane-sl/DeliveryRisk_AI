
import logging

import pandas as pd

logger = logging.getLogger(__name__)


# Executa a previsão de risco de atraso na entrega
def predict_delivery_risk(pipeline, input_data):
    logger.info("Iniciando previsão de risco de atraso.")

    data = input_data.model_dump()

    input_df = pd.DataFrame([data])

    prediction = int(pipeline.predict(input_df)[0])

    probabilities = pipeline.predict_proba(input_df)[0]

    class_index = list(pipeline.classes_).index(1)

    delay_probability = float(probabilities[class_index])

    logger.info(
        "Previsão realizada com sucesso. Classe prevista: %s.",
        prediction
    )

    logger.debug(
        "Probabilidade de atraso calculada: %.4f.",
        delay_probability
    )

    return {
        "prediction": prediction,
        "delay_probability": delay_probability
    }
