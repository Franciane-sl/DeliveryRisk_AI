from typing import Literal
from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)

# Schema para validação de entrada do endpoint POST /predict
class PredictionInput(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        strict=True,
        allow_inf_nan=False,
    )

    quantidade_itens: int | None = Field(
        ...,
        ge=1,
        description="Quantidade total de itens do pedido.",
    )
    quantidade_produtos_distintos: int | None = Field(
        ...,
        ge=1,
        description="Quantidade de produtos distintos no pedido.",
    )
    quantidade_vendedores_distintos: int | None = Field(
        ...,
        ge=1,
        description="Quantidade de vendedores distintos no pedido.",
    )
    quantidade_categorias_distintas: int | None = Field(
        ...,
        ge=1,
        description="Quantidade de categorias distintas no pedido.",
    )
    quantidade_estados_vendedores_distintos: int | None = Field(
        ...,
        ge=1,
        description="Quantidade de estados distintos dos vendedores.",
    )
    quantidade_cidades_vendedores_distintas: int | None = Field(
        ...,
        ge=1,
        description="Quantidade de cidades distintas dos vendedores.",
    )

    valor_total_produtos: float | None = Field(
        ...,
        ge=0,
        description="Valor total dos produtos do pedido.",
    )
    frete_total: float | None = Field(
        ...,
        ge=0,
        description="Valor total do frete do pedido.",
    )
    product_weight_g_medio: float | None = Field(
        ...,
        ge=0,
        description="Peso médio dos produtos, em gramas.",
    )
    product_length_cm_medio: float | None = Field(
        ...,
        ge=0,
        description="Comprimento médio dos produtos, em centímetros.",
    )
    product_height_cm_medio: float | None = Field(
        ...,
        ge=0,
        description="Altura média dos produtos, em centímetros.",
    )
    product_width_cm_medio: float | None = Field(
        ...,
        ge=0,
        description="Largura média dos produtos, em centímetros.",
    )

    
    ano_compra: int | None = Field(
        ...,
        description="Ano em que o pedido foi realizado.",
    )
    mes_compra: int | None = Field(
        ...,
        ge=1,
        le=12,
        description="Mês da compra, de 1 a 12.",
    )
    dia_mes_compra: int | None = Field(
        ...,
        ge=1,
        le=31,
        description="Dia do mês em que a compra foi realizada.",
    )
    dia_semana_compra: int | None = Field(
        ...,
        ge=0,
        le=6,
        description="Dia da semana: segunda-feira = 0 e domingo = 6.",
    )
    hora_compra: int | None = Field(
        ...,
        ge=0,
        le=23,
        description="Hora da compra, no formato de 24 horas.",
    )

    
    customer_zip_code_prefix: int | None = Field(
        ...,
        ge=0,
        le=99999,
        description=(
            "Prefixo numérico do CEP do cliente. "
            "É tratado como variável categórica pelo pipeline."
        ),
    )
    customer_city: str | None = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Cidade do cliente.",
    )
    customer_state: str | None = Field(
        ...,
        min_length=2,
        max_length=2,
        pattern=r"^[A-Z]{2}$",
        description="Sigla da unidade federativa do cliente.",
    )
    categoria_produto_mais_frequente: str | None = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Categoria de produto mais frequente no pedido.",
    )
    seller_state_mais_frequente: str | None = Field(
        ...,
        min_length=2,
        max_length=2,
        pattern=r"^[A-Z]{2}$",
        description="Sigla do estado mais frequente entre os vendedores.",
    )
    seller_city_mais_frequente: str | None = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Cidade mais frequente entre os vendedores.",
    )
    fim_de_semana_compra: bool | None = Field(
        ...,
        description="Indica se a compra ocorreu no fim de semana.",
    )

#Schema para validação de saída do endpoint POST /predict
class PredictionOutput(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        strict=True,
        allow_inf_nan=False,
    )

    prediction_id: int = Field(
        ...,
        gt=0,
        description="Identificador do registro criado no histórico SQLite.",
    )
    prediction: Literal[0, 1] = Field(
        ...,
        description="Classe prevista: 0 para sem atraso e 1 para atraso.",
    )
    prediction_label: Literal[
        "Sem atraso previsto",
        "Atraso previsto",
    ] = Field(
        ...,
        description="Descrição textual da classe prevista.",
    )
    delay_probability: float = Field(
        ...,
        ge=0,
        le=1,
        description=(
            "Probabilidade estimada para a classe de atraso (1), "
            "entre 0 e 1. Não representa garantia de atraso."
        ),
    )
    message: str = Field(
        ...,
        min_length=1,
        description="Mensagem explicativa do resultado da previsão.",
    )

# Schema para validação de saída do endpoint GET /predictions
class PredictionHistoryItem(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        strict=True
    )

    id: int = Field(gt=0)

    prediction: Literal[0, 1]

    prediction_label: Literal[
        "Sem atraso previsto",
        "Atraso previsto"
    ]

    delay_probability: float = Field(
        ge=0,
        le=1,
        allow_inf_nan=False
    )

    input_data: dict | None = Field(
        default=None,
        description="Dados de entrada utilizados para gerar a previsão."
    )

    created_at: datetime

    @field_validator("created_at", mode="before")
    @classmethod
    def parse_created_at(cls, value):

        if isinstance(value, str):
            return datetime.fromisoformat(value)

        return value
