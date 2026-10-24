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
│   │   ├── preparacao_modelo.py
│   │   ├── modelos.py
│   │   ├── avaliacao.py
│   │   └── robustez.py
│   ├── notebooks/
│   │   └── delivery_risk_analysis.ipynb
│   └── scripts/
│       ├── preparar_dados.py
│       ├── treinar_modelos.py
│       └── avaliar_modelos.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── images/
│   ├── eda/
│   ├── distribuicao_dados/
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

O Jupyter e o `ipykernel` fazem parte das dependências do projeto. O ambiente virtual foi registrado como um kernel do Jupyter com o nome de exibição:

`Python (DeliveryRisk AI)`

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
| 2.3 | Pré-processamento e engenharia de atributos. | Pendente |
| 2.4 | Divisão dos dados em treino, validação e teste. | Pendente |
| 2.5 | Treinamento e ajuste dos modelos. | Pendente |
| 2.6 | Avaliação comparativa e análise do custo computacional. | Pendente |
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

## Variável-alvo

A variável-alvo `delivery_delayed` identifica se um pedido foi entregue após a data estimada:

- `1`: pedido entregue depois da data estimada.
- `0`: pedido entregue na data estimada ou antes dela.
- Valor ausente: pedido sem informações suficientes para determinar a classificação.

A variável foi construída na Etapa 2.2 utilizando as datas efetiva e estimada de entrega e passou por uma verificação independente, sem divergências nos registros elegíveis.

A base integrada contém 96.476 pedidos com classificação válida e 2.965 pedidos sem classificação.

Para prevenir vazamento de dados, o modelo deverá utilizar atributos compatíveis com uma previsão realizada no momento da compra. Informações que só ficam disponíveis depois da compra não deverão ser utilizadas como preditores.

Os pedidos sem classificação deverão ser tratados conforme critérios explícitos de elegibilidade antes do treinamento dos modelos.

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
- [ ] **Etapa 2.3:** pré-processamento e engenharia de atributos.
- [ ] **Etapa 2.4:** divisão dos dados em treino, validação e teste.
- [ ] **Etapa 2.5:** treinamento e ajuste dos modelos.
- [ ] **Etapa 2.6:** avaliação comparativa e análise do custo computacional.
- [ ] **Etapa 2.7:** análise de robustez, generalização e serialização do modelo final.

### Desenvolvimento da aplicação

- [ ] Desenvolver a API com FastAPI.
- [ ] Desenvolver a interface com Streamlit.
- [ ] Implementar o armazenamento do histórico de previsões.
- [ ] Criar e executar os testes automatizados.
- [ ] Completar a documentação técnica.

## Próximas etapas

A próxima atividade é a **Etapa 2.3 — Pré-processamento e Engenharia de Atributos**, que deverá contemplar:

1. Definir os critérios de elegibilidade dos registros para modelagem.
2. Avaliar e tratar os valores ausentes conforme as características e a finalidade das variáveis.
3. Selecionar e preparar os atributos que poderão ser utilizados pelo modelo.
4. Avaliar a necessidade de codificação de variáveis categóricas e transformação de variáveis numéricas.
5. Verificar possíveis fontes de vazamento de dados, considerando o momento em que a previsão deverá ser realizada.
6. Documentar as decisões de preparação e gerar a base destinada às etapas posteriores do pipeline.

As estratégias específicas de pré-processamento e engenharia de atributos serão definidas a partir das características observadas na base integrada e dos requisitos do problema de previsão.

## Licença

A licença do projeto será definida posteriormente.
