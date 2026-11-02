from backend.database.connection import get_connection

# Função para criar a tabela de histórico de previsões
def create_predictions_table():

    connection = get_connection()

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prediction INTEGER NOT NULL CHECK (prediction IN (0, 1)),
                prediction_label TEXT NOT NULL,
                delay_probability REAL NOT NULL
                    CHECK (delay_probability BETWEEN 0 AND 1),
                input_data TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )

        columns = connection.execute(
            "PRAGMA table_info(predictions)"
        ).fetchall()

        column_names = [column["name"] for column in columns]

        if "input_data" not in column_names:
            connection.execute(
                "ALTER TABLE predictions ADD COLUMN input_data TEXT"
            )

        connection.commit()

    finally:
        connection.close()
