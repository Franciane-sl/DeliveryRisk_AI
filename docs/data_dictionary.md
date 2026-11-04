# Dicionário de Dados — DeliveryRisk AI

## 1. Visão geral

Este documento descreve as variáveis utilizadas no projeto **DeliveryRisk AI**, desde os datasets originais do Brazilian E-Commerce Public Dataset by Olist até os dados utilizados pelo modelo de Machine Learning e pela aplicação.

O dicionário está organizado nas seguintes categorias:

1. Datasets originais.
2. Base integrada por pedido.
3. Variáveis derivadas e agregadas.
4. Features utilizadas pelo modelo.
5. Variável-alvo.
6. Dados de entrada e saída da API.
7. Estrutura do banco de dados.

O objetivo é documentar o significado das variáveis, seus tipos, suas unidades de medida e sua utilização no sistema.

## 2. Datasets originais

O projeto utiliza cinco arquivos CSV do Brazilian E-Commerce Public Dataset by Olist.

### 2.1. Orders — Pedidos

Arquivo: `olist_orders_dataset.csv`

Contém informações sobre os pedidos realizados na plataforma.

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `order_id` | String | Identificador único do pedido. |
| `customer_id` | String | Identificador do cliente associado ao pedido. |
| `order_status` | String | Status atual do pedido. |
| `order_purchase_timestamp` | Datetime | Data e horário da realização da compra. |
| `order_approved_at` | Datetime | Data e horário da aprovação do pagamento. |
| `order_delivered_carrier_date` | Datetime | Data em que o pedido foi entregue à transportadora. |
| `order_delivered_customer_date` | Datetime | Data em que o pedido foi efetivamente entregue ao cliente. |
| `order_estimated_delivery_date` | Datetime | Data estimada para a entrega do pedido. |

**Utilização:** dataset principal da integração. Fornece os identificadores, as informações temporais e as datas utilizadas na construção da variável-alvo.

### 2.2. Customers — Clientes

Arquivo: `olist_customers_dataset.csv`

Contém informações sobre a localização dos clientes.

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `customer_id` | String | Identificador do cliente associado ao pedido. |
| `customer_unique_id` | String | Identificador único do cliente, independente dos pedidos realizados. |
| `customer_zip_code_prefix` | Inteiro/String | Prefixo do CEP do cliente. |
| `customer_city` | String | Cidade do cliente. |
| `customer_state` | String | Sigla do estado do cliente. |

**Utilização:** fornece informações geográficas do cliente, incorporadas à base integrada por meio de `customer_id`.

### 2.3. Order Items — Itens dos pedidos

Arquivo: `olist_order_items_dataset.csv`

Contém informações sobre os produtos incluídos em cada pedido.

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `order_id` | String | Identificador do pedido. |
| `order_item_id` | Inteiro | Número sequencial do item dentro do pedido. |
| `product_id` | String | Identificador do produto. |
| `seller_id` | String | Identificador do vendedor. |
| `shipping_limit_date` | Datetime | Data limite para o envio do item pelo vendedor. |
| `price` | Decimal | Preço do produto no item do pedido. |
| `freight_value` | Decimal | Valor do frete associado ao item. |

**Utilização:** fornece os dados necessários para calcular quantidades, valores totais, diversidade de produtos e vendedores e características dos produtos de cada pedido.

### 2.4. Products — Produtos

Arquivo: `olist_products_dataset.csv`

Contém características dos produtos comercializados.

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `product_id` | String | Identificador único do produto. |
| `product_category_name` | String | Categoria do produto. |
| `product_name_lenght` | Inteiro | Comprimento do nome do produto. |
| `product_description_lenght` | Inteiro | Comprimento da descrição do produto. |
| `product_photos_qty` | Inteiro | Quantidade de fotografias do produto. |
| `product_weight_g` | Decimal | Peso do produto em gramas. |
| `product_length_cm` | Decimal | Comprimento do produto em centímetros. |
| `product_height_cm` | Decimal | Altura do produto em centímetros. |
| `product_width_cm` | Decimal | Largura do produto em centímetros. |

**Utilização:** fornece categoria e características físicas dos produtos. As dimensões e o peso são agregados por pedido.

### 2.5. Sellers — Vendedores

Arquivo: `olist_sellers_dataset.csv`

Contém informações geográficas dos vendedores.

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `seller_id` | String | Identificador único do vendedor. |
| `seller_zip_code_prefix` | Inteiro/String | Prefixo do CEP do vendedor. |
| `seller_city` | String | Cidade do vendedor. |
| `seller_state` | String | Sigla do estado do vendedor. |

**Utilização:** fornece informações geográficas dos vendedores associados aos itens dos pedidos.

## 3. Base integrada por pedido

Arquivo: `data/processed/base_integrada.parquet`

A base integrada é construída a partir dos cinco datasets originais.

Sua granularidade é de **uma linha por pedido**, utilizando `order_id` como identificador da unidade de análise.

O processo de integração contempla:

- Agregação dos itens por pedido.
- Enriquecimento dos itens com informações de produtos.
- Enriquecimento dos itens com informações de vendedores.
- Integração com os dados de clientes.
- Integração com os dados de pedidos.
- Criação da variável-alvo `delivery_delayed`.

### 3.1. Identificadores e informações do pedido

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `order_id` | String | Identificador único do pedido. |
| `customer_id` | String | Identificador do cliente associado ao pedido. |
| `customer_unique_id` | String | Identificador único do cliente. |
| `order_status` | String | Status do pedido. |
| `order_purchase_timestamp` | Datetime | Data e horário da compra. |
| `order_approved_at` | Datetime | Data e horário da aprovação do pagamento. |
| `order_delivered_carrier_date` | Datetime | Data de entrega do pedido à transportadora. |
| `order_delivered_customer_date` | Datetime | Data efetiva de entrega ao cliente. |
| `order_estimated_delivery_date` | Datetime | Data estimada de entrega. |

### 3.2. Informações geográficas do cliente

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `customer_zip_code_prefix` | Inteiro | Prefixo do CEP do cliente. |
| `customer_city` | String | Cidade do cliente. |
| `customer_state` | String | Estado do cliente. |

### 3.3. Variáveis agregadas dos itens

Os dados originalmente registrados por item são agrupados por `order_id`.

| Coluna | Tipo lógico | Descrição |
|---|---|---|
| `quantidade_itens` | Inteiro | Quantidade total de itens registrados no pedido. |
| `valor_total_produtos` | Decimal | Soma dos preços dos produtos do pedido. |
| `frete_total` | Decimal | Soma dos valores de frete dos itens do pedido. |
| `quantidade_produtos_distintos` | Inteiro | Quantidade de produtos diferentes no pedido. |
| `quantidade_vendedores_distintos` | Inteiro | Quantidade de vendedores diferentes associados ao pedido. |
| `categoria_produto_mais_frequente` | String | Categoria de produto com maior frequência no pedido. |
| `quantidade_categorias_distintas` | Inteiro | Quantidade de categorias diferentes presentes no pedido. |
| `product_weight_g_medio` | Decimal | Peso médio dos produtos do pedido, em gramas. |
| `product_length_cm_medio` | Decimal | Comprimento médio dos produtos, em centímetros. |
| `product_height_cm_medio` | Decimal | Altura média dos produtos, em centímetros. |
| `product_width_cm_medio` | Decimal | Largura média dos produtos, em centímetros. |
| `seller_state_mais_frequente` | String | Estado mais frequente entre os vendedores do pedido. |
| `quantidade_estados_vendedores_distintos` | Inteiro | Quantidade de estados diferentes dos vendedores. |
| `seller_city_mais_frequente` | String | Cidade mais frequente entre os vendedores do pedido. |
| `quantidade_cidades_vendedores_distintas` | Inteiro | Quantidade de cidades diferentes dos vendedores. |

**Regras de agregação:**

- Quantidade de itens: contagem de `order_item_id`.
- Valor total dos produtos: soma de `price`.
- Frete total: soma de `freight_value`.
- Produtos distintos: contagem de `product_id` únicos.
- Vendedores distintos: contagem de `seller_id` únicos.
- Categorias distintas: contagem de categorias únicas.
- Peso e dimensões: média dos valores dos itens.
- Categoria e localização mais frequentes: valor com maior frequência. Em caso de empate, é selecionado o primeiro valor em ordem lexicográfica.

Quando um pedido possui itens sem correspondência com produtos ou vendedores, as informações não encontradas permanecem ausentes após o enriquecimento.

## 4. Features utilizadas pelo modelo

O modelo utiliza 24 features, selecionadas por meio da função `definir_features()`, implementada em `pipeline/src/feature_engineering.py`.

As features são divididas em variáveis numéricas e categóricas.

### 4.1. Features numéricas

| Feature | Tipo | Descrição | Unidade |
|---|---|---|---|
| `quantidade_itens` | Inteiro | Quantidade total de itens do pedido. | Itens |
| `quantidade_produtos_distintos` | Inteiro | Quantidade de produtos diferentes. | Produtos |
| `quantidade_vendedores_distintos` | Inteiro | Quantidade de vendedores diferentes. | Vendedores |
| `quantidade_categorias_distintas` | Inteiro | Quantidade de categorias diferentes. | Categorias |
| `quantidade_estados_vendedores_distintos` | Inteiro | Quantidade de estados diferentes dos vendedores. | Estados |
| `quantidade_cidades_vendedores_distintas` | Inteiro | Quantidade de cidades diferentes dos vendedores. | Cidades |
| `valor_total_produtos` | Decimal | Soma dos valores dos produtos. | Unidade monetária do dataset |
| `frete_total` | Decimal | Soma dos valores de frete. | Unidade monetária do dataset |
| `product_weight_g_medio` | Decimal | Peso médio dos produtos. | Gramas |
| `product_length_cm_medio` | Decimal | Comprimento médio dos produtos. | Centímetros |
| `product_height_cm_medio` | Decimal | Altura média dos produtos. | Centímetros |
| `product_width_cm_medio` | Decimal | Largura média dos produtos. | Centímetros |
| `ano_compra` | Inteiro | Ano em que a compra foi realizada. | Ano |
| `mes_compra` | Inteiro | Mês em que a compra foi realizada. | 1 a 12 |
| `dia_mes_compra` | Inteiro | Dia do mês em que a compra foi realizada. | 1 a 31 |
| `dia_semana_compra` | Inteiro | Dia da semana da compra. Segunda-feira = 0 e domingo = 6. | 0 a 6 |
| `hora_compra` | Inteiro | Hora em que a compra foi realizada. | 0 a 23 |

### 4.2. Features categóricas e booleanas

| Feature | Tipo | Descrição |
|---|---|---|
| `customer_zip_code_prefix` | Categórica | Prefixo do CEP do cliente. |
| `customer_city` | Categórica | Cidade do cliente. |
| `customer_state` | Categórica | Estado do cliente. |
| `categoria_produto_mais_frequente` | Categórica | Categoria de produto mais frequente no pedido. |
| `seller_state_mais_frequente` | Categórica | Estado mais frequente entre os vendedores. |
| `seller_city_mais_frequente` | Categórica | Cidade mais frequente entre os vendedores. |
| `fim_de_semana_compra` | Booleana | Indica se a compra ocorreu em um sábado ou domingo. |

**Total:** 24 features, sendo 17 numéricas e 7 categóricas ou booleanas.

### 4.3. Criação dos atributos temporais

Os atributos temporais são derivados de `order_purchase_timestamp`.

| Atributo | Regra de criação |
|---|---|
| `ano_compra` | Extração do ano da data de compra. |
| `mes_compra` | Extração do mês da data de compra. |
| `dia_mes_compra` | Extração do dia do mês. |
| `dia_semana_compra` | Extração do dia da semana, de 0 a 6. |
| `hora_compra` | Extração da hora da compra. |
| `fim_de_semana_compra` | Verdadeiro quando a compra ocorre no sábado ou domingo. |

Após a criação desses atributos, a coluna original `order_purchase_timestamp` é removida da representação utilizada pelo modelo.

### 4.4. Pré-processamento das features

O pipeline de pré-processamento realiza transformações diferentes conforme o tipo de variável.

**Variáveis numéricas:**

- Imputação de valores ausentes utilizando a mediana.
- Padronização com `StandardScaler`, quando habilitada.

**Variáveis categóricas:**

- Imputação de valores ausentes utilizando a categoria mais frequente.
- Codificação com `OneHotEncoder`.
- Configuração `handle_unknown="ignore"` para categorias não observadas durante o treinamento.

O prefixo do CEP (`customer_zip_code_prefix`) é tratado como categórico, mesmo sendo representado numericamente.

As transformações são ajustadas no conjunto de treinamento e reutilizadas nas etapas posteriores por meio do pipeline serializado.

## 5. Variável-alvo

A variável-alvo do projeto é `delivery_delayed`.

Ela representa se o pedido foi entregue após a data estimada.

| Valor | Significado |
|---|---|
| `0` | Pedido entregue no prazo ou antes da data estimada. |
| `1` | Pedido entregue após a data estimada. |
| `NaN` | Pedido sem informações suficientes para determinar a classificação. |

### 5.1. Regra de construção

A variável é criada pela comparação entre:

- `order_delivered_customer_date`: data real de entrega.
- `order_estimated_delivery_date`: data estimada de entrega.

A regra aplicada é:

```python
delivery_delayed = (
    order_delivered_customer_date
    > order_estimated_delivery_date
)
```

A classificação somente é realizada quando as duas datas estão disponíveis.

Pedidos sem uma das datas permanecem com `delivery_delayed` ausente.

### 5.2. Variável auxiliar de elegibilidade

A coluna `alvo_elegivel` indica se o pedido possui as informações necessárias para a classificação.

| Valor | Significado |
|---|---|
| `True` | Pedido possui data real e estimada de entrega. |
| `False` | Pedido não possui todas as datas necessárias. |

Essa variável é utilizada durante a construção e validação do alvo, mas não é fornecida ao modelo como feature.

## 6. Colunas excluídas do treinamento

Algumas colunas são mantidas na base integrada para rastreabilidade e construção do alvo, mas são excluídas da matriz de features.

| Coluna | Motivo da exclusão |
|---|---|
| `order_id` | Identificador do pedido, sem utilização como feature. |
| `customer_id` | Identificador do cliente. |
| `customer_unique_id` | Identificador único do cliente. |
| `order_delivered_carrier_date` | Informação posterior à compra. |
| `order_delivered_customer_date` | Informação posterior à compra e utilizada na construção do alvo. |
| `order_status` | Status do pedido, que pode refletir informações posteriores à compra. |
| `order_purchase_timestamp` | Data original substituída pelos atributos temporais derivados. |
| `order_approved_at` | Data de aprovação do pagamento, excluída da seleção de features. |
| `order_estimated_delivery_date` | Data utilizada na construção do alvo e excluída da seleção de features. |
| `delivery_delayed` | Variável-alvo, não utilizada como entrada do modelo. |
| `alvo_elegivel` | Variável auxiliar de elegibilidade, não utilizada como entrada do modelo. |

A exclusão dessas variáveis busca evitar o uso de identificadores e informações que poderiam causar vazamento de dados (*data leakage*).

## 7. Dados de entrada da API

O endpoint `POST /predict` recebe os atributos necessários para realizar uma previsão.

O schema `PredictionInput`, definido em `backend/schemas.py`, valida os 24 campos utilizados pelo modelo.

Todos os campos são obrigatórios na estrutura JSON, mas aceitam valores `null`, pois são declarados como tipos opcionais com campo obrigatório (`Field(...)`).

### 7.1. Campos aceitos

| Campo | Tipo esperado | Restrições |
|---|---|---|
| `quantidade_itens` | Inteiro ou null | Valor mínimo 1. |
| `quantidade_produtos_distintos` | Inteiro ou null | Valor mínimo 1. |
| `quantidade_vendedores_distintos` | Inteiro ou null | Valor mínimo 1. |
| `quantidade_categorias_distintas` | Inteiro ou null | Valor mínimo 1. |
| `quantidade_estados_vendedores_distintos` | Inteiro ou null | Valor mínimo 1. |
| `quantidade_cidades_vendedores_distintas` | Inteiro ou null | Valor mínimo 1. |
| `valor_total_produtos` | Decimal ou null | Valor mínimo 0. |
| `frete_total` | Decimal ou null | Valor mínimo 0. |
| `product_weight_g_medio` | Decimal ou null | Valor mínimo 0. |
| `product_length_cm_medio` | Decimal ou null | Valor mínimo 0. |
| `product_height_cm_medio` | Decimal ou null | Valor mínimo 0. |
| `product_width_cm_medio` | Decimal ou null | Valor mínimo 0. |
| `ano_compra` | Inteiro ou null | Sem limite adicional definido no schema. |
| `mes_compra` | Inteiro ou null | Entre 1 e 12. |
| `dia_mes_compra` | Inteiro ou null | Entre 1 e 31. |
| `dia_semana_compra` | Inteiro ou null | Entre 0 e 6. |
| `hora_compra` | Inteiro ou null | Entre 0 e 23. |
| `customer_zip_code_prefix` | Inteiro ou null | Entre 0 e 99999. |
| `customer_city` | String ou null | Entre 1 e 100 caracteres, quando preenchida. |
| `customer_state` | String ou null | Duas letras maiúsculas. |
| `categoria_produto_mais_frequente` | String ou null | Entre 1 e 100 caracteres, quando preenchida. |
| `seller_state_mais_frequente` | String ou null | Duas letras maiúsculas. |
| `seller_city_mais_frequente` | String ou null | Entre 1 e 100 caracteres, quando preenchida. |
| `fim_de_semana_compra` | Booleano ou null | `true` ou `false`. |

### 7.2. Regras de validação

O schema `PredictionInput` utiliza:

- `strict=True`: impede coerções automáticas de tipos.
- `extra="forbid"`: rejeita campos não definidos no schema.
- `allow_inf_nan=False`: impede valores infinitos e NaN.
- `Field(...)`: exige a presença de todos os campos, mesmo quando o valor informado é `null`.

Essas regras garantem que a estrutura recebida pela API corresponda ao formato esperado pelo pipeline.

## 8. Dados de saída da API

O endpoint `POST /predict` retorna os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| `prediction_id` | Inteiro | Identificador do registro criado no histórico. |
| `prediction` | Inteiro | Classe prevista: 0 ou 1. |
| `prediction_label` | String | Descrição textual da classificação. |
| `delay_probability` | Decimal | Probabilidade estimada para a classe de atraso. |
| `message` | String | Mensagem explicativa do resultado. |

### 8.1. Classes previstas

| Valor | Rótulo |
|---|---|
| `0` | Sem atraso previsto |
| `1` | Atraso previsto |

A probabilidade `delay_probability` representa a estimativa do modelo para a classe `1`, variando de 0 a 1.

Ela não representa uma garantia de que o pedido será entregue com atraso.

## 9. Banco de dados — Histórico de previsões

Banco: `data/delivery_risk.db`

Tabela: `predictions`

O SQLite armazena os resultados das previsões realizadas pela API.

| Campo | Tipo SQLite | Restrições | Descrição |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do registro. |
| `prediction` | INTEGER | NOT NULL, CHECK (0 ou 1) | Classe prevista. |
| `prediction_label` | TEXT | NOT NULL | Descrição textual da classificação. |
| `delay_probability` | REAL | NOT NULL, CHECK entre 0 e 1 | Probabilidade estimada de atraso. |
| `input_data` | TEXT | NOT NULL | Dados de entrada armazenados em formato JSON. |
| `created_at` | TEXT | NOT NULL | Data e horário de criação do registro. |

### 9.1. Estrutura do campo `input_data`

O campo `input_data` armazena os atributos enviados à API para gerar a previsão, serializados em JSON.

Isso permite recuperar os dados utilizados em uma previsão específica e consultar o histórico com informações de entrada e saída.

### 9.2. Persistência

As operações de leitura, inserção e exclusão são realizadas pelo backend, por meio da camada Repository.

O frontend não acessa diretamente o banco SQLite.

## 10. Resumo das variáveis do modelo

| Grupo | Quantidade | Exemplos |
|---|---:|---|
| Numéricas | 17 | `valor_total_produtos`, `frete_total`, `hora_compra` |
| Categóricas e booleanas | 7 | `customer_city`, `customer_state`, `fim_de_semana_compra` |
| **Total** | **24** | Features utilizadas pelo modelo |

A variável-alvo `delivery_delayed` é independente das 24 features e representa o resultado que o modelo busca prever.

## 11. Considerações sobre os dados

- A unidade de análise do modelo é o pedido, e não o item individual.
- A base integrada preserva informações necessárias para auditoria e construção da variável-alvo.
- Pedidos sem datas suficientes para classificação permanecem com alvo ausente.
- As features são construídas com informações disponíveis no contexto da compra.
- Identificadores e informações posteriores à compra são excluídos do treinamento.
- Valores ausentes nas features são tratados pelo pipeline de pré-processamento.
- A codificação categórica permite lidar com categorias não observadas durante o treinamento.
- A probabilidade produzida pelo modelo deve ser interpretada como uma estimativa experimental.

Este dicionário documenta as variáveis e estruturas de dados utilizadas no DeliveryRisk AI, desde os arquivos originais até a entrada, o processamento, a previsão e o armazenamento dos resultados.