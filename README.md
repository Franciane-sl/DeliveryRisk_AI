# DeliveryRisk AI

## Sobre o projeto

O **DeliveryRisk AI** é um projeto de Machine Learning que tem como objetivo desenvolver um sistema para prever o risco de atraso nas entregas de pedidos de e-commerce brasileiro.

O projeto utilizará o conjunto de dados público Brazilian E-Commerce Public Dataset by Olist para explorar os dados, preparar as informações, treinar e avaliar modelos preditivos e, futuramente, disponibilizar os resultados por meio de uma API e de uma interface web.

Atualmente, o projeto está na fase de **configuração inicial e organização da estrutura**.

## Objetivo

Desenvolver uma solução de análise preditiva capaz de estimar a probabilidade de um pedido ser entregue após a data prevista, utilizando informações disponíveis no momento da compra.

## Tecnologias previstas

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
- `pipeline/`: scripts, módulos e notebook destinados ao processamento e à modelagem.
- `data/raw/`: arquivos originais do conjunto de dados.
- `data/processed/`: espaço destinado aos dados tratados.
- `models/`: espaço destinado aos modelos treinados.
- `images/`: organização das visualizações e dos gráficos gerados.
- `reports/metrics/`: espaço destinado aos relatórios de métricas.
- `tests/`: testes automatizados.
- `docs/`: documentação técnica do projeto.

Os diretórios e arquivos representam a organização planejada. Suas funcionalidades serão desenvolvidas nas próximas etapas.

## Base de dados

Será utilizado o **Brazilian E-Commerce Public Dataset by Olist**, disponibilizado publicamente no Kaggle.

Fonte: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Os seguintes arquivos CSV já estão organizados em `data/raw/`:

| Arquivo | Descrição |
|---|---|
| `olist_orders_dataset.csv` | Informações dos pedidos e datas relacionadas à entrega. |
| `olist_order_items_dataset.csv` | Itens associados aos pedidos. |
| `olist_customers_dataset.csv` | Informações dos clientes. |
| `olist_products_dataset.csv` | Informações dos produtos. |
| `olist_sellers_dataset.csv` | Informações dos vendedores. |

A preparação e a integração desses dados serão realizadas em uma etapa posterior.

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

As dependências diretas do projeto e suas versões estão registradas em `requirements.txt`.

### 4. Configuração do Jupyter Notebook

O Jupyter e o `ipykernel` estão incluídos nas dependências do projeto. O ambiente virtual foi registrado como um kernel do Jupyter com o nome:

`Python (DeliveryRisk AI)`

Para iniciar o Jupyter Notebook:

```powershell
jupyter notebook
```

No notebook `delivery_risk_analysis.ipynb`, selecione o kernel **Python (DeliveryRisk AI)** para utilizar o ambiente virtual do projeto.

## Controle de versão

O projeto utiliza Git para controle de versão e organização do desenvolvimento por branches.

Branches planejadas:

- `main`
- `develop`
- `feature/Estrutura_do_projeto`
- `feature/Preparacao_de_dados`
- `feature/Ml-pipeline`
- `feature/Backend`
- `feature/Frontend`
- `Feature/Documentacao`

## Status atual

- [x] Criação da estrutura inicial de diretórios e arquivos.
- [x] Organização dos cinco arquivos CSV em `data/raw/`.
- [x] Configuração do ambiente virtual Python.
- [x] Instalação e registro das dependências do projeto.
- [x] Configuração do kernel do Jupyter Notebook.
- [x] Criação do arquivo `requirements.txt`.
- [x] Configuração inicial do `.gitignore`.
- [x] Documentação inicial do projeto no `README.md`.

### Próximas etapas

- [ ] Realizar a análise exploratória dos dados.
- [ ] Definir e executar o processo de preparação e integração dos dados.
- [ ] Treinar e avaliar os modelos de Machine Learning.
- [ ] Desenvolver a API com FastAPI.
- [ ] Desenvolver a interface com Streamlit.
- [ ] Implementar o armazenamento do histórico de previsões.
- [ ] Criar e executar os testes automatizados.
- [ ] Completar a documentação técnica.

## Licença

A licença do projeto será definida posteriormente.
