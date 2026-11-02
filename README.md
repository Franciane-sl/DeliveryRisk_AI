# DeliveryRisk AI

## Sobre o projeto

O **DeliveryRisk AI** é um projeto de Machine Learning que tem como objetivo desenvolver um sistema para prever o risco de atraso nas entregas de pedidos de e-commerce brasileiro.

O projeto utiliza o **Brazilian E-Commerce Public Dataset by Olist** para analisar dados históricos, preparar informações, treinar e avaliar modelos preditivos e disponibilizar previsões por meio de uma API REST.

A solução está sendo desenvolvida em etapas, desde a análise exploratória e preparação dos dados até a modelagem, avaliação, integração com o backend e desenvolvimento da interface web.

## Objetivo

Desenvolver uma solução de análise preditiva capaz de estimar o risco de um pedido ser entregue após a data prevista, utilizando informações disponíveis no momento da compra.

A solução utiliza dados históricos para construir um modelo de classificação binária, disponibilizar previsões por meio de uma API e, posteriormente, apresentar os resultados em uma interface interativa.

## Tecnologias

- **Python:** linguagem principal.
- **Pandas e NumPy:** manipulação e análise de dados.
- **Scikit-learn:** desenvolvimento e avaliação dos modelos de Machine Learning.
- **Matplotlib, Seaborn e Plotly:** visualização de dados.
- **Jupyter Notebook:** análise exploratória e experimentação.
- **FastAPI e Uvicorn:** desenvolvimento e execução da API REST.
- **Pydantic:** validação e estruturação dos dados.
- **Streamlit:** tecnologia planejada para o desenvolvimento da interface web.
- **SQLite:** armazenamento do histórico de previsões.
- **Pytest:** execução dos testes automatizados.
- **HTTPX e HTTPX2:** suporte a testes e requisições HTTP.
- **Joblib:** serialização e carregamento do pipeline de Machine Learning.
- **Colorlog:** formatação de logs coloridos no terminal.
- **Python-dotenv:** gerenciamento de variáveis de ambiente.

As versões das dependências estão registradas em `requirements.txt`.

## Estrutura do projeto

```text
DeliveryRisk_AI/
│
├── backend/
│   ├── core/
│   │   ├── exception_handlers.py
│   │   └── logging_config.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── models.py
│   │
│   ├── repositories/
│   │   └── prediction_repository.py
│   │
│   ├── routers/
│   │   ├── health.py
│   │   ├── history.py
│   │   ├── metrics.py
│   │   └── predictions.py
│   │
│   ├── services/
│   │   ├── history_service.py
│   │   ├── metrics_service.py
│   │   └── prediction_service.py
│   │
│   ├── dependencies.py
│   ├── main.py
│   └── schemas.py
│
├── frontend/
│   ├── pages/
│   ├── components/
│   ├── utils/
│   ├── streamlit_app.py
│   ├── api_client.py
│   └── config.py
│
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
│   │
│   └── notebooks/
│       └── delivery_risk_analysis.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│       └── base_integrada.parquet
│
├── models/
│   └── delivery_risk_pipeline.joblib
│
├── images/
│   ├── eda/
│   ├── matrizes_de_confusao/
│   └── avaliacao_modelos/
│
├── reports/
│   └── metrics.json
│
├── logs/
│
├── tests/
│   ├── integration/
│   │   ├── test_health.py
│   │   ├── test_history.py
│   │   ├── test_metrics.py
│   │   └── test_predictions.py
│   │
│   ├── unit/
│   │   ├── test_metrics_service.py
│   │   ├── test_prediction_repository.py
│   │   ├── test_prediction_service.py
│   │   └── test_schemas.py
│   │
│   └── conftest.py
│
├── docs/
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

A estrutura está organizada para separar as responsabilidades:

- `backend/`: implementação da API REST.
- `backend/core/`: configurações centrais, logging e tratamento de exceções.
- `backend/database/`: conexão e estrutura do banco de dados.
- `backend/repositories/`: operações de persistência e acesso aos dados.
- `backend/routers/`: definição dos endpoints da API.
- `backend/services/`: regras de negócio e processamento das solicitações.
- `backend/schemas.py`: modelos Pydantic para validação e estruturação dos dados.
- `frontend/`: estrutura destinada à interface web com Streamlit.
- `pipeline/`: módulos e notebook destinados ao processamento dos dados e à modelagem.
- `data/raw/`: arquivos originais do conjunto de dados.
- `data/processed/`: dados processados e integrados.
- `models/`: modelos e pipelines treinados e serializados.
- `images/`: visualizações e gráficos produzidos durante as análises.
- `reports/`: relatórios consolidados de métricas.
- `logs/`: arquivos de registro da aplicação.
- `tests/`: testes automatizados unitários e de integração.
- `docs/`: documentação técnica do projeto.

A estrutura do frontend representa a organização planejada. Sua implementação funcional ainda não está concluída.

## Base de dados

O projeto utiliza o **Brazilian E-Commerce Public Dataset by Olist**, disponibilizado publicamente no Kaggle.

Fonte: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

Os cinco arquivos CSV utilizados nas etapas de análise e preparação são:

| Arquivo | Descrição |
|---|---|
| `olist_orders_dataset.csv` | Informações dos pedidos e datas relacionadas ao processo de entrega. |
| `olist_order_items_dataset.csv` | Itens associados aos pedidos, incluindo produtos, vendedores, preços e fretes. |
| `olist_customers_dataset.csv` | Identificadores e informações geográficas dos clientes. |
| `olist_products_dataset.csv` | Informações cadastrais, categorias e características físicas dos produtos. |
| `olist_sellers_dataset.csv` | Identificadores e informações geográficas dos vendedores. |

Os arquivos originais são utilizados como fontes para as etapas de análise e preparação dos dados. A disponibilidade dos arquivos no ambiente local deve ser verificada antes da execução do pipeline.

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

O Jupyter e o `ipykernel` fazem parte das dependências do projeto.

O ambiente virtual foi registrado como um kernel do Jupyter com o nome de exibição **Python (DeliveryRisk AI)**.

Para iniciar o Jupyter Notebook:

```powershell
jupyter notebook
```

No notebook `pipeline/notebooks/delivery_risk_analysis.ipynb`, selecione o kernel **Python (DeliveryRisk AI)**.

---

# Fase 2 — Desenvolvimento do pipeline de Machine Learning

**Status: concluída.**

A Fase 2 foi organizada em sete etapas, abrangendo desde a análise exploratória até a avaliação final e serialização do pipeline.

| Etapa | Descrição | Status |
|---|---|---|
| 2.1 | Carregamento, diagnóstico e análise exploratória dos dados (EDA). | Concluída |
| 2.2 | Tratamento e integração dos dados, com construção da variável-alvo. | Concluída |
| 2.3 | Pré-processamento e engenharia de atributos. | Concluída |
| 2.4 | Divisão dos dados em treino, validação e teste. | Concluída |
| 2.5 | Treinamento e ajuste dos modelos. | Concluída |
| 2.6 | Avaliação comparativa e análise do custo computacional. | Concluída |
| 2.7 | Avaliação final, análise de erros, generalização, robustez temporal e serialização do pipeline. | Concluída |

## Etapa 2.1 — Carregamento, diagnóstico e análise exploratória dos dados (EDA)

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

### Resumo do diagnóstico

| Dataset | Registros | Colunas | Valores ausentes | Registros integralmente duplicados |
|---|---:|---:|---:|---:|
| `orders` | 99.441 | 8 | 4.908 | 0 |
| `order_items` | 112.650 | 7 | 0 | 0 |
| `customers` | 99.441 | 5 | 0 | 0 |
| `products` | 32.951 | 9 | 2.448 | 0 |
| `sellers` | 3.095 | 4 | 0 | 0 |
| **Total** | **347.578** | — | **7.356** | **0** |

O total de registros corresponde à soma das linhas dos cinco datasets, que possuem diferentes granularidades. O total de valores ausentes corresponde à soma das células ausentes, e não à quantidade de registros afetados.

### Principais observações

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

### Resultado da etapa

A EDA permitiu documentar as características estruturais dos datasets, os padrões de valores ausentes, as propriedades das distribuições e as associações lineares observadas.

Os resultados serviram de referência para o tratamento, a integração dos dados e a construção da variável-alvo.

## Etapa 2.2 — Tratamento e integração dos dados

**Status: concluída.**

A etapa teve como objetivo preparar, validar e integrar os datasets para construir uma base consolidada, com uma linha por pedido, e criar a variável-alvo utilizada na previsão de atrasos nas entregas.

### Tratamento inicial e validação

Os cinco datasets — `orders`, `order_items`, `customers`, `products` e `sellers` — foram copiados para a estrutura `datasets_trabalho`, preservando os dados originais carregados.

As atividades realizadas foram:

- Conversão das colunas de data selecionadas para o tipo `datetime64[us]`.
- Normalização dos textos, com remoção de espaços nas extremidades e conversão de textos vazios em valores ausentes.
- Validação das chaves dos cinco datasets, incluindo a chave composta de `order_items`.
- Verificação de valores ausentes, não numéricos e infinitos nas colunas numéricas selecionadas.
- Validação das correspondências entre os identificadores dos datasets relacionados.

Não foram identificadas datas inválidas nas colunas verificadas, chaves inválidas ou referências sem correspondência nas relações analisadas. Os valores ausentes existentes foram preservados para avaliação nas etapas posteriores.

### Agregação e integração

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

### Criação e validação da variável-alvo

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

### Investigação dos pedidos sem itens

Foram identificados 775 pedidos sem registros correspondentes em `order_items`.

Esses pedidos apresentaram valores ausentes nas 15 colunas derivadas da agregação. Também foi verificado que nenhum desses pedidos possuía a variável-alvo preenchida.

Os registros foram mantidos na base integrada, e as ausências foram documentadas para orientar as decisões posteriores de preparação dos dados.

### Salvamento da base integrada

A base resultante foi salva no formato Parquet em:

`data/processed/base_integrada.parquet`

O arquivo permite reutilizar os dados integrados nas próximas etapas sem repetir as operações de agregação e integração, desde que os dados de origem e as regras de processamento permaneçam inalterados.

### Resultado da etapa

A Etapa 2.2 foi concluída com a preparação e validação dos datasets, a agregação dos itens por pedido, a integração das informações, a criação e validação da variável-alvo e o salvamento da base consolidada.

A base integrada contém 99.441 registros e 29 colunas, mantém uma linha por pedido e não apresenta IDs de pedido ausentes ou duplicados.

## Etapa 2.3 — Pré-processamento e engenharia de atributos

**Status: concluída.**

A etapa teve como objetivo preparar as variáveis preditoras para a modelagem, criar atributos relevantes a partir do momento da compra e configurar um pipeline de pré-processamento que reduza inconsistências e evite vazamento de informações.

### Elegibilidade e atributos temporais

A base foi filtrada para manter os pedidos elegíveis, isto é, aqueles que possuem uma classificação válida em `delivery_delayed`. A base elegível contém 96.476 pedidos e 29 colunas antes da engenharia de atributos.

A partir de `order_purchase_timestamp`, foram criados seis atributos temporais:

- `ano_compra`: ano em que o pedido foi realizado.
- `mes_compra`: mês da compra.
- `dia_mes_compra`: dia do mês da compra.
- `dia_semana_compra`: dia da semana da compra.
- `hora_compra`: hora da compra.
- `fim_de_semana_compra`: indicador de compra realizada no fim de semana.

A validação confirmou que não havia datas de compra ausentes ou inválidas na base elegível e que os seis atributos temporais criados não continham valores ausentes. O timestamp original foi removido das variáveis preditoras após a criação dos atributos derivados.

### Seleção e validação das variáveis preditoras

Foram selecionadas 24 variáveis preditoras, divididas em 17 numéricas e 7 categóricas.

As variáveis abrangem informações geográficas do cliente, características agregadas dos itens e vendedores do pedido, valores e quantidades, categoria predominante dos produtos e atributos temporais da compra.

A seleção exclui identificadores, a variável-alvo e colunas auxiliares de elegibilidade, além de informações que não estariam disponíveis no momento da compra.

Entre as colunas excluídas estão as datas de entrega, `order_status`, `order_approved_at` e `order_estimated_delivery_date`.

O prefixo do CEP do cliente, `customer_zip_code_prefix`, foi classificado explicitamente como categórico, evitando que seu valor numérico seja interpretado como uma medida contínua.

As validações confirmaram que todas as 24 variáveis foram classificadas, sem sobreposição entre os grupos numérico e categórico, e que a seleção não continha colunas proibidas.

### Diagnóstico dos valores ausentes

A análise dos valores ausentes em `X` identificou:

- `categoria_produto_mais_frequente`: 1.332 valores ausentes, aproximadamente 1,38% dos pedidos elegíveis.
- `product_weight_g_medio`, `product_length_cm_medio`, `product_height_cm_medio` e `product_width_cm_medio`: 16 valores ausentes em cada variável, aproximadamente 0,02%.

A investigação das dimensões físicas mostrou que os 16 pedidos correspondem a 18 itens associados a dois produtos com informações físicas incompletas no dataset `products`. As correspondências entre os itens e os produtos foram encontradas, indicando que as ausências decorrem dos dados cadastrais dos produtos, e não de uma falha na integração.

Os registros não foram excluídos nem receberam valores preenchidos manualmente nesta etapa. O tratamento foi delegado ao pipeline de pré-processamento.

### Configuração do pipeline de pré-processamento

Foi implementado e inspecionado um `ColumnTransformer` para aplicar transformações adequadas a cada tipo de variável.

| Tipo de variável | Estratégia de valores ausentes | Transformação |
|---|---|---|
| Numéricas | Imputação pela mediana (`SimpleImputer`) | Padronização (`StandardScaler`) |
| Categóricas | Imputação pela categoria mais frequente (`SimpleImputer`) | Codificação One-Hot Encoding, com `handle_unknown="ignore"` |

O pipeline foi configurado, mas seus transformadores não foram ajustados sobre a base completa. O ajuste foi realizado posteriormente, exclusivamente com o conjunto de treinamento, evitando que informações dos conjuntos de validação e teste influenciassem o pré-processamento.

### Resultado da etapa

A Etapa 2.3 foi concluída com a seleção e validação de 24 variáveis preditoras, a criação de seis atributos temporais, a análise dos valores ausentes e a configuração do pipeline de pré-processamento.

## Etapa 2.4 — Divisão temporal entre treino, validação e teste

**Status: concluída.**

A divisão foi realizada com base na coluna `order_purchase_timestamp`, utilizando os seguintes intervalos:

| Conjunto | Período das compras | Regra aplicada |
|---|---|---|
| Treino | Até 28/02/2018 | Data anterior a `2018-03-01` |
| Validação | Março a maio de 2018 | Data a partir de `2018-03-01` e anterior a `2018-06-01` |
| Teste | Junho a agosto de 2018 | Data a partir de `2018-06-01` e anterior a `2018-09-01` |

### Resultados da divisão

| Conjunto | Quantidade de pedidos | Pedidos atrasados | Pedidos no prazo | Taxa de atraso |
|---|---:|---:|---:|---:|
| Treino | 57.323 | 4.395 | 52.928 | 7,67% |
| Validação | 20.550 | 2.413 | 18.137 | 11,74% |
| Teste | 18.603 | 1.019 | 17.584 | 5,48% |
| **Total** | **96.476** | **7.827** | **88.649** | **8,11%** |

A divisão foi implementada no módulo `pipeline/src/preparacao_modelo.py`, contendo funções para realizar a separação temporal, resumir os conjuntos e validar os resultados.

As verificações confirmaram:

- Unicidade dos índices de `X`, `y` e da base elegível.
- Alinhamento entre as features e a variável-alvo.
- Ausência de sobreposição de índices entre treino, validação e teste.
- Preservação dos 96.476 registros elegíveis.
- Cumprimento dos intervalos temporais definidos.
- Ordem cronológica entre os conjuntos.
- Consistência das 24 features nos três conjuntos.

O pipeline de pré-processamento permaneceu sem ajuste antes da divisão. Seu treinamento foi realizado exclusivamente com `X_train`.

### Resultado da etapa

A Etapa 2.4 foi concluída com a implementação e validação da divisão temporal dos dados. Os conjuntos de treino, validação e teste foram preparados para as etapas posteriores, preservando a separação cronológica.

## Etapa 2.5 — Treinamento e ajuste dos modelos

**Status: concluída.**

A etapa teve como objetivo implementar, treinar e comparar diferentes configurações de algoritmos de classificação para identificar pedidos com risco de atraso nas entregas.

Foram implementadas funções auxiliares no módulo `pipeline/src/modelos.py` para organizar a criação dos modelos, a construção dos pipelines de pré-processamento, o treinamento, a geração de previsões e o registro dos resultados.

### Preparação dos modelos

A modelagem utilizou as 24 variáveis preditoras definidas na Etapa 2.3:

| Tipo de variável | Quantidade |
|---|---:|
| Numéricas | 17 |
| Categóricas | 7 |
| **Total** | **24** |

O pré-processamento foi integrado aos pipelines dos modelos, com estratégias de imputação, codificação de variáveis categóricas e padronização das variáveis numéricas quando aplicável.

### Experimentos realizados

Foram executados 18 experimentos, distribuídos igualmente entre os três algoritmos.

| Algoritmo | Quantidade de configurações | Hiperparâmetros avaliados |
|---|---:|---|
| Regressão Logística | 6 | `C`, `class_weight` |
| Random Forest | 6 | `n_estimators`, `max_depth`, `class_weight` |
| Gradient Boosting | 6 | `n_estimators`, `learning_rate` |
| **Total** | **18** | — |

As configurações foram comparadas utilizando acurácia, precisão, recall, F1-score e ROC-AUC. Também foram registrados os tempos de treinamento e predição.

### Resultados da Regressão Logística

A Regressão Logística apresentou variação de desempenho conforme a regularização e a ponderação de classes utilizadas.

O maior recall foi de **80,02%**, obtido com `C=0.01` e `class_weight="balanced"`. Essa configuração apresentou precisão de 12,92% e F1-score de 0,2225.

O maior F1-score do algoritmo foi de **0,2357**, obtido com `C=1.0` e `class_weight="balanced"`. O maior ROC-AUC foi de 0,6038, observado com `C=0.1` e `class_weight="balanced"`.

As configurações sem ponderação apresentaram acurácias elevadas, mas tiveram dificuldade para identificar a classe minoritária.

### Resultados do Random Forest

O Random Forest apresentou os melhores resultados gerais entre os três algoritmos avaliados.

A melhor configuração foi obtida no Experimento 4:

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
| Acurácia | 68,10% |
| Precisão | 18,85% |
| Recall | 51,93% |
| F1-score | 0,2766 |
| ROC-AUC | 0,6527 |
| Tempo de treinamento | 5,13 s |
| Tempo de predição | 1,15 s |

Essa configuração apresentou o maior F1-score e o maior ROC-AUC entre os 18 experimentos.

Outra configuração, com `n_estimators=200`, `max_depth=5` e `class_weight="balanced"`, apresentou o maior recall do Random Forest, de 60,75%, mas obteve F1-score de 0,2722.

### Resultados do Gradient Boosting

O Gradient Boosting apresentou baixo desempenho na identificação dos pedidos atrasados, apesar de algumas configurações terem alcançado acurácia próxima de 88,26%.

A melhor configuração do algoritmo foi obtida com `n_estimators=200` e `learning_rate=0.1`:

| Métrica | Resultado |
|---|---:|
| Acurácia | 87,62% |
| Precisão | 17,73% |
| Recall | 1,49% |
| F1-score | 0,0275 |
| ROC-AUC | 0,6080 |
| Tempo de treinamento | 185,88 s |
| Tempo de predição | 1,38 s |

O recall permaneceu muito baixo, e o tempo de treinamento foi significativamente superior ao dos outros algoritmos.

### Comparação geral dos melhores resultados

A tabela apresenta a melhor configuração de cada algoritmo segundo o F1-score obtido no conjunto de validação.

| Algoritmo | Melhor configuração | Precisão | Recall | F1-score | ROC-AUC | Treinamento |
|---|---|---:|---:|---:|---:|---:|
| Regressão Logística | `C=1.0`, `class_weight="balanced"` | 15,19% | 52,55% | 0,2357 | 0,5902 | 6,34 s |
| Random Forest | `n_estimators=100`, `max_depth=10`, `class_weight="balanced"` | 18,85% | 51,93% | 0,2766 | 0,6527 | 5,13 s |
| Gradient Boosting | `n_estimators=200`, `learning_rate=0.1` | 17,73% | 1,49% | 0,0275 | 0,6080 | 185,88 s |

O Random Forest apresentou o melhor equilíbrio entre precisão e recall segundo o F1-score, além do maior ROC-AUC.

### Análise do limiar de classificação

Após a seleção do Random Forest como principal candidato, foi avaliado o impacto de diferentes limiares sobre a classificação dos pedidos como atrasados. A análise utilizou as probabilidades previstas no conjunto de validação.

| Limiar | Precisão | Recall | F1-score | Pedidos classificados como atrasados |
|---:|---:|---:|---:|---:|
| 0,50 | 18,85% | 51,93% | 0,2766 | 6.648 |
| 0,45 | 11,94% | 99,38% | 0,2132 | 20.081 |
| 0,40 | 11,74% | 100,00% | 0,2102 | 20.546 |
| 0,10 a 0,35 | 11,74% | 100,00% | 0,2102 | 20.550 |
| 0,55 | 25,56% | 0,95% | 0,0184 | 90 |
| 0,60 a 0,80 | 0,00% | 0,00% | 0,0000 | 0 |

O limiar de 0,50 apresentou o maior F1-score e foi mantido como referência inicial.

### Resultado da etapa

A Etapa 2.5 foi concluída com o treinamento e a comparação de 18 configurações de modelos.

O Random Forest com `n_estimators=100`, `max_depth=10` e `class_weight="balanced"` foi selecionado para as avaliações posteriores, por apresentar F1-score de 0,2766 e ROC-AUC de 0,6527 na validação.

## Etapa 2.6 — Avaliação comparativa dos modelos

**Status: concluída.**

A etapa teve como objetivo consolidar e comparar os resultados dos experimentos realizados na Etapa 2.5, identificando o modelo candidato mais adequado para a previsão de atrasos nas entregas.

Todas as análises foram realizadas utilizando o conjunto de validação. O conjunto de teste permaneceu reservado para a avaliação final da Etapa 2.7.

### Comparação dos melhores experimentos

| Algoritmo | Experimento | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Random Forest | 4 | 68,10% | 18,85% | 51,93% | 0,2766 | 0,6527 |
| Logistic Regression | 5 | 59,99% | 15,19% | 52,55% | 0,2357 | 0,5902 |
| Gradient Boosting | 6 | 87,62% | 17,73% | 1,49% | 0,0275 | 0,6080 |

### Matrizes de confusão

Foram geradas matrizes de confusão para os melhores experimentos de cada algoritmo, utilizando as previsões sobre o conjunto de validação.

| Modelo | Verdadeiros negativos | Falsos positivos | Falsos negativos | Verdadeiros positivos |
|---|---:|---:|---:|---:|
| Random Forest — Exp. 4 | 12.742 | 5.395 | 1.160 | 1.253 |
| Logistic Regression — Exp. 5 | 11.060 | 7.077 | 1.145 | 1.268 |
| Gradient Boosting — Exp. 6 | 17.970 | 167 | 2.377 | 36 |

As matrizes foram salvas no diretório `images/matrizes_de_confusao/`.

O Random Forest identificou 1.253 pedidos atrasados, mas também apresentou 5.395 falsos positivos. A Regressão Logística identificou 1.268 pedidos atrasados, com 7.077 falsos positivos.

O Gradient Boosting apresentou poucos falsos positivos, porém deixou de identificar 2.377 pedidos que realmente atrasaram.

### Desempenho computacional

O desempenho computacional foi avaliado considerando os 20.550 pedidos do conjunto de validação.

| Modelo | Treinamento (s) | Predição (s) | Latência (ms/pedido) | Pedidos/s |
|---|---:|---:|---:|---:|
| Random Forest — Exp. 4 | 4,22 | 1,04 | 0,0507 | 19.738 |
| Logistic Regression — Exp. 5 | 8,51 | 0,83 | 0,0406 | 24.615 |
| Gradient Boosting — Exp. 6 | 176,75 | 1,87 | 0,0910 | 10.993 |

A Regressão Logística apresentou a menor latência e a maior vazão aproximada. O Random Forest apresentou o menor tempo de treinamento entre os três modelos.

### Tamanho dos modelos

| Modelo | Tamanho |
|---|---:|
| Random Forest — Exp. 4 | 1,5548 MB |
| Logistic Regression — Exp. 5 | 0,2396 MB |
| Gradient Boosting — Exp. 6 | 0,6256 MB |

Todos os modelos permaneceram abaixo de 2 MB.

### Consumo de memória

O pico de memória foi medido durante a execução da predição sobre o conjunto de validação, utilizando `tracemalloc`.

| Modelo | Pico de memória rastreada |
|---|---:|
| Random Forest — Exp. 4 | 17,7755 MB |
| Logistic Regression — Exp. 5 | 17,7705 MB |
| Gradient Boosting — Exp. 6 | 27,9407 MB |

Essa medição representa a memória rastreada pelo `tracemalloc`, não necessariamente o consumo total de RAM do processo, pois algumas alocações internas de bibliotecas nativas podem não ser contabilizadas.

### Seleção do modelo candidato

O modelo selecionado foi o **Random Forest — Experimento 4**.

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

A escolha representa uma seleção preliminar para a avaliação final, não uma aprovação para produção.

### Salvamento dos resultados

Os resultados consolidados da avaliação comparativa foram registrados no relatório de métricas do projeto, incluindo as informações de comparação dos experimentos, desempenho computacional e matrizes de confusão.

As matrizes foram armazenadas em `images/matrizes_de_confusao/`.

### Resultado da etapa

A Etapa 2.6 foi concluída com a comparação dos 18 experimentos, análise dos erros de classificação, avaliação do desempenho computacional e seleção do Random Forest — Experimento 4 como modelo candidato.

O conjunto de teste permaneceu reservado para a avaliação final.

## Etapa 2.7 — Avaliação final, generalização, robustez temporal e serialização

**Status: concluída.**

A etapa teve como objetivo avaliar o modelo candidato no conjunto de teste, analisar a distribuição dos erros, comparar seu desempenho entre validação e teste, investigar a estabilidade temporal e armazenar o pipeline completo para utilização posterior.

As decisões de seleção do modelo foram mantidas com base nos resultados do conjunto de validação. O conjunto de teste foi utilizado exclusivamente para a avaliação final, sem ajuste de hiperparâmetros ou alteração do limiar com base em seus resultados.

### Validação dos dados e recuperação do modelo

Antes da avaliação, foram validados os conjuntos de treino, validação e teste, confirmando a disponibilidade das 24 variáveis preditoras e a consistência das dimensões:

| Conjunto | Registros |
|---|---:|
| Treino | 57.323 |
| Validação | 20.550 |
| Teste | 18.603 |

Foi recuperado o pipeline candidato **Random Forest — Experimento 4**, selecionado na Etapa 2.6 pelo maior F1-score.

### Avaliação final no conjunto de teste

A avaliação foi realizada nos 18.603 registros do conjunto de teste, mantendo o limiar de classificação em 0,50.

| Métrica | Resultado |
|---|---:|
| Acurácia | 66,66% |
| Precisão | 4,64% |
| Recall | 26,01% |
| F1-score | 0,0787 |
| ROC-AUC | 0,4266 |

A matriz de confusão apresentou os seguintes resultados:

| Indicador | Quantidade |
|---|---:|
| Verdadeiros negativos (TN) | 12.135 |
| Falsos positivos (FP) | 5.449 |
| Falsos negativos (FN) | 754 |
| Verdadeiros positivos (TP) | 265 |

O modelo identificou corretamente 265 dos 1.019 pedidos atrasados do conjunto de teste. Também apresentou uma quantidade elevada de falsos positivos e deixou de identificar 754 pedidos que efetivamente atrasaram.

### Análise da distribuição dos erros

Dos 18.603 pedidos avaliados, 12.400 foram classificados corretamente e 6.203 incorretamente. A taxa de erros foi de 33,34%.

Os falsos positivos corresponderam a 29,29% de todos os registros, enquanto os falsos negativos representaram 4,05%.

### Comparação entre validação e teste

| Métrica | Validação | Teste | Variação |
|---|---:|---:|---:|
| Acurácia | 68,10% | 66,66% | -1,45 p.p. |
| Precisão | 18,85% | 4,64% | -14,21 p.p. |
| Recall | 51,93% | 26,01% | -25,92 p.p. |
| F1-score | 27,66% | 7,87% | -19,79 p.p. |
| ROC-AUC | 65,27% | 42,66% | -22,62 p.p. |

A redução das métricas, principalmente de precisão, recall, F1-score e ROC-AUC, indica dificuldade de generalização para o período representado pelo conjunto de teste.

### Caracterização e robustez temporal

O conjunto de teste abrangeu o período de 1º de junho a 29 de agosto de 2018, com 18.603 registros e nenhuma data de compra ausente.

Os registros foram ordenados cronologicamente e divididos em três períodos consecutivos de mesmo tamanho, com 6.201 pedidos cada.

| Indicador | Período 1 | Período 2 | Período 3 |
|---|---:|---:|---:|
| Taxa de atraso | 1,34% | 4,73% | 10,37% |
| Acurácia | 68,44% | 65,01% | 66,52% |
| Precisão | 2,63% | 5,50% | 5,96% |
| Recall | 62,65% | 39,59% | 15,09% |
| F1-score | 5,05% | 9,66% | 8,55% |
| ROC-AUC | 66,20% | 51,90% | 36,62% |
| Falsos negativos | 31 | 177 | 546 |
| Verdadeiros positivos | 52 | 116 | 97 |

A taxa de atraso aumentou progressivamente entre os períodos, enquanto o recall e a ROC-AUC diminuíram. Também houve crescimento da quantidade de falsos negativos.

Os resultados demonstram variação temporal relevante no desempenho do modelo, sem permitir estabelecer, isoladamente, a causa dessa variação.

### Serialização e validação do pipeline

O pipeline completo foi serializado utilizando Joblib e armazenado em:

`models/delivery_risk_pipeline.joblib`

O arquivo gerado possui aproximadamente 1,55 MB.

Em seguida, foi carregado novamente e validado por meio da comparação entre as previsões e probabilidades do pipeline original e do pipeline carregado.

As verificações retornaram:

- `np.array_equal(y_predito_teste, previsoes_carregadas)`: `True`.
- `np.allclose(probabilidades_teste, probabilidades_carregadas)`: `True`.

As verificações confirmaram que o pipeline carregado preservou as previsões e probabilidades produzidas pelo pipeline original.

### Relatório final

Os resultados da etapa foram consolidados em:

`reports/metrics.json`

O relatório contém nove seções:

- `projeto`
- `etapa`
- `modelo_selecionado`
- `avaliacao_validacao`
- `avaliacao_teste`
- `analise_erros`
- `comparacao_generalizacao`
- `robustez_temporal`
- `serializacao`

Após a gravação, o arquivo foi carregado novamente. A leitura e a validação foram concluídas com sucesso.

### Resultado da etapa

A Etapa 2.7 foi concluída com a avaliação final do modelo, a análise dos erros, a comparação entre validação e teste, a investigação da robustez temporal, a serialização do pipeline e a geração do relatório consolidado.

Embora os artefatos técnicos tenham sido gerados e validados, os resultados do conjunto de teste demonstram limitações importantes, especialmente na identificação de pedidos atrasados e na manutenção do desempenho ao longo do tempo.

Assim, o Random Forest selecionado deve ser considerado um candidato experimental, e não um modelo aprovado para produção.

Com a conclusão da Etapa 2.7, encerra-se a **Fase 2 — Desenvolvimento do pipeline de Machine Learning**.

---

# Fase 3 — Desenvolvimento da API com FastAPI

**Status: implementação concluída; testes automatizados aprovados.**

A Fase 3 tem como objetivo disponibilizar o pipeline de Machine Learning por meio de uma API REST, permitindo receber dados de pedidos, realizar previsões de risco de atraso e armazenar o histórico das solicitações.

A API foi desenvolvida com FastAPI, utilizando uma arquitetura modular em camadas para separar validação, regras de negócio, persistência e rotas HTTP.

## Arquitetura modular

O backend foi organizado nas seguintes camadas:

| Camada | Responsabilidade |
|---|---|
| `schemas.py` | Definição dos modelos Pydantic para validação e estruturação dos dados de entrada e saída. |
| `routers/` | Definição dos endpoints e recebimento das requisições HTTP. |
| `services/` | Implementação das regras de negócio e execução das operações. |
| `repositories/` | Acesso e persistência dos dados. |
| `database/` | Conexão e estrutura do banco de dados SQLite. |
| `core/` | Configurações centrais, logging e tratamento global de exceções. |
| `dependencies.py` | Organização das dependências utilizadas pela aplicação. |
| `main.py` | Criação da aplicação, inicialização e integração dos componentes. |

Essa separação evita concentrar toda a implementação em um único arquivo e facilita a manutenção e a evolução do backend.

## Inicialização e carregamento do modelo

A aplicação utiliza `@asynccontextmanager` com `lifespan` para controlar sua inicialização e encerramento.

Durante a inicialização:

1. O sistema configura o logging.
2. A conexão e a estrutura do banco de dados são preparadas.
3. A existência do arquivo `models/delivery_risk_pipeline.joblib` é verificada.
4. O pipeline completo é carregado utilizando Joblib.
5. O modelo fica disponível em `app.state.pipeline` para utilização pelos serviços.

O pipeline é carregado uma única vez durante a inicialização da aplicação, evitando recarregá-lo a cada requisição.

Durante o encerramento, a referência ao pipeline é liberada.

## Validação dos dados

Os modelos Pydantic são utilizados para validar os dados recebidos pela API.

A entrada da previsão corresponde às 24 variáveis preditoras definidas durante a Etapa 2.3 do pipeline de Machine Learning.

A validação ocorre antes da execução do modelo, verificando os tipos e as restrições estabelecidas nos schemas.

Requisições com dados inválidos são rejeitadas com HTTP 422.

## Serviço de previsão

O módulo `backend/services/prediction_service.py` concentra a execução das previsões.

O serviço:

- Recebe os dados validados.
- Organiza os atributos em um DataFrame do Pandas.
- Executa `predict()` para obter a classe prevista.
- Executa `predict_proba()` para obter a probabilidade associada à classe de atraso.
- Identifica a classe positiva por meio de `pipeline.classes_`.
- Retorna o resultado estruturado para o router.

A classe positiva representa o pedido classificado como atrasado.

## Histórico de previsões

O armazenamento do histórico utiliza SQLite.

A implementação está dividida entre:

- `backend/database/connection.py`: conexão com o banco.
- `backend/database/models.py`: estrutura dos registros.
- `backend/repositories/prediction_repository.py`: operações de persistência e consulta.
- `backend/services/history_service.py`: organização das operações de histórico.

As previsões são armazenadas juntamente com os dados de entrada e as informações do resultado.

## Logging e tratamento de exceções

A aplicação possui configuração centralizada de logging em `backend/core/logging_config.py`.

O sistema utiliza:

- `RotatingFileHandler` para armazenamento dos logs.
- Arquivo `logs/delivery_risk.log`.
- Rotação com limite de 10 MB por arquivo.
- Até 30 arquivos de backup.
- Codificação UTF-8.
- Saída no terminal com formatação colorida utilizando Colorlog.

A pasta `logs/` é ignorada pelo Git.

O módulo `backend/core/exception_handlers.py` concentra os handlers globais de exceção, padronizando as respostas de erro.

Entre os tratamentos implementados estão:

- HTTP 404 para recursos não encontrados.
- HTTP 422 para erros de validação.
- HTTP 500 para erros internos do servidor.

## Endpoints implementados

A API disponibiliza os seguintes endpoints:

| Método | Endpoint | Descrição | Resposta esperada |
|---|---|---|---|
| GET | `/health` | Verifica a disponibilidade da aplicação e o carregamento do modelo. | 200 |
| POST | `/predict` | Recebe os dados de um pedido, realiza a previsão e persiste o resultado. | 200 |
| GET | `/predictions` | Lista o histórico de previsões. | 200 |
| GET | `/predictions/{id}` | Consulta uma previsão pelo identificador. | 200 ou 404 |
| DELETE | `/predictions/{id}` | Exclui uma previsão do histórico. | 204 ou 404 |
| GET | `/metrics` | Retorna o relatório consolidado de métricas do modelo. | 200 |

### Exemplos de respostas

**Verificação de saúde — `GET /health`**

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

**Recurso não encontrado — HTTP 404**

```json
{
  "error": "Not Found",
  "message": "Previsão não encontrada."
}
```

**Erro de validação — HTTP 422**

```json
{
  "error": "Validation Error",
  "message": "Os dados enviados são inválidos."
}
```

**Erro interno — HTTP 500**

```json
{
  "error": "Internal Server Error",
  "message": "Ocorreu um erro interno ao processar a solicitação."
}
```

A documentação interativa disponibilizada pelo FastAPI apresenta os schemas completos de entrada e saída, além de permitir executar requisições diretamente pelo navegador.

## Como executar a API

Na raiz do projeto, com o ambiente virtual ativado e as dependências instaladas, execute:

```powershell
uvicorn backend.main:app --reload
```

A API será disponibilizada localmente em:

`http://127.0.0.1:8000`

### Documentação interativa

Swagger UI:

`http://127.0.0.1:8000/docs`

ReDoc:

`http://127.0.0.1:8000/redoc`

A documentação do Swagger permite visualizar os endpoints, consultar os schemas Pydantic, informar os dados de entrada e testar as requisições.

### Verificação da API

Com o servidor em execução, o endpoint de saúde pode ser acessado em:

`http://127.0.0.1:8000/health`

A resposta esperada quando a aplicação está inicializada e o modelo carregado é:

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

## Testes automatizados

O projeto utiliza Pytest para validar os componentes do backend.

Os testes estão organizados em duas categorias:

**Testes unitários (`tests/unit/`)**

Validam os componentes individualmente, incluindo:

- Schemas Pydantic.
- Serviço de previsão.
- Repositório de previsões.
- Serviço de métricas.

**Testes de integração (`tests/integration/`)**

Validam o comportamento dos endpoints e a integração entre os componentes da aplicação:

- Health check.
- Histórico de previsões.
- Consulta de métricas.
- Execução de previsões.

### Executar os testes

Na raiz do projeto:

```powershell
python -m pytest
```

Para executar os testes exibindo os avisos:

```powershell
python -m pytest -W default
```

### Resultado da execução

Na última execução, foram coletados e executados 33 testes.

```text
===========================================================
33 passed in 6.07s
===========================================================
```

| Categoria | Testes aprovados |
|---|---:|
| Integração | 10 |
| Unitários | 23 |
| **Total** | **33** |

Todos os testes foram aprovados na última execução registrada.

## Limitações atuais do modelo

Embora a API esteja implementada e os testes automatizados tenham sido aprovados, o modelo utilizado apresenta limitações importantes.

Na validação, o Random Forest apresentou:

- F1-score de 27,66%.
- ROC-AUC de 65,27%.

No conjunto de teste, apresentou:

- F1-score de 7,87%.
- ROC-AUC de 42,66%.
- Precisão de 4,64%.
- Recall de 26,01%.

A queda entre validação e teste demonstra dificuldade de generalização para o período mais recente.

Portanto, a API disponibiliza um modelo experimental. A implementação técnica da previsão não deve ser confundida com a comprovação de desempenho adequado para utilização em produção.

A evolução do modelo dependerá de novas investigações, experimentos e avaliações.

---

# Variável-alvo

A variável-alvo `delivery_delayed` identifica se um pedido foi entregue após a data estimada:

- `1`: pedido entregue depois da data estimada.
- `0`: pedido entregue na data estimada ou antes dela.
- Valor ausente: pedido sem informações suficientes para determinar a classificação.

A variável foi construída na Etapa 2.2 utilizando as datas efetiva e estimada de entrega e passou por uma verificação independente, sem divergências nos registros elegíveis.

A base integrada contém 96.476 pedidos com classificação válida e 2.965 pedidos sem classificação.

Para prevenir vazamento de dados, o modelo utiliza atributos compatíveis com uma previsão realizada no momento da compra. Informações que só ficam disponíveis depois da compra não devem ser utilizadas como preditores.

Os pedidos sem classificação foram excluídos da base elegível utilizada na preparação para modelagem, conforme os critérios definidos no projeto.

# Controle de versão

O projeto utiliza Git para controle de versão e organização do desenvolvimento por branches.

Branches definidas:

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

# Status atual

## Fase 1 — Estruturação inicial

- [x] Criação da estrutura inicial de diretórios e arquivos.
- [x] Configuração do ambiente virtual Python.
- [x] Definição e registro das dependências em `requirements.txt`.
- [x] Configuração do kernel do Jupyter Notebook.
- [x] Configuração inicial do `.gitignore`.
- [x] Documentação inicial do projeto no `README.md`.

## Fase 2 — Pipeline de Machine Learning

- [x] **Etapa 2.1:** carregamento, diagnóstico e análise exploratória dos dados.
- [x] **Etapa 2.2:** tratamento e integração dos dados, com construção da variável-alvo.
- [x] **Etapa 2.3:** pré-processamento e engenharia de atributos.
- [x] **Etapa 2.4:** divisão dos dados em treino, validação e teste.
- [x] **Etapa 2.5:** treinamento e ajuste dos modelos.
- [x] **Etapa 2.6:** avaliação comparativa e análise do custo computacional.
- [x] **Etapa 2.7:** avaliação final, análise de erros, generalização, robustez temporal e serialização do pipeline.

## Fase 3 — API com FastAPI

- [x] Organização modular do backend em camadas.
- [x] Implementação dos schemas Pydantic.
- [x] Implementação do serviço de previsão.
- [x] Carregamento do pipeline durante a inicialização com `lifespan`.
- [x] Implementação do endpoint de saúde.
- [x] Implementação do endpoint de previsão.
- [x] Implementação da persistência do histórico com SQLite.
- [x] Implementação dos endpoints de consulta e exclusão do histórico.
- [x] Implementação do endpoint de métricas.
- [x] Implementação do logging e tratamento global de exceções.
- [x] Execução e aprovação dos testes automatizados (33 testes).

## Fase 4 — Frontend com Streamlit

- [ ] Implementar a interface web.
- [ ] Desenvolver a comunicação entre Streamlit e FastAPI.
- [ ] Criar a apresentação das previsões.
- [ ] Criar a visualização do histórico.
- [ ] Integrar a apresentação das métricas do modelo.
- [ ] Validar o funcionamento integrado da aplicação.

## Documentação e entrega

- [x] Documentação da estrutura do backend.
- [x] Documentação dos endpoints implementados.
- [x] Instruções de instalação e execução da API.
- [x] Registro das dependências.
- [x] Registro dos resultados dos testes automatizados.
- [ ] Documentação completa da interface web.
- [ ] Gravação e disponibilização do vídeo de demonstração.
- [ ] Definição da licença do projeto.

# Próximas etapas

Com a conclusão do pipeline de Machine Learning e da implementação do backend, as próximas atividades serão dedicadas ao desenvolvimento e à integração da interface web.

As atividades previstas incluem:

1. Desenvolver a interface web com Streamlit.
2. Implementar a comunicação entre o frontend e a API FastAPI.
3. Apresentar as previsões e probabilidades retornadas pela API.
4. Disponibilizar a consulta do histórico de previsões.
5. Apresentar as métricas e limitações do modelo.
6. Executar testes da aplicação integrada.
7. Completar a documentação técnica e de utilização.
8. Gravar o vídeo de demonstração e disponibilizá-lo para entrega.

O desempenho observado no conjunto de teste deverá ser considerado durante o desenvolvimento, pois foram identificadas limitações relevantes na capacidade preditiva do modelo.

# Licença

A licença do projeto será definida posteriormente.
