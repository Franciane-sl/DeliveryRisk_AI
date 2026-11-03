
from datetime import datetime


def format_percentage(value: float) -> str:
    """
    Formata uma probabilidade como porcentagem.
    """

    return f"{value:.2%}"


def format_datetime(value: str) -> str:
    """
    Formata uma data ISO para o padrão brasileiro.

    Se não conseguir interpretar a data, retorna o valor original.
    """

    if not value:
        return value

    try:
        data = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return data.strftime("%d/%m/%Y %H:%M:%S")

    except (ValueError, TypeError):
        return value
