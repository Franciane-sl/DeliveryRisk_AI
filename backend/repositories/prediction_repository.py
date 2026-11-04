import json
from datetime import datetime, timezone

from backend.database.connection import get_connection


# Função para salvar uma previsão no histórico
def save_prediction(
    prediction,
    prediction_label,
    delay_probability,
    input_data
):
    connection = get_connection()

    try:
        # Converte os dados de entrada para JSON
        input_json = json.dumps(
            input_data,
            ensure_ascii=False
        )

        cursor = connection.execute(
            """
            INSERT INTO predictions (
                prediction,
                prediction_label,
                delay_probability,
                input_data,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                prediction,
                prediction_label,
                delay_probability,
                input_json,
                datetime.now(timezone.utc).isoformat()
            )
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


# Função para consultar todas as previsões
def get_predictions():

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT *
            FROM predictions
            ORDER BY id DESC
            """
        )

        return [
                 convert_prediction_row(row)
                 for row in cursor.fetchall()
        ]

    finally:
        connection.close()


# Função para consultar uma previsão pelo ID
def get_prediction_by_id(prediction_id):

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT *
            FROM predictions
            WHERE id = ?
            """,
            (prediction_id,)
        )

        row = cursor.fetchone()

        return convert_prediction_row(row) if row else None

    finally:
        connection.close()


# Função para excluir uma previsão pelo ID
def delete_prediction(prediction_id):

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            DELETE FROM predictions
            WHERE id = ?
            """,
            (prediction_id,)
        )

        connection.commit()

        return cursor.rowcount > 0

    finally:
        connection.close()

# Converte os dados de uma linha do banco para dicionário
def convert_prediction_row(row):

    prediction = dict(row)

    if prediction.get("input_data"):
        prediction["input_data"] = json.loads(
            prediction["input_data"]
        )

    return prediction
