# DeliveryRisk AI

## Sobre o projeto

O **DeliveryRisk AI** é um projeto de Machine Learning que tem como objetivo desenvolver um sistema para prever o risco de atraso nas entregas de pedidos de e-commerce brasileiro.

O projeto utiliza o **Brazilian E-Commerce Public Dataset by Olist** para analisar dados históricos, preparar informações, treinar e avaliar modelos preditivos e, futuramente, disponibilizar as previsões por meio de uma API REST e de uma interface web.

O desenvolvimento está organizado em etapas, desde a análise exploratória e preparação dos dados até a avaliação dos modelos e a integração da solução com o backend e o frontend.

## Objetivo

Desenvolver uma solução de análise preditiva capaz de estimar o risco de um pedido ser entregue após a data prevista, utilizando informações disponíveis no momento da compra.

A solução deverá utilizar dados históricos para construir um modelo de classificação binária, disponibilizar previsões por meio de uma API e apresentar os resultados em uma interface interativa.

## Tecnologias

- **Python:** linguagem principal.
- **Pandas e NumPy:** manipulação e análise de dados.
- **Scikit-learn:** desenvolvimento e avaliação dos modelos de Machine Learning.
- **Matplotlib, Seaborn e Plotly:** visualização de dados.
- **Jupyter Notebook:** análise exploratória e experimentação.
- **FastAPI e Uvicorn:** desenvolvimento e execução da API.
- **Pydantic:** validação de dados.
- **Streamlit:** desenvolvimento da interface web.
- **SQLite:** armazenamento do histórico de previsões.
- **Pytest e HTTPX:** testes automatizados.
- **Joblib:** serialização de modelos treinados.
- **Python-dotenv:** gerenciamento de variáveis de ambiente.

As versões das dependências estão registradas em `requirements.txt`.

## Estrutura do projeto

```text
DeliveryRisk_AI/
├── backend/
│   ├── routers/
│   ├── services/
│   ├── database/
│   ├── repositories/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── dependencies.py
├── frontend/
│   ├── pages/
│   ├── components/
│   ├── utils/
│   ├── streamlit_app.py
│   ├── api_client.py
│   └── config.py
├── pipeline/
│   ├── src/
│   │   ├── carregamento.py
│   │   ├── analise_exploratoria.py
│   │   ├── tratamento.py
│   │   ├── integracao_dados.py
│   │   ├── feature_engineering.py
│   │   ├── preparacao_modelo.py
│   │   ├── modelos.py
│   │   ├── avaliacao.py
│   │   └── robustez.py
│   ├── notebooks/
│       └── delivery_risk_analysis.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── images/
│   ├── eda/
│   ├── matrizes_de_confusao/
│   └── avaliacao_modelos/
├── reports/
│   └── metrics/
├── tests/
├── docs/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

A estrutura foi organizada para separar as responsabilidades do projeto:

- `backend/`: componentes da futura API.
- `frontend/`: componentes da futura interface web.
- `pipeline/`: módulos, scripts e notebook destinados ao processamento e à modelagem.
- `data/raw/`: arquivos originais do conjunto de dados.
- `data/processed/`: espaço destinado aos dados processados.
- `models/`: espaço destinado aos modelos treinados.
- `images/`: organização das visualizações e dos gráficos.
- `reports/metrics/`: espaço destinado aos relatórios de métricas.
- `tests/`: testes automatizados.
- `docs/`: documentação técnica do projeto.

Os diretórios e arquivos representam a estrutura definida para o projeto. A presença de um arquivo não implica que sua implementação esteja concluída.

## Base de dados

O projeto utiliza o **Brazilian E-Commerce Public Dataset by Olist**, disponibilizado publicamente no Kaggle.

Fonte: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Os cinco arquivos CSV utilizados nas etapas de análise e preparação são:

| Arquivo | Descrição |
|---|---|
| `olist_orders_dataset.csv` | Informações dos pedidos e datas relacionadas ao processo de entrega. |
| `olist_order_items_dataset.csv` | Itens associados aos pedidos, incluindo produtos, vendedores, preços e fretes. |
| `olist_customers_dataset.csv` | Identificadores e informações geográficas dos clientes. |
| `olist_products_dataset.csv` | Informações cadastrais, categorias e características físicas dos produtos. |
| `olist_sellers_dataset.csv` | Identificadores e informações geográficas dos vendedores. |

Os arquivos originais são utilizados como fontes para a análise e as etapas posteriores de preparação dos dados. A disponibilidade dos arquivos no ambiente local deve ser verificada antes da execução do pipeline.

## Configuração do ambiente

O projeto utiliza um ambiente virtual Python chamado `.venv`, para manter as dependências isoladas do restante do sistema.

### 1. Criar o ambiente virtual

Caso ainda não exista:

```powershell
python -m venv .venv
```

### 2. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

Com o ambiente virtual ativado:

```powershell
python -m pip install -r requirements.txt
```

### 4. Verificar as dependências

Para verificar possíveis conflitos:

```powershell
python -m pip check
```

### 5. Configuração do Jupyter Notebook

O Jupyter e o `ipykernel` fazem parte das dependências do projeto. O ambiente virtual foi registrado como um kernel do Jupyter com o nome de exibição **Python (DeliveryRisk AI)**.

Para iniciar o Jupyter Notebook:

```powershell
jupyter notebook
```

No notebook `pipeline/notebooks/delivery_risk_analysis.ipynb`, selecione o kernel **Python (DeliveryRisk AI)** para utilizar o ambiente virtual do projeto.

## Fase 2 — Desenvolvimento do pipeline de Machine Learning

A Fase 2 foi planejada em sete etapas:

| Etapa | Descrição | Status |
|---|---|---|
| 2.1 | Carregamento, diagnóstico e análise exploratória dos dados (EDA). | Concluída |
| 2.2 | Tratamento e integração dos dados, com construção da variável-alvo. | Concluída |
| 2.3 | Pré-processamento e engenharia de atributos. | Concluída |
| 2.4 | Divisão dos dados em treino, validação e teste. | Concluída |
| 2.5 | Treinamento e ajuste dos modelos. | Concluída |
| 2.6 | Avaliação comparativa e análise do custo computacional. | Concluída |
| 2.7 | Análise de robustez, generalização e serialização do modelo final. | Pendente |

### Etapa 2.1 — Carregamento, diagnóstico e análise exploratória dos dados (EDA)

**Status: concluída.**

As análises foram documentadas no notebook `pipeline/notebooks/delivery_risk_analysis.ipynb`.

Foram carregados e examinados os cinco datasets do projeto, com foco na compreensão da estrutura, qualidade e distribuição dos dados.

As atividades realizadas foram:

- Carregamento dos datasets.
- Análise das dimensões e dos tipos de dados.
- Diagnóstico de valores ausentes.
- Verificação de registros integralmente duplicados.
- Análise de chaves e identificadores.
- Análise das distribuições das variáveis numéricas.
- Análise das distribuições das variáveis categóricas.
- Geração e interpretação de matrizes de correlação de Pearson.

#### Resumo do diagnóstico

| Dataset | Registros | Colunas | Valores ausentes | Registros integralmente duplicados |
|---|---:|---:|---:|---:|
| `orders` | 99.441 | 8 | 4.908 | 0 |
| `order_items` | 112.650 | 7 | 0 | 0 |
| `customers` | 99.441 | 5 | 0 | 0 |
| `products` | 32.951 | 9 | 2.448 | 0 |
| `sellers` | 3.095 | 4 | 0 | 0 |
| **Total** | **347.578** | — | **7.356** | **0** |

O total de registros corresponde à soma das linhas dos cinco datasets, que possuem diferentes granularidades. O total de valores ausentes corresponde à soma das células ausentes, e não à quantidade de registros afetados.

#### Principais observações

**Valores ausentes**

- Em `orders`, as ausências concentram-se nas datas de aprovação e nas etapas de entrega.
- Em `products`, foram identificados 611 produtos com pelo menos um campo ausente.
- A análise por status em `orders` demonstrou que os padrões de ausência variam conforme a situação do pedido.

**Duplicatas e chaves**

- Não foram encontrados registros integralmente duplicados nos cinco datasets.
- `order_id` é único em `orders`.
- A combinação `order_id` + `order_item_id` não apresentou duplicatas em `order_items`.
- A repetição de `order_id` em `order_items` é compatível com a existência de vários itens por pedido.

**Distribuições numéricas e categóricas**

- As variáveis `price` e `freight_value` de `order_items` apresentam distribuições assimétricas à direita.
- A categoria `delivered` predomina em `orders`.
- Os registros de clientes e vendedores apresentam concentração em determinadas cidades e estados.
- Os produtos apresentam diferentes frequências entre as categorias cadastradas.
- Algumas colunas inicialmente classificadas como categóricas representam identificadores ou datas armazenadas como texto.

**Correlações**

- Em `order_items`, foi observada correlação positiva moderada entre `price` e `freight_value` (0,41).
- Em `products`, o peso apresentou correlações positivas com altura (0,56), largura (0,53) e comprimento (0,48).

As correlações são descritivas e não demonstram causalidade.

#### Resultado da etapa

A EDA permitiu documentar as características estruturais dos datasets, os padrões de valores ausentes, as propriedades das distribuições e as associações lineares observadas.

Os resultados serviram de referência para o tratamento, a integração dos dados e a construção da variável-alvo.

### Etapa 2.2 — Tratamento e integração dos dados

**Status: concluída.**

A etapa teve como objetivo preparar, validar e integrar os datasets para construir uma base consolidada, com uma linha por pedido, e criar a variável-alvo utilizada na previsão de atrasos nas entregas.

#### Tratamento inicial e validação

Os cinco datasets — `orders`, `order_items`, `customers`, `products` e `sellers` — foram copiados para a estrutura `datasets_trabalho`, preservando os dados originais carregados.

As atividades realizadas foram:

- Conversão das colunas de data selecionadas para o tipo `datetime64[us]`.
- Normalização dos textos, com remoção de espaços nas extremidades e conversão de textos vazios em valores ausentes.
- Validação das chaves dos cinco datasets, incluindo a chave composta de `order_items`.
- Verificação de valores ausentes, não numéricos e infinitos nas colunas numéricas selecionadas.
- Validação das correspondências entre os identificadores dos datasets relacionados.

Não foram identificadas datas inválidas nas colunas verificadas, chaves inválidas ou referências sem correspondência nas relações analisadas. Os valores ausentes existentes foram preservados para avaliação nas etapas posteriores.

#### Agregação e integração

Os 112.650 registros de `order_items` foram agregados por `order_id`, resultando em 98.666 pedidos com itens.

A agregação reuniu informações sobre quantidades de itens e produtos, valores de produtos e frete, categorias, características físicas dos produtos e informações geográficas dos vendedores.

Em seguida, os dados agregados foram integrados às informações de `orders` e `customers`, preservando a granularidade de um registro por pedido.

A base integrada apresentou os seguintes resultados:

| Indicador | Resultado |
|---|---:|
| Total de pedidos | 99.441 |
| Total de colunas | 29 |
| IDs de pedido distintos | 99.441 |
| IDs de pedido ausentes | 0 |
| Linhas pertencentes a pedidos duplicados | 0 |
| Pedidos sem itens | 775 |

A validação confirmou que a quantidade de registros corresponde à quantidade esperada de pedidos e que a base integrada mantém uma linha por pedido.

#### Criação e validação da variável-alvo

Foi criada a variável `delivery_delayed` para classificar o resultado da entrega:

- `1`: entrega realizada após a data estimada.
- `0`: entrega realizada na data estimada ou antes dela.
- Valor ausente: ausência de informações suficientes para determinar a classificação.

A distribuição obtida foi:

| Indicador | Quantidade |
|---|---:|
| Total de pedidos | 99.441 |
| Entregas atrasadas | 7.827 |
| Entregas no prazo | 88.649 |
| Pedidos sem classificação | 2.965 |
| Pedidos com classificação válida | 96.476 |

Entre os pedidos com classificação válida, aproximadamente 8,11% apresentaram atraso.

Uma verificação independente da regra de classificação foi realizada nos 96.476 pedidos que possuíam as duas datas necessárias. Não foram encontradas divergências entre a regra definida e os valores calculados.

Os 2.965 pedidos sem classificação foram mantidos com a variável-alvo ausente, sem atribuição artificial de rótulos.

#### Investigação dos pedidos sem itens

Foram identificados 775 pedidos sem registros correspondentes em `order_items`.

Esses pedidos apresentaram valores ausentes nas 15 colunas derivadas da agregação. Também foi verificado que nenhum desses pedidos possuía a variável-alvo preenchida.

Os registros foram mantidos na base integrada, e as ausências foram documentadas para orientar as decisões posteriores de preparação dos dados.

#### Salvamento da base integrada

A base resultante foi salva no formato Parquet em:

`data/processed/base_integrada.parquet`

O arquivo permite reutilizar os dados integrados nas próximas etapas sem repetir as operações de agregação e integração, desde que os dados de origem e as regras de processamento permaneçam inalterados.

#### Resultado da etapa

A Etapa 2.2 foi concluída com a preparação e validação dos datasets, a agregação dos itens por pedido, a integração das informações, a criação e validação da variável-alvo e o salvamento da base consolidada.

A base integrada contém 99.441 registros e 29 colunas, mantém uma linha por pedido e não apresenta IDs de pedido ausentes ou duplicados. Os valores ausentes relevantes foram preservados e documentados para orientar as próximas decisões do pipeline.

### Etapa 2.3 — Pré-processamento e engenharia de atributos

**Status: concluída.**

A etapa teve como objetivo preparar as variáveis preditoras para a futura modelagem, criar atributos relevantes a partir do momento da compra e configurar um pipeline de pré-processamento que reduza inconsistências e evite vazamento de informações.

#### Elegibilidade e atributos temporais

A base foi filtrada para manter os pedidos elegíveis, isto é, aqueles que possuem uma classificação válida em `delivery_delayed`. A base elegível contém 96.476 pedidos e 29 colunas antes da engenharia de atributos.

A partir de `order_purchase_timestamp`, foram criados seis atributos temporais:

- `ano_compra`: ano em que o pedido foi realizado.
- `mes_compra`: mês da compra.
- `dia_mes_compra`: dia do mês da compra.
- `dia_semana_compra`: dia da semana da compra.
- `hora_compra`: hora da compra.
- `fim_de_semana_compra`: indicador de compra realizada no fim de semana.

A validação confirmou que não havia datas de compra ausentes ou inválidas na base elegível e que os seis atributos temporais criados não continham valores ausentes. O timestamp original foi removido das variáveis preditoras após a criação dos atributos derivados.

#### Seleção e validação das variáveis preditoras

Foram selecionadas 24 variáveis preditoras, divididas em 17 numéricas e 7 categóricas.

As variáveis abrangem informações geográficas do cliente, características agregadas dos itens e vendedores do pedido, valores e quantidades, categoria predominante dos produtos e atributos temporais da compra.

A seleção exclui identificadores, a variável-alvo e colunas auxiliares de elegibilidade, além de informações que não estariam disponíveis no momento da compra. Entre as colunas excluídas estão as datas de entrega, `order_status`, `order_approved_at` e `order_estimated_delivery_date`. A data estimada de entrega foi mantida fora das variáveis preditoras para respeitar a definição do cenário de previsão.

O prefixo do CEP do cliente, `customer_zip_code_prefix`, foi classificado explicitamente como categórico, evitando que seu valor numérico seja interpretado como uma medida contínua.

As validações confirmaram que todas as 24 variáveis foram classificadas, sem sobreposição entre os grupos numérico e categórico, e que a seleção não continha colunas proibidas.

#### Diagnóstico dos valores ausentes

A análise dos valores ausentes em `X` identificou:

- `categoria_produto_mais_frequente`: 1.332 valores ausentes, aproximadamente 1,38% dos pedidos elegíveis.
- `product_weight_g_medio`, `product_length_cm_medio`, `product_height_cm_medio` e `product_width_cm_medio`: 16 valores ausentes em cada variável, aproximadamente 0,02%.

A investigação das dimensões físicas mostrou que os 16 pedidos correspondem a 18 itens associados a dois produtos com informações físicas incompletas no dataset `products`. As correspondências entre os itens e os produtos foram encontradas, indicando que as ausências decorrem dos dados cadastrais dos produtos, e não de uma falha na integração.

Os registros não foram excluídos nem receberam valores preenchidos manualmente nesta etapa. O tratamento foi delegado ao pipeline de pré-processamento.

#### Configuração do pipeline de pré-processamento

Foi implementado e inspecionado um `ColumnTransformer` para aplicar transformações adequadas a cada tipo de variável.

| Tipo de variável | Estratégia de valores ausentes | Transformação |
|---|---|---|
| Numéricas | Imputação pela mediana (`SimpleImputer`) | Padronização (`StandardScaler`) |
| Categóricas | Imputação pela categoria mais frequente (`SimpleImputer`) | Codificação One-Hot Encoding, com `handle_unknown="ignore"` |

O pipeline foi configurado, mas seus transformadores não foram ajustados sobre a base completa. O ajuste será realizado após a divisão dos dados, exclusivamente com o conjunto de treinamento, evitando que informações dos conjuntos de validação e teste influenciem o pré-processamento.

#### Resultado da etapa

A Etapa 2.3 foi concluída com a seleção e validação de 24 variáveis preditoras, a criação de seis atributos temporais, a análise dos valores ausentes e a configuração do pipeline de pré-processamento.

A base elegível contém 96.476 pedidos, com as variáveis preditoras definidas e as estratégias de transformação especificadas. Esses dados estão preparados para a divisão temporal, sem que o pipeline tenha sido ajustado sobre os dados completos.

### Etapa 2.4 — Divisão temporal entre treino, validação e teste

**Status: concluída.**

A etapa teve como objetivo separar os dados elegíveis em conjuntos de treino, validação e teste, respeitando a ordem cronológica das compras. Essa estratégia permite avaliar futuramente o modelo em períodos posteriores aos utilizados no treinamento, aproximando a avaliação do cenário de utilização real.

#### Estratégia de divisão temporal

A divisão foi realizada com base na coluna `order_purchase_timestamp`, utilizando os seguintes intervalos:

| Conjunto | Período das compras | Regra aplicada |
|---|---|---|
| Treino | Até 28/02/2018 | Data anterior a `2018-03-01` |
| Validação | Março a maio de 2018 | Data a partir de `2018-03-01` e anterior a `2018-06-01` |
| Teste | Junho a agosto de 2018 | Data a partir de `2018-06-01` e anterior a `2018-09-01` |

Os limites foram definidos para manter o conjunto de treino no período mais antigo, utilizar o período seguinte para validação e reservar o período mais recente para teste.

#### Resultados da divisão

A divisão foi aplicada aos 96.476 pedidos elegíveis, mantendo as 24 variáveis preditoras selecionadas na Etapa 2.3.

| Conjunto | Quantidade de pedidos | Pedidos atrasados | Pedidos no prazo | Taxa de atraso |
|---|---:|---:|---:|---:|
| Treino | 57.323 | 4.395 | 52.928 | 7,67% |
| Validação | 20.550 | 2.413 | 18.137 | 11,74% |
| Teste | 18.603 | 1.019 | 17.584 | 5,48% |
| **Total** | **96.476** | **7.827** | **88.649** | **8,11%** |

A distribuição da variável-alvo varia entre os períodos. A taxa de atraso foi de 7,67% no treino, 11,74% na validação e 5,48% no teste. Essas diferenças foram registradas para contextualizar a avaliação futura dos modelos.

#### Validações realizadas

Foi implementado o módulo `pipeline/src/preparacao_modelo.py`, contendo funções para realizar a divisão temporal, resumir os conjuntos e validar os resultados.

As verificações executadas confirmaram:

- Unicidade dos índices de `X`, `y` e da base elegível.
- Alinhamento entre as features e a variável-alvo em cada conjunto.
- Ausência de sobreposição de índices entre treino, validação e teste.
- Preservação dos 96.476 registros elegíveis após a divisão.
- Cumprimento dos intervalos temporais definidos.
- Ordem cronológica entre os conjuntos.
- Consistência das 24 features nos três conjuntos.

Todas as validações executadas foram concluídas com sucesso.

#### Pré-processamento e prevenção de vazamento de dados

O pipeline de pré-processamento configurado na Etapa 2.3 permaneceu sem ajuste durante esta etapa. Não foram executados `fit()` ou `fit_transform()` antes da divisão temporal.

Nas etapas posteriores, o ajuste dos transformadores deverá utilizar exclusivamente `X_train`. Os conjuntos de validação e teste deverão receber as transformações aprendidas no treino, sem reajuste do pipeline com seus próprios dados.

Essa separação evita que estatísticas de imputação, parâmetros de padronização ou categorias aprendidas durante o pré-processamento sejam influenciados pelos conjuntos destinados à avaliação.

#### Resultado da etapa

A Etapa 2.4 foi concluída com a implementação e validação da divisão temporal dos dados. Os conjuntos `X_train`, `y_train`, `X_val`, `y_val`, `X_test` e `y_test` estão preparados para serem utilizados nas etapas posteriores.

Não foram realizados treinamento de modelos, ajuste de hiperparâmetros ou avaliação de desempenho nesta etapa. Essas atividades foram desenvolvidas na Etapa 2.5.

### Etapa 2.5 — Treinamento e ajuste dos modelos

**Status: concluída.**

A etapa teve como objetivo implementar, treinar e comparar diferentes configurações de algoritmos de classificação para identificar pedidos com risco de atraso nas entregas. A avaliação foi realizada com o conjunto de validação, preservando o conjunto de teste para as etapas posteriores.

Foram implementadas funções auxiliares no módulo `pipeline/src/modelos.py` para organizar a criação dos modelos, a construção dos pipelines de pré-processamento, o treinamento, a geração de previsões e o registro dos resultados.

#### Preparação dos modelos

A modelagem utilizou as 24 variáveis preditoras definidas na Etapa 2.3, sendo:

| Tipo de variável | Quantidade |
|---|---:|
| Numéricas | 17 |
| Categóricas | 7 |
| **Total** | **24** |

O pré-processamento foi integrado aos pipelines dos modelos, com estratégias de imputação, codificação de variáveis categóricas e padronização das variáveis numéricas quando aplicável.

Para a Regressão Logística e o Random Forest, foram avaliadas configurações com e sem ponderação de classes, por meio do parâmetro `class_weight`. Para o Gradient Boosting, foram testadas combinações de quantidade de árvores e taxa de aprendizado.

#### Experimentos realizados

Foram executados 18 experimentos, distribuídos igualmente entre os três algoritmos.

| Algoritmo | Quantidade de configurações | Hiperparâmetros avaliados |
|---|---:|---|
| Regressão Logística | 6 | `C`, `class_weight` |
| Random Forest | 6 | `n_estimators`, `max_depth`, `class_weight` |
| Gradient Boosting | 6 | `n_estimators`, `learning_rate` |
| **Total** | **18** | — |

As configurações foram comparadas utilizando acurácia, precisão, recall, F1-score e ROC-AUC. Também foram registrados os tempos de treinamento e predição.

#### Resultados da Regressão Logística

A Regressão Logística apresentou variação de desempenho conforme a regularização e a ponderação de classes utilizadas.

O maior recall foi de **80,02%**, obtido com `C=0.01` e `class_weight="balanced"`. Essa configuração apresentou precisão de 12,92% e F1-score de 0,2225, demonstrando elevada capacidade de identificar pedidos atrasados, mas também uma quantidade significativa de falsos positivos.

O maior F1-score do algoritmo foi de **0,2357**, obtido com `C=1.0` e `class_weight="balanced"`. O maior ROC-AUC foi de 0,6038, observado com `C=0.1` e `class_weight="balanced"`.

Os experimentos demonstraram que a ponderação de classes aumentou o recall em relação às configurações sem ponderação, embora tenha reduzido a acurácia. As configurações sem ponderação apresentaram acurácias elevadas, mas tiveram dificuldade para identificar a classe minoritária.

#### Resultados do Random Forest

O Random Forest apresentou os melhores resultados gerais entre os três algoritmos avaliados.

A melhor configuração foi obtida no Experimento 4, com os seguintes hiperparâmetros:

```python
{
    "n_estimators": 100,
    "max_depth": 10,
    "class_weight": "balanced"
}
```

Os resultados no conjunto de validação foram:

| Métrica | Resultado |
|---|---:|
| Acurácia | 68,10% |
| Precisão | 18,85% |
| Recall | 51,93% |
| F1-score | 0,2766 |
| ROC-AUC | 0,6527 |
| Tempo de treinamento | 5,13 s |
| Tempo de predição | 1,15 s |

Essa configuração apresentou o maior F1-score e o maior ROC-AUC entre os 18 experimentos.

Outra configuração, com `n_estimators=200`, `max_depth=5` e `class_weight="balanced"`, apresentou o maior recall do Random Forest, de 60,75%, mas obteve F1-score de 0,2722. Assim, a configuração com 100 árvores e profundidade máxima 10 apresentou o melhor F1-score e a melhor capacidade de discriminação entre as classes, enquanto a configuração com 200 árvores e profundidade máxima 5 identificou uma proporção maior dos pedidos atrasados.

As configurações sem ponderação de classes apresentaram acurácia de aproximadamente 88,26%, mas precisão, recall e F1-score iguais a zero. Esse resultado reforçou a importância de avaliar as métricas específicas da classe minoritária.

#### Resultados do Gradient Boosting

O Gradient Boosting apresentou baixo desempenho na identificação dos pedidos atrasados, apesar de algumas configurações terem alcançado acurácia próxima de 88,26%.

A melhor configuração do algoritmo foi obtida com `n_estimators=200` e `learning_rate=0.1`, apresentando:

| Métrica | Resultado |
|---|---:|
| Acurácia | 87,62% |
| Precisão | 17,73% |
| Recall | 1,49% |
| F1-score | 0,0275 |
| ROC-AUC | 0,6080 |
| Tempo de treinamento | 185,88 s |
| Tempo de predição | 1,38 s |

Embora essa configuração tenha apresentado o maior F1-score e ROC-AUC do Gradient Boosting, o recall permaneceu muito baixo. O tempo de treinamento também foi significativamente superior ao dos outros algoritmos.

O aumento da quantidade de árvores elevou o custo computacional sem produzir uma melhoria suficiente na identificação dos pedidos atrasados.

#### Comparação geral dos melhores resultados

A tabela apresenta a melhor configuração de cada algoritmo segundo o F1-score obtido no conjunto de validação.

| Algoritmo | Melhor configuração | Precisão | Recall | F1-score | ROC-AUC | Treinamento |
|---|---|---:|---:|---:|---:|---:|
| Regressão Logística | `C=1.0`, `class_weight="balanced"` | 15,19% | 52,55% | 0,2357 | 0,5902 | 6,34 s |
| Random Forest | `n_estimators=100`, `max_depth=10`, `class_weight="balanced"` | 18,85% | 51,93% | 0,2766 | 0,6527 | 5,13 s |
| Gradient Boosting | `n_estimators=200`, `learning_rate=0.1` | 17,73% | 1,49% | 0,0275 | 0,6080 | 185,88 s |

A comparação demonstrou que o Random Forest apresentou o melhor equilíbrio entre precisão e recall segundo o F1-score, além do maior ROC-AUC. A Regressão Logística permaneceu como referência útil, especialmente por apresentar configurações com recall elevado. O Gradient Boosting teve desempenho inferior na identificação da classe minoritária e maior custo de treinamento.

A acurácia não foi utilizada como único critério de seleção devido ao desequilíbrio entre as classes.

#### Análise do limiar de classificação

Após a seleção do Random Forest como principal candidato, foi avaliado o impacto de diferentes limiares sobre a classificação dos pedidos como atrasados. A análise utilizou as probabilidades previstas no conjunto de validação.

Os principais resultados foram:

| Limiar | Precisão | Recall | F1-score | Pedidos classificados como atrasados |
|---:|---:|---:|---:|---:|
| 0,50 | 18,85% | 51,93% | 0,2766 | 6.648 |
| 0,45 | 11,94% | 99,38% | 0,2132 | 20.081 |
| 0,40 | 11,74% | 100,00% | 0,2102 | 20.546 |
| 0,10 a 0,35 | 11,74% | 100,00% | 0,2102 | 20.550 |
| 0,55 | 25,56% | 0,95% | 0,0184 | 90 |
| 0,60 a 0,80 | 0,00% | 0,00% | 0,0000 | 0 |

Entre os limiares testados, **0,50 apresentou o maior F1-score**. A redução do limiar aumentou o recall, mas também elevou consideravelmente a quantidade de pedidos classificados como atrasados, reduzindo a precisão.

O limiar de 0,50 foi mantido como referência inicial. A definição do limiar definitivo dependerá da análise dos custos dos falsos positivos e falsos negativos na Etapa 2.6.

#### Resultado da etapa

A Etapa 2.5 foi concluída com o treinamento e a comparação de 18 configurações de modelos, utilizando o conjunto de validação para orientar a seleção do principal candidato.

O Random Forest com `n_estimators=100`, `max_depth=10` e `class_weight="balanced"` foi selecionado para as avaliações posteriores, por apresentar F1-score de 0,2766 e ROC-AUC de 0,6527, os melhores resultados dessas métricas entre os experimentos realizados.

A seleção ainda é preliminar. O conjunto de teste permanece reservado para a avaliação final, e a definição do limiar de classificação deverá considerar os custos dos erros e os objetivos de negócio.

### Etapa 2.6 — Avaliação comparativa dos modelos

**Status: concluída.**

A etapa teve como objetivo consolidar e comparar os resultados dos experimentos realizados na Etapa 2.5, identificando o modelo candidato mais adequado para a previsão de atrasos nas entregas.

A avaliação considerou métricas preditivas, matrizes de confusão, análise dos erros de classificação, desempenho computacional, tamanho dos modelos e consumo de memória.

Todas as análises foram realizadas utilizando o conjunto de validação. O conjunto de teste permaneceu reservado para a avaliação final da Etapa 2.7.

#### Consolidação dos experimentos

Foram consolidados os resultados dos 18 experimentos realizados anteriormente:

- 6 experimentos de Regressão Logística.
- 6 experimentos de Random Forest.
- 6 experimentos de Gradient Boosting.

O F1-score foi utilizado como principal critério de comparação, por combinar Precision e Recall e ser adequado à avaliação de problemas com classes desbalanceadas.

#### Comparação dos melhores experimentos

Foi identificado o melhor experimento de cada algoritmo com base no F1-score obtido na validação.

| Algoritmo | Experimento | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Random Forest | 4 | 68,10% | 18,85% | 51,93% | 0,2766 | 0,6527 |
| Logistic Regression | 5 | 59,99% | 15,19% | 52,55% | 0,2357 | 0,5902 |
| Gradient Boosting | 6 | 87,62% | 17,73% | 1,49% | 0,0275 | 0,6080 |

O Random Forest apresentou o maior F1-score e ROC-AUC entre os três melhores experimentos.

A Regressão Logística apresentou Recall ligeiramente superior, enquanto o Gradient Boosting demonstrou dificuldade para identificar os pedidos atrasados, apesar de sua elevada acurácia.

#### Matrizes de confusão

Foram geradas matrizes de confusão para os melhores experimentos de cada algoritmo, utilizando as previsões sobre o conjunto de validação.

| Modelo | Verdadeiros negativos | Falsos positivos | Falsos negativos | Verdadeiros positivos |
|---|---:|---:|---:|---:|
| Random Forest — Exp. 4 | 12.742 | 5.395 | 1.160 | 1.253 |
| Logistic Regression — Exp. 5 | 11.060 | 7.077 | 1.145 | 1.268 |
| Gradient Boosting — Exp. 6 | 17.970 | 167 | 2.377 | 36 |

As matrizes foram salvas no diretório `images/matrizes_de_confusao/`.

O Random Forest identificou 1.253 pedidos atrasados, mas também apresentou 5.395 falsos positivos. A Regressão Logística identificou 1.268 pedidos atrasados, com 7.077 falsos positivos.

O Gradient Boosting apresentou poucos falsos positivos, mas deixou de identificar 2.377 pedidos que realmente atrasaram.

#### Análise de falsos positivos e falsos negativos

A análise dos erros permitiu observar o comportamento dos modelos diante dos dois tipos de classificação incorreta:

- **Falso positivo:** pedido classificado como atrasado que não apresentou atraso.
- **Falso negativo:** pedido que apresentou atraso, mas não foi identificado pelo modelo.

O Random Forest apresentou um equilíbrio entre os dois tipos de erro em comparação aos demais algoritmos.

A Regressão Logística apresentou quantidade próxima de falsos negativos, mas maior quantidade de falsos positivos.

O Gradient Boosting apresentou a menor quantidade de falsos positivos, porém o maior número de falsos negativos.

Como não foram definidos pesos financeiros ou operacionais para cada tipo de erro, a análise foi realizada considerando suas quantidades, sem atribuição de custos monetários.

#### Desempenho computacional

O desempenho computacional foi avaliado considerando os 20.550 pedidos do conjunto de validação.

Foram comparados o tempo de treinamento, o tempo de predição, a latência média por pedido e a quantidade aproximada de pedidos processados por segundo.

| Modelo | Treinamento (s) | Predição (s) | Latência (ms/pedido) | Pedidos/s |
|---|---:|---:|---:|---:|
| Random Forest — Exp. 4 | 4,22 | 1,04 | 0,0507 | 19.738 |
| Logistic Regression — Exp. 5 | 8,51 | 0,83 | 0,0406 | 24.615 |
| Gradient Boosting — Exp. 6 | 176,75 | 1,87 | 0,0910 | 10.993 |

A Regressão Logística apresentou a menor latência e a maior vazão aproximada.

O Random Forest apresentou o menor tempo de treinamento entre os três modelos, com desempenho de predição próximo ao da Regressão Logística.

O Gradient Boosting apresentou o maior tempo de treinamento e predição, além da menor vazão.

#### Tamanho dos modelos

O tamanho dos pipelines treinados foi medido por meio da serialização temporária em formato Joblib.

| Modelo | Tamanho |
|---|---:|
| Random Forest — Exp. 4 | 1,5548 MB |
| Logistic Regression — Exp. 5 | 0,2396 MB |
| Gradient Boosting — Exp. 6 | 0,6256 MB |

A Regressão Logística apresentou o menor tamanho, enquanto o Random Forest apresentou o maior. Todos os modelos permaneceram abaixo de 2 MB.

#### Consumo de memória

O pico de memória foi medido durante a execução da predição sobre o conjunto de validação, utilizando `tracemalloc`.

| Modelo | Pico de memória rastreada |
|---|---:|
| Random Forest — Exp. 4 | 17,7755 MB |
| Logistic Regression — Exp. 5 | 17,7705 MB |
| Gradient Boosting — Exp. 6 | 27,9407 MB |

O Random Forest e a Regressão Logística apresentaram consumo praticamente igual. O Gradient Boosting apresentou o maior pico de memória.

Essa medição representa a memória rastreada pelo `tracemalloc`, não necessariamente o consumo total de RAM do processo, pois algumas alocações internas de bibliotecas nativas podem não ser contabilizadas.

#### Seleção do modelo candidato

A seleção foi realizada considerando o F1-score dos 18 experimentos, sem estabelecer um limite mínimo de Recall.

O modelo selecionado foi:

**Random Forest — Experimento 4**

Hiperparâmetros:

```python
{
    "n_estimators": 100,
    "max_depth": 10,
    "class_weight": "balanced"
}
```

Resultados na validação:

| Métrica | Resultado |
|---|---:|
| Accuracy | 68,10% |
| Precision | 18,85% |
| Recall | 51,93% |
| F1-score | 0,2766 |
| ROC-AUC | 0,6527 |

O Random Forest foi selecionado por apresentar o maior F1-score entre os 18 experimentos, além do maior ROC-AUC entre os melhores experimentos dos três algoritmos.

Apesar da seleção, o modelo ainda apresenta limitações: sua Precision foi de 18,85%, seu Recall foi de 51,93% e foram registrados 5.395 falsos positivos e 1.160 falsos negativos na validação.

Portanto, a escolha representa uma seleção preliminar para a avaliação final, não uma aprovação para produção.

#### Salvamento dos resultados

Os resultados da avaliação foram salvos em `reports/metrics/`:

| Arquivo | Descrição |
|---|---|
| `comparacao_experimentos.csv` | Resultados dos 18 experimentos. |
| `melhores_modelos.csv` | Melhores experimentos de cada algoritmo. |
| `desempenho_computacional.csv` | Tempos, latência e vazão dos experimentos. |

As matrizes de confusão foram armazenadas separadamente em `images/matrizes_de_confusao/`.

#### Resultado da etapa

A Etapa 2.6 foi concluída com a comparação dos 18 experimentos, análise dos erros de classificação, avaliação do desempenho computacional e seleção do Random Forest — Experimento 4 como modelo candidato.

O modelo apresentou F1-score de 0,2766 e ROC-AUC de 0,6527 na validação, além de desempenho computacional e tamanho adequados para prosseguir com a avaliação.

O conjunto de teste não foi utilizado nesta etapa, permanecendo reservado para a avaliação final na Etapa 2.7.

## Variável-alvo

A variável-alvo `delivery_delayed` identifica se um pedido foi entregue após a data estimada:

- `1`: pedido entregue depois da data estimada.
- `0`: pedido entregue na data estimada ou antes dela.
- Valor ausente: pedido sem informações suficientes para determinar a classificação.

A variável foi construída na Etapa 2.2 utilizando as datas efetiva e estimada de entrega e passou por uma verificação independente, sem divergências nos registros elegíveis.

A base integrada contém 96.476 pedidos com classificação válida e 2.965 pedidos sem classificação.

Para prevenir vazamento de dados, o modelo deverá utilizar atributos compatíveis com uma previsão realizada no momento da compra. Informações que só ficam disponíveis depois da compra não deverão ser utilizadas como preditores.

Os pedidos sem classificação foram excluídos da base elegível utilizada na preparação para modelagem, conforme os critérios definidos no projeto.

## Controle de versão

O projeto utiliza Git para controle de versão e organização do desenvolvimento por branches.

Branches planejadas ou definidas:

- `main`
- `develop`
- `feature/Estrutura_do_projeto`
- `feature/Preparacao_de_dados`
- `feature/Ml-pipeline`
- `feature/Backend`
- `feature/Frontend`
- `Feature/Documentacao`

As mensagens de commit seguem a convenção Conventional Commits, com tipos como `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `style` e `perf`.

A branch ativa e o estado atual do repositório devem ser verificados antes de realizar operações Git.

## Status atual

### Fase 1 — Estruturação inicial

- [x] Criação da estrutura inicial de diretórios e arquivos.
- [x] Configuração do ambiente virtual Python.
- [x] Definição e registro das dependências em `requirements.txt`.
- [x] Configuração do kernel do Jupyter Notebook.
- [x] Configuração inicial do `.gitignore`.
- [x] Documentação inicial do projeto no `README.md`.

### Fase 2 — Pipeline de Machine Learning

- [x] **Etapa 2.1:** carregamento, diagnóstico e análise exploratória dos dados.
- [x] **Etapa 2.2:** tratamento e integração dos dados, com construção da variável-alvo.
- [x] **Etapa 2.3:** pré-processamento e engenharia de atributos.
- [x] **Etapa 2.4:** divisão dos dados em treino, validação e teste.
- [x] **Etapa 2.5:** treinamento e ajuste dos modelos.
- [x] **Etapa 2.6:** avaliação comparativa e análise do custo computacional.
- [ ] **Etapa 2.7:** análise de robustez, generalização e serialização do modelo final.

### Desenvolvimento da aplicação

- [ ] Desenvolver a API com FastAPI.
- [ ] Desenvolver a interface com Streamlit.
- [ ] Implementar o armazenamento do histórico de previsões.
- [ ] Criar e executar os testes automatizados.
- [ ] Completar a documentação técnica.

## Próximas etapas

## Próximas etapas

A próxima atividade é a **Etapa 2.7 — Análise de robustez, generalização e serialização do modelo final**.

Essa etapa deverá contemplar:

1. Avaliar o modelo candidato no conjunto de teste, que permaneceu reservado durante as etapas anteriores.
2. Analisar sua capacidade de generalização em dados de um período posterior ao treinamento e à validação.
3. Comparar os resultados finais com os resultados obtidos na validação.
4. Investigar a estabilidade do modelo e possíveis limitações de desempenho.
5. Confirmar a configuração final do modelo e o limiar de classificação, conforme os critérios definidos.
6. Serializar o modelo final para utilização nas etapas de integração.

Após a conclusão da Fase 2, o desenvolvimento deverá avançar para a integração do modelo com a API REST utilizando FastAPI, a interface web com Streamlit, o armazenamento do histórico de previsões e os testes automatizados.

## Licença

A licença do projeto será definida posteriormente.
