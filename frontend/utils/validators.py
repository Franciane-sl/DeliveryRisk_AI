
def validate_prediction_data(dados: dict) -> list[str]:
    """
    Valida os campos obrigatórios do formulário de previsão.
    Retorna uma lista com os erros encontrados.
    """

    erros = []

    campos_obrigatorios = [
        campo
        for campo, valor in dados.items()
        if valor is None or valor == ""
    ]

    if campos_obrigatorios:
        erros.append(
            "Preencha todos os campos antes de gerar a previsão."
        )

    estados = [
        dados.get("customer_state", ""),
        dados.get("seller_state_mais_frequente", ""),
    ]

    if any(
        len(estado) != 2 or not estado.isalpha()
        for estado in estados
    ):
        erros.append(
            "Informe as siglas dos estados com exatamente duas letras."
        )

    return erros
