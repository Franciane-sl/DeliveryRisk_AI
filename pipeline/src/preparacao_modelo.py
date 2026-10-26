import pandas as pd

def dividir_dados_temporalmente(
    X,
    y,
    base_elegivel,
    coluna_data="order_purchase_timestamp",
    limite_treino="2018-03-01",
    limite_validacao="2018-06-01",
    limite_teste="2018-09-01",
):
    
    assert X.index.is_unique, "O índice de X contém duplicidades."
    assert y.index.is_unique, "O índice de y contém duplicidades."
    assert base_elegivel.index.is_unique, (
        "O índice de base_elegivel contém duplicidades."
    )
    assert X.index.equals(y.index), (
        "Os índices de X e y não estão alinhados."
    )
    assert X.index.isin(base_elegivel.index).all(), (
        "Existem índices de X ausentes em base_elegivel."
    )

    datas_compra = pd.to_datetime(
        base_elegivel.loc[X.index, coluna_data],
        errors="coerce",
    )

    assert datas_compra.notna().all(), (
        "Existem datas de compra ausentes ou inválidas."
    )
    assert y.notna().all(), (
        "Existem valores ausentes na variável-alvo."
    )
    assert set(y.unique()).issubset({0, 1}), (
        "A variável-alvo contém valores diferentes de 0 e 1."
    )


    limite_treino = pd.Timestamp(limite_treino)
    limite_validacao = pd.Timestamp(limite_validacao)
    limite_teste = pd.Timestamp(limite_teste)

    assert limite_treino < limite_validacao < limite_teste, (
        "Os limites temporais devem estar em ordem crescente."
    )

    mascara_treino = datas_compra < limite_treino

    mascara_validacao = (
        (datas_compra >= limite_treino)
        & (datas_compra < limite_validacao)
    )

    mascara_teste = (
        (datas_compra >= limite_validacao)
        & (datas_compra < limite_teste)
    )

    indice_cronologico = datas_compra.sort_values(
        kind="stable"
    ).index

    indice_treino = indice_cronologico[
        mascara_treino.loc[indice_cronologico].to_numpy()
    ]
    indice_validacao = indice_cronologico[
        mascara_validacao.loc[indice_cronologico].to_numpy()
    ]
    indice_teste = indice_cronologico[
        mascara_teste.loc[indice_cronologico].to_numpy()
    ]

    X_train = X.loc[indice_treino].copy()
    y_train = y.loc[indice_treino].copy()

    X_val = X.loc[indice_validacao].copy()
    y_val = y.loc[indice_validacao].copy()

    X_test = X.loc[indice_teste].copy()
    y_test = y.loc[indice_teste].copy()

 
    assert len(X_train) + len(X_val) + len(X_test) == len(X), (
        "A divisão não preservou todas as observações."
    )
    assert X_train.index.equals(y_train.index)
    assert X_val.index.equals(y_val.index)
    assert X_test.index.equals(y_test.index)

    assert len(X_train) > 0, "O conjunto de treino está vazio."
    assert len(X_val) > 0, "O conjunto de validação está vazio."
    assert len(X_test) > 0, "O conjunto de teste está vazio."

    return X_train, X_val, X_test, y_train, y_val, y_test


def resumir_conjunto(nome, X_parte, y_parte, datas_parte):

    quantidade = len(y_parte)
    atrasados = int(y_parte.eq(1).sum())
    no_prazo = int(y_parte.eq(0).sum())

    return {
        "conjunto": nome,
        "data_inicial": datas_parte.min(),
        "data_final": datas_parte.max(),
        "quantidade_pedidos": quantidade,
        "pedidos_atrasados": atrasados,
        "pedidos_no_prazo": no_prazo,
        "taxa_atraso_pct": (
            round(atrasados / quantidade * 100, 2)
            if quantidade
            else float("nan")
        ),
        "quantidade_features": X_parte.shape[1],
    }


def validar_divisao_temporal(
    X,
    y,
    X_train,
    y_train,
    X_val,
    y_val,
    X_test,
    y_test,
    base_elegivel,
    pipeline_preprocessamento,
    coluna_data="order_purchase_timestamp",
    limite_treino="2018-03-01",
    limite_validacao="2018-06-01",
    limite_teste="2018-09-01",
):

    assert X.index.is_unique, "O índice de X contém duplicidades."
    assert y.index.is_unique, "O índice de y contém duplicidades."

    for nome, X_parte, y_parte in [
        ("treino", X_train, y_train),
        ("validação", X_val, y_val),
        ("teste", X_test, y_test),
    ]:
        assert X_parte.index.is_unique, (
            f"O índice de X_{nome} contém duplicidades."
        )
        assert y_parte.index.is_unique, (
            f"O índice de y_{nome} contém duplicidades."
        )
        assert X_parte.index.equals(y_parte.index), (
            f"Índices desalinhados em {nome}."
        )

    indices_conjuntos = [
        set(X_train.index),
        set(X_val.index),
        set(X_test.index),
    ]

    assert indices_conjuntos[0].isdisjoint(indices_conjuntos[1]), (
        "Treino e validação possuem índices em comum."
    )
    assert indices_conjuntos[0].isdisjoint(indices_conjuntos[2]), (
        "Treino e teste possuem índices em comum."
    )
    assert indices_conjuntos[1].isdisjoint(indices_conjuntos[2]), (
        "Validação e teste possuem índices em comum."
    )

    assert len(X_train) + len(X_val) + len(X_test) == len(X), (
        "A quantidade total de registros mudou."
    )
    assert set.union(*indices_conjuntos) == set(X.index), (
        "Há registros ausentes ou extras após a divisão."
    )

    datas_compra = pd.to_datetime(
        base_elegivel.loc[X.index, coluna_data],
        errors="coerce",
    )

    assert datas_compra.notna().all(), (
        "Existem datas de compra ausentes ou inválidas."
    )

    limite_treino = pd.Timestamp(limite_treino)
    limite_validacao = pd.Timestamp(limite_validacao)
    limite_teste = pd.Timestamp(limite_teste)

    assert limite_treino < limite_validacao < limite_teste, (
        "Os limites temporais devem estar em ordem crescente."
    )

    datas_train = datas_compra.loc[X_train.index]
    datas_val = datas_compra.loc[X_val.index]
    datas_test = datas_compra.loc[X_test.index]

    assert (datas_train < limite_treino).all(), (
        "Treino contém pedidos fora do período definido."
    )
    assert (
        (datas_val >= limite_treino)
        & (datas_val < limite_validacao)
    ).all(), "Validação contém pedidos fora do período definido."

    assert (
        (datas_test >= limite_validacao)
        & (datas_test < limite_teste)
    ).all(), "Teste contém pedidos fora do período definido."

    assert datas_train.max() < datas_val.min(), (
        "A ordem temporal entre treino e validação não foi respeitada."
    )
    assert datas_val.max() < datas_test.min(), (
        "A ordem temporal entre validação e teste não foi respeitada."
    )

    assert X_train.columns.equals(X.columns), (
        "As features de treino diferem das features originais."
    )
    assert X_val.columns.equals(X.columns), (
        "As features de validação diferem das features originais."
    )
    assert X_test.columns.equals(X.columns), (
        "As features de teste diferem das features originais."
    )

    assert not hasattr(pipeline_preprocessamento, "transformers_"), (
        "O pipeline parece já ter sido ajustado. "
        "Confirme que nenhum ajuste foi feito usando dados completos."
    )

    resumo_divisao = pd.DataFrame([
        resumir_conjunto("Treino", X_train, y_train, datas_train),
        resumir_conjunto("Validação", X_val, y_val, datas_val),
        resumir_conjunto("Teste", X_test, y_test, datas_test),
    ])

    print(
        "Validações concluídas: alinhamento, cobertura dos registros, "
        "ausência de sobreposição e ordem temporal."
    )
    
    return resumo_divisao
