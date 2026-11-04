# DeliveryRisk AI

## Sobre o projeto

O **DeliveryRisk AI** é um projeto de Machine Learning que tem como objetivo desenvolver um sistema para prever o risco de atraso nas entregas de pedidos de e-commerce brasileiro.

O projeto utiliza o **Brazilian E-Commerce Public Dataset by Olist** para analisar dados históricos, preparar informações, treinar e avaliar modelos preditivos e disponibilizar previsões por meio de uma API REST.

A solução foi desenvolvida em etapas, desde a análise exploratória e preparação dos dados até a modelagem, avaliação, integração com o backend e desenvolvimento de uma interface web interativa.

O projeto possui finalidade acadêmica e experimental, demonstrando a construção de um fluxo completo de Machine Learning integrado a uma API e a um frontend.

## Objetivo

Desenvolver uma solução de análise preditiva capaz de estimar o risco de um pedido ser entregue após a data prevista, utilizando informações disponíveis no momento da compra.

A solução utiliza dados históricos para construir um modelo de classificação binária, disponibilizar previsões por meio de uma API e apresentar os resultados em uma interface web desenvolvida com Streamlit.

## Tecnologias

- **Python:** linguagem principal.
- **Pandas e NumPy:** manipulação e análise de dados.
- **Scikit-learn:** desenvolvimento e avaliação dos modelos de Machine Learning.
- **Matplotlib, Seaborn e Plotly:** visualização de dados.
- **Jupyter Notebook:** análise exploratória e experimentação.
- **FastAPI e Uvicorn:** desenvolvimento e execução da API REST.
- **Pydantic:** validação e estruturação dos dados.
- **Streamlit:** desenvolvimento da interface web.
- **SQLite:** armazenamento do histórico de previsões.
- **Pytest:** execução dos testes automatizados.
- **HTTPX:** suporte a requisições HTTP e testes.
- **Joblib:** serialização e carregamento do pipeline de Machine Learning.
- **Colorlog:** formatação de logs coloridos no terminal.
- **Python-dotenv:** gerenciamento de variáveis de ambiente.

As versões das dependências estão registradas em `requirements.txt`.

## Estrutura do projeto

```text
DeliveryRisk_AI/
├── backend/
│   ├── core/
│   │   ├── exception_handlers.py
│   │   └── logging_config.py
│   ├── database/
│   │   ├── connection.py
│   │   └── models.py
│   ├── repositories/
│   │   └── prediction_repository.py
│   ├── routers/
│   │   ├── health.py
│   │   ├── history.py
│   │   ├── metrics.py
│   │   └── predictions.py
│   ├── services/
│   │   ├── history_service.py
│   │   ├── metrics_service.py
│   │   └── prediction_service.py
│   ├── dependencies.py
│   ├── main.py
│   └── schemas.py
├── data/
│   ├── raw/
│   ├── processed/
│   │   └── base_integrada.parquet
│   └── delivery_risk.db
├── docs/
│   ├── architecture.md
│   ├── backend_specification.md
│   ├── data_dictionary.md
│   ├── frontend_specification.md
│   ├── implementation_plan.md
│   └── modeling_plan.md
├── frontend/
│   ├── components/
│   │   ├── charts.py
│   │   ├── metric_cards.py
│   │   ├── prediction_result.py
│   │   └── sidebar.py
│   ├── pages/
│   │   ├── historico.py
│   │   ├── nova_Previsao.py
│   │   └── visao_Geral.py
│   ├── utils/
│   │   ├── formatters.py
│   │   └── validators.py
│   ├── api_client.py
│   ├── config.py
│   └── streamlit_app.py
├── images/
│   ├── avaliacao_modelos/
│   ├── eda/
│   └── matrizes_de_confusao/
├── models/
│   └── delivery_risk_pipeline.joblib
├── pipeline/
│   ├── notebooks/
│   │   └── delivery_risk_analysis.ipynb
│   └── src/
│       ├── analise_exploratoria.py
│       ├── avaliacao.py
│       ├── carregamento.py
│       ├── feature_engineering.py
│       ├── integracao_dados.py
│       ├── modelos.py
│       ├── preparacao_modelo.py
│       ├── robustez.py
│       └── tratamento.py
├── reports/
│   ├── metrics/
│   └── metrics.json
├── tests/
│   ├── tests_backend/
│   │   ├── integration/
│   │   └── unit/
│   └── tests_frontend/
│       ├── integration/
│       └── unit/
├── .gitignore
├── requirements.txt
└── README.md
```

A estrutura separa as responsabilidades do projeto:

- `backend/`: API REST desenvolvida com FastAPI.
- `frontend/`: interface web desenvolvida com Streamlit.
- `pipeline/`: módulos de carregamento, análise, tratamento, integração, engenharia de atributos, preparação, treinamento, avaliação e robustez.
- `data/raw/`: datasets originais do Olist.
- `data/processed/`: base integrada utilizada no desenvolvimento do modelo.
- `models/`: pipeline de Machine Learning serializado.
- `reports/`: métricas e resultados dos experimentos.
- `images/`: gráficos da EDA, matrizes de confusão e avaliação dos modelos.
- `tests/`: testes unitários e de integração do backend e frontend.
- `docs/`: documentação técnica e planejamento das etapas do projeto.

## Documentação

A documentação técnica do DeliveryRisk AI está organizada na pasta `docs/`.

| Documento | Descrição |
|---|---|
| [Architecture](docs/architecture.md) | Apresenta a arquitetura geral do sistema, seus componentes e a comunicação entre as camadas. |
| [Backend Specification](docs/backend_specification.md) | Descreve a implementação da API FastAPI, endpoints, serviços, persistência e tratamento de erros. |
| [Data Dictionary](docs/data_dictionary.md) | Documenta as fontes de dados, variáveis, features e estruturas utilizadas no projeto. |
| [Frontend Specification](docs/frontend_specification.md) | Apresenta a estrutura do frontend Streamlit, suas páginas e integração com a API. |
| [Implementation Plan](docs/implementation_plan.md) | Registra as fases de desenvolvimento, atividades realizadas e entregas do projeto. |
| [Modeling Plan](docs/modeling_plan.md) | Documenta a preparação dos dados, treinamento, seleção e avaliação do modelo de Machine Learning. |

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

# Fase 1 — Estruturação inicial

**Status: concluída.**

A fase contemplou a organização inicial do projeto e a preparação do ambiente de desenvolvimento.

Principais entregas:

- Estruturação dos diretórios.
- Configuração do ambiente virtual.
- Instalação e organização das dependências.
- Configuração do Jupyter Notebook e kernel.
- Configuração do Git e `.gitignore`.
- Organização dos dados e arquivos do projeto.

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

### Principais resultados da Fase 2

- Integração de cinco datasets do Olist.
- Construção de uma base integrada com 99.441 pedidos e 29 colunas.
- Criação da variável-alvo `delivery_delayed`.
- Identificação de 96.476 pedidos elegíveis para classificação.
- Seleção de 24 variáveis preditoras.
- Implementação de pré-processamento para variáveis numéricas e categóricas.
- Divisão temporal entre treino, validação e teste.
- Treinamento e comparação de 18 experimentos.
- Seleção do Random Forest — Experimento 4.
- Avaliação final no conjunto de teste.
- Análise de generalização e robustez temporal.
- Serialização do pipeline com Joblib.

## Variável-alvo

A variável `delivery_delayed` representa o resultado da entrega:

- `1`: pedido entregue depois da data estimada.
- `0`: pedido entregue na data estimada ou antes dela.
- Valor ausente: pedido sem informações suficientes para determinar a classificação.

Distribuição da variável-alvo:

| Classificação | Quantidade |
|---|---:|
| Pedidos atrasados | 7.827 |
| Pedidos no prazo | 88.649 |
| Pedidos sem classificação | 2.965 |
| **Total** | **99.441** |

Os registros sem classificação não são utilizados como exemplos rotulados no treinamento supervisionado.

## Divisão dos dados

Foi adotada uma estratégia de divisão temporal (*temporal split*):

| Conjunto | Período |
|---|---|
| Treinamento | Até 28/02/2018 |
| Validação | Março a maio de 2018 |
| Teste | Junho a agosto de 2018 |

Essa estratégia simula o treinamento com dados históricos e a avaliação em períodos posteriores.

## Modelo selecionado

O modelo selecionado foi o **Random Forest — Experimento 4**, com os seguintes hiperparâmetros:

```python
{
    "n_estimators": 100,
    "max_depth": 10,
    "class_weight": "balanced"
}
```

O critério de seleção foi o maior F1-score obtido no conjunto de validação.

## Resultados da avaliação

| Métrica | Validação | Teste |
|---|---:|---:|
| Acurácia | 68,10% | 66,66% |
| Precisão | 18,85% | 4,64% |
| Recall | 51,93% | 26,01% |
| F1-score | 27,66% | 7,87% |
| ROC-AUC | 65,27% | 42,66% |

A avaliação no conjunto de teste demonstrou queda relevante em relação à validação, principalmente nas métricas de precisão, recall, F1-score e ROC-AUC.

O resultado evidencia limitações na capacidade de generalização do modelo, especialmente diante das variações temporais observadas na distribuição dos atrasos.

**Importante:** o modelo possui finalidade experimental e acadêmica. Os resultados não indicam que esteja adequado para utilização operacional ou produção.

# Fase 3 — Desenvolvimento da API com FastAPI

**Status: concluída.**

A API disponibiliza o pipeline de Machine Learning por meio de endpoints REST.

Sua arquitetura é modular e separa as responsabilidades de validação, rotas HTTP, regras de negócio, persistência e configurações centrais.

### Arquitetura do backend

| Diretório/arquivo | Responsabilidade |
|---|---|
| `backend/schemas.py` | Modelos Pydantic para validação dos dados. |
| `backend/routers/` | Endpoints de saúde, previsão, histórico e métricas. |
| `backend/services/` | Regras de negócio para previsão, histórico e métricas. |
| `backend/repositories/` | Operações de persistência e consulta. |
| `backend/database/` | Conexão e estrutura do banco SQLite. |
| `backend/core/` | Logging e tratamento global de exceções. |
| `backend/dependencies.py` | Disponibilização das dependências da aplicação. |
| `backend/main.py` | Criação da aplicação e ciclo de vida. |

Durante a inicialização, o pipeline `models/delivery_risk_pipeline.joblib` é carregado uma única vez no ciclo de vida da aplicação e disponibilizado em `app.state.pipeline`.

### Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/health` | Informa o estado da API e do modelo. |
| POST | `/predict` | Realiza uma previsão e registra o resultado. |
| GET | `/predictions` | Lista as previsões registradas. |
| GET | `/predictions/{id}` | Consulta uma previsão pelo identificador. |
| DELETE | `/predictions/{id}` | Exclui uma previsão do histórico. |
| GET | `/metrics` | Retorna as métricas do modelo. |

### Persistência, logs e exceções

O histórico é armazenado em SQLite. A camada de repositório concentra o acesso aos registros, enquanto os serviços organizam as operações utilizadas pelas rotas.

O logging utiliza `RotatingFileHandler` e a aplicação possui tratamento global de exceções para padronizar respostas de erro.

A documentação interativa da API é disponibilizada pelo FastAPI em `/docs` (Swagger UI) e `/redoc` (ReDoc).

# Fase 4 — Frontend com Streamlit

**Status: concluída.**

O frontend foi desenvolvido como uma camada de apresentação para consumir a API.

A interface não carrega o modelo de Machine Learning nem acessa diretamente o banco SQLite. Todas as operações são realizadas por meio dos endpoints do backend.

## Páginas da aplicação

### Visão geral

Apresenta indicadores calculados a partir do histórico retornado pela API:

- Total de previsões realizadas.
- Quantidade de previsões classificadas como atraso.
- Quantidade de previsões classificadas sem atraso.
- Probabilidade média de atraso.

Também apresenta gráficos de distribuição das classificações, distribuição das probabilidades e evolução temporal das previsões.

### Nova previsão

Disponibiliza um formulário para informar as características do pedido, organizado em seções:

- Informações gerais e quantidades.
- Valores, frete e dimensões médias dos produtos.
- Data e horário da compra.
- Informações geográficas.
- Categoria de produto mais frequente.

Os dados são validados no frontend e enviados ao endpoint `POST /predict`.

O resultado apresenta a classificação, a probabilidade estimada de atraso e o identificador da previsão registrada.

### Histórico

Permite consultar as previsões armazenadas pela API, visualizar indicadores, selecionar um registro para consultar seus detalhes e excluir uma previsão após confirmação.

## Organização do frontend

| Arquivo/diretório | Responsabilidade |
|---|---|
| `frontend/streamlit_app.py` | Configuração visual e navegação. |
| `frontend/pages/` | Implementação das páginas. |
| `frontend/components/` | Componentes reutilizáveis. |
| `frontend/utils/` | Funções de validação e formatação. |
| `frontend/api_client.py` | Cliente HTTP centralizado. |
| `frontend/config.py` | Configurações da aplicação. |

O `APIClient` centraliza as chamadas HTTP e trata timeout, falha de conexão, erros HTTP, respostas JSON inválidas e respostas sem conteúdo HTTP 204.

O timeout padrão das requisições é de 10 segundos.

A URL da API pode ser configurada pela variável de ambiente `DELIVERYRISK_API_URL`. Na ausência dessa variável, o frontend utiliza `http://127.0.0.1:8000`.

---

# Como executar a aplicação completa

Execute os comandos a partir da raiz do projeto.

## 1. Configurar o ambiente

Caso ainda não tenha configurado o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## 2. Iniciar a API FastAPI

Abra o primeiro terminal, na raiz do projeto, com o ambiente virtual ativado.

Execute:

```powershell
uvicorn backend.main:app --reload
```

A API ficará disponível em:

`http://127.0.0.1:8000`

## 3. Iniciar o frontend Streamlit

Abra um segundo terminal na raiz do projeto.

Ative o mesmo ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Configure o caminho dos módulos do frontend:

```powershell
$env:PYTHONPATH = "$PWD\frontend;$PWD"
```

Execute a aplicação:

```powershell
streamlit run frontend/streamlit_app.py
```

A interface ficará disponível em:

`http://localhost:8501`

## Endereços locais

| Serviço | Endereço |
|---|---|
| Frontend Streamlit | `http://localhost:8501` |
| API FastAPI | `http://127.0.0.1:8000` |
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |
| Health check | `http://127.0.0.1:8000/health` |

### Configuração da URL da API

Para utilizar outro endereço de API, configure a variável de ambiente antes de iniciar o Streamlit.

Exemplo no PowerShell:

```powershell
$env:DELIVERYRISK_API_URL = "http://127.0.0.1:8000"
```

# Testes automatizados

O projeto utiliza Pytest e organiza os testes por componente e tipo:

- `tests/tests_backend/unit/`: testes unitários do backend.
- `tests/tests_backend/integration/`: testes de integração dos endpoints.
- `tests/tests_frontend/unit/`: testes do cliente HTTP, formatadores e validadores.
- `tests/tests_frontend/integration/`: testes de integração da comunicação com a API e das páginas Streamlit.

Para executar a suíte completa na raiz do projeto:

```powershell
python -m pytest tests/ -v
```

### Resultado da última execução registrada

<badge color="success">91 testes aprovados</badge>

| Grupo | Quantidade |
|---|---:|
| Backend — testes unitários | 23 |
| Backend — testes de integração | 10 |
| Frontend — integração API | 6 |
| Frontend — páginas Streamlit | 12 |
| Frontend — API Client | 13 |
| Frontend — formatadores | 10 |
| Frontend — validadores | 17 |
| **Total** | **91** |

A suíte contempla validação dos dados, serviços e persistência do backend, endpoints da API, tratamento de respostas HTTP, utilitários do frontend e renderização e comportamento das páginas Streamlit.

# Artefatos gerados

| Arquivo/diretório | Conteúdo |
|---|---|
| `data/processed/base_integrada.parquet` | Base integrada utilizada no pipeline. |
| `models/delivery_risk_pipeline.joblib` | Pipeline completo serializado com Joblib. |
| `reports/metrics.json` | Métricas de validação, teste, análise de erros e robustez temporal. |
| `reports/metrics/` | Relatórios de comparação dos experimentos e desempenho computacional. |
| `images/eda/` | Visualizações da análise exploratória. |
| `images/matrizes_de_confusao/` | Matrizes de confusão dos modelos avaliados. |
| `images/avaliacao_modelos/` | Gráficos complementares da avaliação. |
| `data/delivery_risk.db` | Banco SQLite utilizado para armazenar o histórico de previsões. |

# Status geral do projeto

## Fase 1 — Estruturação inicial

- [x] Criação da estrutura de diretórios.
- [x] Configuração do ambiente virtual e dependências.
- [x] Configuração do Jupyter Notebook e kernel.
- [x] Configuração inicial do Git e `.gitignore`.
- [x] Organização inicial do projeto.

## Fase 2 — Pipeline de Machine Learning

- [x] Etapa 2.1 — Carregamento, diagnóstico e análise exploratória.
- [x] Etapa 2.2 — Tratamento, integração e construção da variável-alvo.
- [x] Etapa 2.3 — Pré-processamento e engenharia de atributos.
- [x] Etapa 2.4 — Divisão temporal entre treino, validação e teste.
- [x] Etapa 2.5 — Treinamento e ajuste dos modelos.
- [x] Etapa 2.6 — Avaliação comparativa e análise do custo computacional.
- [x] Etapa 2.7 — Avaliação final, análise de erros, robustez temporal e serialização.

## Fase 3 — API com FastAPI

- [x] Arquitetura modular em camadas.
- [x] Schemas Pydantic e validação de entrada e saída.
- [x] Carregamento do pipeline no ciclo de vida da aplicação.
- [x] Endpoints de saúde, previsão, histórico e métricas.
- [x] Persistência do histórico com SQLite.
- [x] Logging e tratamento global de exceções.
- [x] Testes unitários e de integração.

## Fase 4 — Frontend com Streamlit

- [x] Página Visão geral.
- [x] Página Nova previsão.
- [x] Página Histórico.
- [x] Cliente HTTP centralizado para comunicação com a API.
- [x] Exibição de resultados, indicadores e gráficos.
- [x] Consulta detalhada e exclusão de previsões.
- [x] Testes unitários e de integração.
- [x] Validação da execução integrada com a API.

## Documentação e entrega

- [x] README principal.
- [x] Documentação da arquitetura.
- [x] Dicionário de dados.
- [x] Plano de implementação.
- [x] Plano de modelagem.
- [x] Especificação técnica do backend.
- [x] Especificação técnica do frontend.
- [x] Definição da licença do projeto.


# Licença

Este projeto está licenciado sob a **MIT License**.

A licença permite o uso, a cópia, a modificação e a distribuição do código, desde que o aviso de copyright e o texto da licença sejam preservados.

Consulte o arquivo [LICENSE](LICENSE) para acessar os termos completos.

A licença do projeto não substitui as condições de uso dos datasets, bibliotecas e demais recursos de terceiros utilizados.