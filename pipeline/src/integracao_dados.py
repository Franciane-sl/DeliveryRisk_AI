import pandas as pd

from pipeline.src.tratamento import (
    validar_colunas,
    validar_chaves,
)

def _valor_mais_frequente(serie):
    
    valores = serie.dropna()

    if valores.empty:
        return pd.NA

    frequencias = valores.value_counts()
    maior_frequencia = frequencias.max()

    empatados = frequencias[
        frequencias == maior_frequencia
    ].index.tolist()

    return sorted(empatados, key=str)[0]


def agregar_itens_por_pedido(
    order_items,
    products,
    sellers,
):
   
    validar_colunas(
        order_items,
        [
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "price",
            "freight_value",
        ],
        "order_items",
    )

    validar_colunas(
        products,
        ["product_id"],
        "products",
    )

    validar_colunas(
        sellers,
        ["seller_id"],
        "sellers",
    )

    validar_chaves(
        products,
        ["product_id"],
        "products",
    )

    validar_chaves(
        sellers,
        ["seller_id"],
        "sellers",
    )

    itens = order_items.copy()
    produtos = products.copy()
    vendedores = sellers.copy()

    for df, coluna, nome in [
        (itens, "product_id", "order_items"),
        (produtos, "product_id", "products"),
        (itens, "seller_id", "order_items"),
        (vendedores, "seller_id", "sellers"),
    ]:
        if df[coluna].isna().any():
            print(
                f"Atenção: existem valores ausentes em "
                f"'{coluna}' no dataset '{nome}'."
            )

    colunas_produtos = [
        coluna
        for coluna in [
            "product_id",
            "product_category_name",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm",
        ]
        if coluna in produtos.columns
    ]

    produtos = produtos[colunas_produtos]

    itens_enriquecidos = itens.merge(
        produtos,
        on="product_id",
        how="left",
        validate="many_to_one",
        indicator="_produto_merge",
    )

    produtos_sem_correspondencia = int(
        (
            itens_enriquecidos["_produto_merge"]
            == "left_only"
        ).sum()
    )

    itens_enriquecidos = itens_enriquecidos.drop(
        columns="_produto_merge"
    )

    colunas_vendedores = [
        coluna
        for coluna in [
            "seller_id",
            "seller_state",
            "seller_city",
        ]
        if coluna in vendedores.columns
    ]

    vendedores = vendedores[colunas_vendedores]

    itens_enriquecidos = itens_enriquecidos.merge(
        vendedores,
        on="seller_id",
        how="left",
        validate="many_to_one",
        indicator="_vendedor_merge",
    )

    vendedores_sem_correspondencia = int(
        (
            itens_enriquecidos["_vendedor_merge"]
            == "left_only"
        ).sum()
    )

    itens_enriquecidos = itens_enriquecidos.drop(
        columns="_vendedor_merge"
    )

    colunas_numericas = [
        "price",
        "freight_value",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    for coluna in colunas_numericas:
        if coluna in itens_enriquecidos.columns:
            itens_enriquecidos[coluna] = pd.to_numeric(
                itens_enriquecidos[coluna],
                errors="coerce",
            )

    agregacoes = {
        "order_item_id": "count",
        "price": lambda serie: serie.sum(min_count=1),
        "freight_value": lambda serie: serie.sum(
            min_count=1
        ),
        "product_id": "nunique",
        "seller_id": "nunique",
    }

    renomear = {
        "order_item_id": "quantidade_itens",
        "price": "valor_total_produtos",
        "freight_value": "frete_total",
        "product_id": "quantidade_produtos_distintos",
        "seller_id": "quantidade_vendedores_distintos",
    }

    agregacoes = {
        coluna: funcao
        for coluna, funcao in agregacoes.items()
        if coluna in itens_enriquecidos.columns
    }

    agregados = itens_enriquecidos.groupby(
        "order_id",
        as_index=False,
        dropna=False,
    ).agg(agregacoes)

    agregados = agregados.rename(columns=renomear)

    agrupado = itens_enriquecidos.groupby(
        "order_id",
        dropna=False,
    )

    if "product_category_name" in itens_enriquecidos.columns:
        categorias = agrupado[
            "product_category_name"
        ].agg(
            categoria_produto_mais_frequente=(
                _valor_mais_frequente
            ),
            quantidade_categorias_distintas="nunique",
        ).reset_index()

        agregados = agregados.merge(
            categorias,
            on="order_id",
            how="left",
            validate="one_to_one",
        )

    colunas_medidas = [
        coluna
        for coluna in [
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm",
        ]
        if coluna in itens_enriquecidos.columns
    ]

    if colunas_medidas:
        medidas = agrupado[colunas_medidas].mean().reset_index()

        medidas = medidas.rename(
            columns={
                coluna: f"{coluna}_medio"
                for coluna in colunas_medidas
            }
        )

        agregados = agregados.merge(
            medidas,
            on="order_id",
            how="left",
            validate="one_to_one",
        )

    for coluna in ["seller_state", "seller_city"]:
        if coluna in itens_enriquecidos.columns:
            nome_contagem = (
                "quantidade_estados_vendedores_distintos"
                if coluna == "seller_state"
                else "quantidade_cidades_vendedores_distintas"
            )

            resumo_localizacao = agrupado[coluna].agg(
                _valor_mais_frequente
            ).rename(
                f"{coluna}_mais_frequente"
            ).to_frame()

            resumo_localizacao[nome_contagem] = (
                agrupado[coluna].nunique()
            )

            resumo_localizacao = (
                resumo_localizacao.reset_index()
            )

            agregados = agregados.merge(
                resumo_localizacao,
                on="order_id",
                how="left",
                validate="one_to_one",
            )

    relatorio = {
        "linhas_order_items": len(order_items),
        "pedidos_com_itens": int(
            order_items["order_id"].nunique()
        ),
        "itens_sem_produto_correspondente":
            produtos_sem_correspondencia,
        "itens_sem_vendedor_correspondente":
            vendedores_sem_correspondencia,
        "linhas_apos_agregacao": len(agregados),
        "pedidos_com_order_id_ausente": int(
            order_items["order_id"].isna().sum()
        ),
    }

    return agregados, relatorio


def criar_variavel_alvo(
    df,
    coluna_data_real="order_delivered_customer_date",
    coluna_data_estimada="order_estimated_delivery_date",
):
    validar_colunas(
        df,
        [coluna_data_real, coluna_data_estimada],
        "base para criação do alvo",
    )

    resultado = df.copy()

    data_real = pd.to_datetime(
        resultado[coluna_data_real],
        errors="coerce",
    )

    data_estimada = pd.to_datetime(
        resultado[coluna_data_estimada],
        errors="coerce",
    )

    elegiveis = data_real.notna() & data_estimada.notna()

    resultado["delivery_delayed"] = pd.Series(
        pd.NA,
        index=resultado.index,
        dtype="Int64",
    )

    resultado.loc[elegiveis, "delivery_delayed"] = (
        data_real.loc[elegiveis]
        > data_estimada.loc[elegiveis]
    ).astype("int64")

    resultado["alvo_elegivel"] = elegiveis

    relatorio = {
        "total_pedidos": len(resultado),
        "pedidos_elegiveis": int(elegiveis.sum()),
        "pedidos_sem_alvo": int((~elegiveis).sum()),
        "sem_data_real": int(data_real.isna().sum()),
        "sem_data_estimada": int(data_estimada.isna().sum()),
        "sem_ambas_as_datas": int(
            (data_real.isna() & data_estimada.isna()).sum()
        ),
        "entregas_atrasadas": int(
            (resultado["delivery_delayed"] == 1).sum()
        ),
        "entregas_no_prazo": int(
            (resultado["delivery_delayed"] == 0).sum()
        ),
    }

    return resultado, relatorio

def integrar_datasets(
    orders,
    customers,
    itens_agregados,
):
    
    validar_colunas(
        orders,
        [
            "order_id",
            "customer_id",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ],
        "orders",
    )

    validar_colunas(
        customers,
        ["customer_id"],
        "customers",
    )

    validar_colunas(
        itens_agregados,
        ["order_id"],
        "itens_agregados",
    )

    validar_chaves(orders, ["order_id"], "orders")
    validar_chaves(customers, ["customer_id"], "customers")
    validar_chaves(itens_agregados, ["order_id"], "itens_agregados")

    base = orders.copy()

    colunas_customers = [
        coluna
        for coluna in customers.columns
        if coluna != "customer_id"
    ]

    base = base.merge(
        customers[["customer_id"] + colunas_customers],
        on="customer_id",
        how="left",
        validate="many_to_one",
        indicator="_cliente_merge",
    )

    clientes_sem_correspondencia = int(
        (base["_cliente_merge"] == "left_only").sum()
    )

    base = base.drop(columns="_cliente_merge")

    base = base.merge(
        itens_agregados,
        on="order_id",
        how="left",
        validate="one_to_one",
        indicator="_itens_merge",
    )

    pedidos_sem_itens = int(
        (base["_itens_merge"] == "left_only").sum()
    )

    base = base.drop(columns="_itens_merge")

    base, relatorio_alvo = criar_variavel_alvo(base)

    relatorio = {
        "pedidos_originais": len(orders),
        "clientes_sem_correspondencia":
            clientes_sem_correspondencia,
        "pedidos_sem_itens": pedidos_sem_itens,
        "linhas_base_integrada": len(base),
        "relatorio_alvo": relatorio_alvo,
    }

    return base, relatorio

def validar_integracao(
    base,
    quantidade_pedidos_esperada=None,
):
   
    validar_colunas(
        base,
        ["order_id", "delivery_delayed"],
        "base integrada",
    )

    total_linhas = len(base)
    pedidos_distintos = int(base["order_id"].nunique())
    pedidos_ausentes = int(base["order_id"].isna().sum())
    linhas_duplicadas = int(
        base.duplicated(subset=["order_id"], keep=False).sum()
    )

    resultado = {
        "total_linhas": total_linhas,
        "pedidos_distintos": pedidos_distintos,
        "pedidos_com_id_ausente": pedidos_ausentes,
        "linhas_em_pedidos_duplicados": linhas_duplicadas,
        "uma_linha_por_pedido": (
            pedidos_ausentes == 0
            and linhas_duplicadas == 0
            and total_linhas == pedidos_distintos
        ),
        "quantidade_pedidos_esperada": (
            quantidade_pedidos_esperada
        ),
        "quantidade_pedidos_compativel": (
            None
            if quantidade_pedidos_esperada is None
            else total_linhas == quantidade_pedidos_esperada
        ),
        "valores_alvo_ausentes": int(
            base["delivery_delayed"].isna().sum()
        ),
        "valores_alvo_invalidos": int(
            (
                base["delivery_delayed"].notna()
                & ~base["delivery_delayed"].isin([0, 1])
            ).sum()
        ),
    }

    return resultado

def resumir_variavel_alvo(base):
    
    validar_colunas(
        base,
        ["delivery_delayed"],
        "base integrada",
    )

    alvo = base["delivery_delayed"]

    quantidade_atrasados = int((alvo == 1).sum())
    quantidade_no_prazo = int((alvo == 0).sum())
    quantidade_sem_alvo = int(alvo.isna().sum())
    total = len(base)

    distribuicao = (
        alvo.value_counts(dropna=False)
        .rename_axis("delivery_delayed")
        .reset_index(name="quantidade")
    )

    distribuicao["percentual_sobre_total"] = (
        distribuicao["quantidade"] / total * 100
        if total > 0
        else 0.0
    )

    resumo = {
        "total_pedidos": total,
        "entregas_atrasadas": quantidade_atrasados,
        "entregas_no_prazo": quantidade_no_prazo,
        "pedidos_sem_alvo": quantidade_sem_alvo,
        "percentual_atrasados_entre_elegiveis": (
            round(
                quantidade_atrasados
                / (quantidade_atrasados + quantidade_no_prazo)
                * 100,
                2,
            )
            if quantidade_atrasados + quantidade_no_prazo > 0
            else None
        ),
    }

    return resumo, distribuicao


def construir_base_integrada(datasets):
 
    datasets_necessarios = [
        "orders",
        "order_items",
        "customers",
        "products",
        "sellers",
    ]

    ausentes = [
        nome
        for nome in datasets_necessarios
        if nome not in datasets
    ]

    if ausentes:
        raise ValueError(
            f"Datasets obrigatórios ausentes: {ausentes}."
        )

    orders = datasets["orders"].copy(deep=True)
    order_items = datasets["order_items"].copy(deep=True)
    customers = datasets["customers"].copy(deep=True)
    products = datasets["products"].copy(deep=True)
    sellers = datasets["sellers"].copy(deep=True)

    itens_agregados, relatorio_itens = (
        agregar_itens_por_pedido(
            order_items,
            products,
            sellers,
        )
    )

    base, relatorio_integracao = integrar_datasets(
        orders,
        customers,
        itens_agregados,
    )

    relatorio_validacao = validar_integracao(
        base,
        quantidade_pedidos_esperada=len(orders),
    )

    resumo_alvo, distribuicao_alvo = (
        resumir_variavel_alvo(base)
    )

    relatorios = {
        "agregacao_itens": relatorio_itens,
        "integracao": relatorio_integracao,
        "validacao": relatorio_validacao,
        "resumo_alvo": resumo_alvo,
        "distribuicao_alvo": distribuicao_alvo,
    }

    return base, relatorios


def investigar_pedidos_sem_itens(base):
   
    colunas_itens = [
        "quantidade_itens",
        "valor_total_produtos",
        "frete_total",
        "quantidade_produtos_distintos",
        "quantidade_vendedores_distintos",
        "categoria_produto_mais_frequente",
        "quantidade_categorias_distintas",
        "product_weight_g_medio",
        "product_length_cm_medio",
        "product_height_cm_medio",
        "product_width_cm_medio",
        "seller_state_mais_frequente",
        "quantidade_estados_vendedores_distintos",
        "seller_city_mais_frequente",
        "quantidade_cidades_vendedores_distintas",
    ]

    colunas_obrigatorias = [
        "quantidade_itens",
        "delivery_delayed",
        *colunas_itens,
    ]

    colunas_ausentes = [
        coluna
        for coluna in colunas_obrigatorias
        if coluna not in base.columns
    ]

    if colunas_ausentes:
        raise ValueError(
            "Colunas obrigatórias ausentes na base: "
            f"{colunas_ausentes}"
        )

    pedidos_sem_itens = base["quantidade_itens"].isna()

    ausencias_colunas_itens = (
        base.loc[pedidos_sem_itens, colunas_itens]
        .isna()
        .sum()
        .rename("valores_ausentes")
        .to_frame()
    )

    alvo_preenchido = (
        base.loc[pedidos_sem_itens, "delivery_delayed"]
        .notna()
        .sum()
    )

    return {
        "total_pedidos_sem_itens": int(pedidos_sem_itens.sum()),
        "ausencias_colunas_itens": ausencias_colunas_itens,
        "pedidos_sem_itens_com_alvo_preenchido": int(
            alvo_preenchido
        ),
    }
