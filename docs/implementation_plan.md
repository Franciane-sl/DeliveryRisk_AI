# Plano de Implementação — DeliveryRisk AI

## 1. Visão geral

O **DeliveryRisk AI** é um projeto de Machine Learning desenvolvido para prever o risco de atraso na entrega de pedidos de e-commerce brasileiro, utilizando o Brazilian E-Commerce Public Dataset by Olist.

O desenvolvimento foi organizado em quatro fases principais:

1. Estruturação e preparação inicial do projeto.
2. Desenvolvimento do pipeline de Machine Learning.
3. Implementação da API REST com FastAPI.
4. Desenvolvimento da interface web com Streamlit.

As três primeiras fases correspondem ao desenvolvimento principal da solução. A quarta fase foi implementada como uma funcionalidade adicional para facilitar a utilização e a demonstração do sistema.

Este documento apresenta o planejamento, as atividades realizadas, os resultados obtidos e as possibilidades de evolução do projeto.

## 2. Objetivos da implementação

Os principais objetivos do desenvolvimento foram:

- Construir uma base de dados integrada a partir dos datasets da Olist.
- Realizar análise exploratória e preparação dos dados.
- Construir uma variável-alvo que represente o atraso das entregas.
- Desenvolver e avaliar modelos de Machine Learning.
- Selecionar um modelo com base em métricas de avaliação.
- Disponibilizar o modelo por meio de uma API REST.
- Implementar persistência do histórico de previsões.
- Desenvolver uma interface web para interação com o sistema.
- Implementar testes automatizados para validar os componentes.

## 3. Planejamento geral das fases

| Fase | Descrição | Status |
|---|---|---|
| Fase 1 | Estruturação inicial do projeto | Concluída |
| Fase 2 | Pipeline de Machine Learning | Concluída |
| Fase 3 | API REST com FastAPI | Concluída |
| Fase 4 | Frontend com Streamlit | Concluída |

<badge color="success">Implementação principal concluída</badge>

## 4. Fase 1 — Estruturação inicial do projeto

### 4.1. Objetivo

Preparar o ambiente de desenvolvimento, organizar os diretórios e estabelecer a estrutura inicial do DeliveryRisk AI.

### 4.2. Atividades planejadas

- Definir o objetivo do projeto.
- Identificar e obter os datasets necessários.
- Configurar o ambiente virtual Python.
- Instalar as dependências iniciais.
- Organizar os diretórios do projeto.
- Configurar o controle de versão com Git.
- Criar o README inicial.

### 4.3. Atividades executadas

- Estruturação dos diretórios principais.
- Configuração do ambiente Python.
- Organização dos arquivos de dados.
- Configuração do repositório Git.
- Preparação do ambiente para análise e desenvolvimento do pipeline.

### 4.4. Resultado

A estrutura inicial foi concluída, permitindo o desenvolvimento modular das etapas seguintes.

**Critérios de conclusão:**

- [x] Estrutura de diretórios criada.
- [x] Ambiente de desenvolvimento configurado.
- [x] Datasets disponibilizados.
- [x] Repositório Git configurado.
- [x] Documentação inicial criada.

## 5. Fase 2 — Pipeline de Machine Learning

### 5.1. Objetivo

Desenvolver um pipeline de Machine Learning capaz de preparar os dados históricos da Olist, treinar modelos e estimar o risco de atraso das entregas.

### 5.2. Etapa 1 — Carregamento dos dados

**Atividades:**

- Implementar funções para carregamento dos arquivos CSV.
- Verificar a existência dos arquivos.
- Identificar problemas de leitura e estrutura.
- Inspecionar as dimensões dos datasets.

**Resultado:**

Foram utilizados cinco datasets originais:

- Orders.
- Order Items.
- Customers.
- Products.
- Sellers.

### 5.3. Etapa 2 — Análise exploratória

**Atividades:**

- Analisar a distribuição dos dados.
- Investigar valores ausentes.
- Identificar duplicidades.
- Verificar inconsistências.
- Analisar características temporais.
- Investigar a distribuição dos pedidos e entregas.

**Resultado:**

A análise exploratória forneceu informações para orientar as decisões de tratamento, integração e engenharia de atributos.

### 5.4. Etapa 3 — Tratamento e integração

**Atividades:**

- Validar chaves de relacionamento.
- Tratar inconsistências.
- Integrar os cinco datasets.
- Agregar os itens ao nível do pedido.
- Construir uma base com uma linha por pedido.

**Resultado:**

Foi gerada a base integrada:

`data/processed/base_integrada.parquet`

A base possui:

- 99.441 pedidos.
- 29 colunas.
- Granularidade de uma linha por pedido.

### 5.5. Etapa 4 — Construção da variável-alvo

**Objetivo:**

Criar a variável `delivery_delayed`, responsável por representar se um pedido foi entregue com atraso.

**Regra aplicada:**

- `1`: entrega posterior à data estimada.
- `0`: entrega realizada até a data estimada.
- `NaN`: pedido sem informações suficientes para classificação.

Somente pedidos com data real e data estimada de entrega disponíveis são considerados elegíveis.

**Distribuição registrada:**

| Classificação | Quantidade |
|---|---:|
| Pedidos atrasados | 7.827 |
| Pedidos no prazo | 88.649 |
| Pedidos sem classificação | 2.965 |
| Total | 99.441 |

### 5.6. Etapa 5 — Engenharia de atributos

**Atividades:**

- Selecionar variáveis relevantes.
- Criar atributos temporais.
- Agregar características dos produtos e vendedores.
- Separar variáveis numéricas e categóricas.
- Excluir identificadores e informações com risco de vazamento de dados.

**Resultado:**

Foram selecionadas 24 features:

- 17 numéricas.
- 7 categóricas ou booleanas.

Os atributos representam características do pedido, localização, produtos, vendedores e momento da compra.

### 5.7. Etapa 6 — Preparação dos dados

**Atividades:**

- Separar os conjuntos de treinamento, validação e teste.
- Aplicar divisão temporal.
- Configurar o pré-processamento.
- Tratar valores ausentes.
- Codificar variáveis categóricas.
- Padronizar variáveis numéricas quando configurado.

**Divisão temporal:**

| Conjunto | Período |
|---|---|
| Treinamento | Até 28/02/2018 |
| Validação | Março a maio de 2018 |
| Teste | Junho a agosto de 2018 |

A divisão temporal foi adotada para respeitar a ordem cronológica dos pedidos e reduzir o risco de vazamento de informações entre os conjuntos.

### 5.8. Etapa 7 — Treinamento e avaliação

**Atividades:**

- Configurar os algoritmos de classificação.
- Treinar os experimentos.
- Comparar resultados.
- Avaliar métricas de classificação.
- Selecionar o modelo final.

O modelo selecionado foi o Random Forest, experimento 4, com:

- `n_estimators=100`
- `max_depth=10`
- `class_weight="balanced"`

O critério de seleção foi o maior F1-score na validação.

### 5.9. Etapa 8 — Avaliação de robustez e serialização

**Atividades:**

- Avaliar o desempenho temporal.
- Investigar limitações de generalização.
- Registrar as métricas.
- Serializar o pipeline selecionado.

**Artefatos gerados:**

| Arquivo | Finalidade |
|---|---|
| `models/delivery_risk_pipeline.joblib` | Pipeline de Machine Learning serializado. |
| `reports/metrics.json` | Métricas de avaliação do modelo. |
| `data/processed/base_integrada.parquet` | Base integrada utilizada no projeto. |

### 5.10. Critérios de conclusão da Fase 2

- [x] Carregamento dos datasets.
- [x] Análise exploratória.
- [x] Tratamento dos dados.
- [x] Integração dos cinco datasets.
- [x] Agregação dos itens por pedido.
- [x] Construção da variável-alvo.
- [x] Engenharia de atributos.
- [x] Prevenção de vazamento de dados.
- [x] Divisão temporal.
- [x] Treinamento dos modelos.
- [x] Comparação dos experimentos.
- [x] Avaliação do modelo.
- [x] Serialização do pipeline.

## 6. Fase 3 — API REST com FastAPI

### 6.1. Objetivo

Disponibilizar o modelo de Machine Learning por meio de uma API REST, permitindo realizar previsões, consultar métricas e gerenciar o histórico de resultados.

A API foi desenvolvida utilizando FastAPI e organizada em camadas.

### 6.2. Etapa 1 — Estrutura modular

**Atividades:**

- Criar a estrutura do backend.
- Separar routers, schemas, services e repositories.
- Organizar configurações centrais.
- Implementar o ponto de entrada da aplicação.

**Resultado:**

O backend passou a possuir uma arquitetura modular, separando as responsabilidades de comunicação, validação, regras de negócio e persistência.

### 6.3. Etapa 2 — Validação dos dados

**Atividades:**

- Implementar schemas Pydantic.
- Validar os dados recebidos.
- Definir campos obrigatórios.
- Configurar limites e tipos esperados.
- Rejeitar campos adicionais não permitidos.

**Resultado:**

A API passou a validar os dados de entrada antes de encaminhá-los ao pipeline.

### 6.4. Etapa 3 — Integração com o modelo

**Atividades:**

- Carregar o pipeline serializado.
- Implementar o mecanismo de inicialização.
- Disponibilizar o modelo por meio de dependências.
- Implementar o serviço de previsão.
- Retornar classe prevista e probabilidade estimada.

**Resultado:**

O modelo passou a ser carregado uma única vez durante a inicialização da aplicação, ficando disponível para as requisições.

### 6.5. Etapa 4 — Persistência do histórico

**Atividades:**

- Configurar SQLite.
- Criar a tabela de previsões.
- Implementar Repository.
- Persistir os resultados.
- Implementar consultas e exclusões.

**Resultado:**

As previsões passaram a ser armazenadas no banco `data/delivery_risk.db`.

### 6.6. Etapa 5 — Implementação dos endpoints

Foram implementados os seguintes endpoints:

| Método | Endpoint | Funcionalidade |
|---|---|---|
| GET | `/health` | Verificar disponibilidade da API. |
| POST | `/predict` | Realizar previsão. |
| GET | `/predictions` | Consultar histórico. |
| GET | `/predictions/{id}` | Consultar previsão específica. |
| DELETE | `/predictions/{id}` | Excluir previsão. |
| GET | `/metrics` | Consultar métricas do modelo. |

### 6.7. Etapa 6 — Logging e tratamento de erros

**Atividades:**

- Configurar logging.
- Implementar rotação de arquivos de log.
- Criar exception handlers.
- Padronizar respostas de erro.
- Tratar erros de validação e execução.

**Resultado:**

A API passou a registrar eventos e tratar exceções de forma centralizada.

### 6.8. Etapa 7 — Testes automatizados

Foram desenvolvidos testes unitários e de integração para validar:

- Schemas.
- Serviços.
- Repositórios.
- Endpoints.
- Persistência.
- Métricas.
- Tratamento de erros.

### 6.9. Critérios de conclusão da Fase 3

- [x] Estrutura modular do backend.
- [x] Schemas Pydantic.
- [x] Integração com o pipeline.
- [x] Carregamento único do modelo.
- [x] Banco SQLite.
- [x] Repository.
- [x] Serviços de negócio.
- [x] Endpoints REST.
- [x] Logging.
- [x] Exception handlers.
- [x] Testes unitários.
- [x] Testes de integração.
- [x] Documentação Swagger.

## 7. Fase 4 — Frontend com Streamlit

### 7.1. Objetivo

Desenvolver uma interface web para facilitar a interação com a API e permitir a demonstração visual das funcionalidades do DeliveryRisk AI.

Esta fase foi implementada como um bônus ao escopo principal do projeto.

### 7.2. Etapa 1 — Estruturação do frontend

**Atividades:**

- Criar o diretório `frontend/`.
- Organizar páginas.
- Criar componentes reutilizáveis.
- Criar utilitários.
- Implementar configurações centralizadas.

### 7.3. Etapa 2 — Cliente HTTP

**Atividades:**

- Implementar a classe `APIClient`.
- Centralizar as requisições HTTP.
- Configurar timeout.
- Implementar tratamento de erros.
- Integrar os métodos aos endpoints da API.

**Resultado:**

O frontend passou a consumir os serviços do backend por meio de uma camada única de comunicação.

### 7.4. Etapa 3 — Página de visão geral

**Atividades:**

- Implementar indicadores.
- Consultar métricas do modelo.
- Consultar informações gerais da API.
- Apresentar gráficos e informações resumidas.

### 7.5. Etapa 4 — Página de nova previsão

**Atividades:**

- Criar formulário de entrada.
- Implementar validação dos campos.
- Enviar dados para o endpoint `/predict`.
- Apresentar a classe prevista.
- Apresentar a probabilidade estimada de atraso.

### 7.6. Etapa 5 — Página de histórico

**Atividades:**

- Consultar previsões armazenadas.
- Apresentar registros.
- Consultar detalhes individuais.
- Implementar exclusão de previsões.

### 7.7. Etapa 6 — Testes e validação

**Atividades:**

- Criar testes para o cliente HTTP.
- Testar funções de formatação.
- Testar validadores.
- Testar páginas Streamlit.
- Testar integração com a API.
- Realizar validação manual da aplicação.

**Resultado:**

O frontend foi executado e validado com sucesso, com comunicação funcional com a API.

### 7.8. Critérios de conclusão da Fase 4

- [x] Estrutura modular do frontend.
- [x] Configuração da aplicação.
- [x] Cliente HTTP.
- [x] Página de visão geral.
- [x] Página de nova previsão.
- [x] Página de histórico.
- [x] Componentes reutilizáveis.
- [x] Funções auxiliares de validação e formatação.
- [x] Tratamento de erros.
- [x] Testes automatizados.
- [x] Validação manual.

## 8. Estratégia de testes

Os testes automatizados foram desenvolvidos utilizando Pytest.

A estratégia contempla testes unitários e de integração.

### 8.1. Testes unitários

Verificam o comportamento isolado dos componentes.

Incluem:

- Validação de schemas.
- Serviços do backend.
- Repositórios.
- Cliente HTTP.
- Formatação de dados.
- Validação de campos do frontend.

### 8.2. Testes de integração

Verificam a comunicação entre diferentes componentes.

Incluem:

- Endpoints FastAPI.
- Persistência SQLite.
- Comunicação HTTP.
- Integração frontend e API.
- Comportamento das páginas Streamlit.

### 8.3. Resultado dos testes

Na execução completa registrada durante o desenvolvimento:

<badge color="success">91 testes aprovados</badge>

| Grupo | Quantidade |
|---|---:|
| Backend — integração | 10 |
| Backend — unitários | 23 |
| Frontend — integração API | 6 |
| Frontend — páginas Streamlit | 12 |
| Frontend — API Client | 13 |
| Frontend — formatters | 10 |
| Frontend — validators | 17 |
| **Total** | **91** |

Comando para executar todos os testes:

```bash
python -m pytest tests/ -v
```

## 9. Organização das entregas

As principais entregas do projeto são:

| Entrega | Descrição | Status |
|---|---|---|
| Base integrada | Dataset consolidado por pedido. | Concluída |
| Pipeline ML | Pipeline de treinamento e previsão. | Concluída |
| Modelo serializado | Arquivo Joblib. | Concluída |
| Relatório de métricas | Resultados da avaliação. | Concluída |
| API REST | Endpoints para integração com o modelo. | Concluída |
| Banco de dados | Persistência do histórico. | Concluída |
| Frontend | Interface web Streamlit. | Concluída |
| Testes automatizados | Testes unitários e de integração. | Concluída |
| README | Documentação geral. | Atualizada |
| Architecture | Documentação arquitetural. | Elaborada |
| Data Dictionary | Dicionário de dados. | Elaborado |
| Frontend Specification | Especificação do frontend. | Elaborada |
| Implementation Plan | Plano de implementação. | Elaborado |

## 10. Riscos e limitações identificados

Durante o desenvolvimento, foram identificadas limitações que devem ser consideradas na interpretação dos resultados.

### 10.1. Desbalanceamento da variável-alvo

A quantidade de pedidos no prazo é significativamente superior à quantidade de pedidos atrasados.

Esse desbalanceamento influencia o treinamento e a avaliação dos modelos.

### 10.2. Generalização temporal

A divisão temporal permite avaliar o comportamento do modelo em períodos posteriores aos dados utilizados no treinamento.

Entretanto, os resultados do conjunto de teste demonstram limitações de generalização.

### 10.3. Qualidade dos dados

Os datasets históricos possuem valores ausentes e limitações relacionadas à disponibilidade de determinadas informações.

O pré-processamento reduz parte desses problemas, mas não elimina todas as limitações dos dados originais.

### 10.4. Natureza experimental

O modelo é experimental e foi desenvolvido para fins acadêmicos.

As previsões representam estimativas produzidas a partir dos dados históricos e não garantem o resultado real de uma entrega.


## 11. Considerações finais

O desenvolvimento do DeliveryRisk AI foi organizado em fases que permitiram evoluir desde a preparação dos dados até a disponibilização de uma aplicação integrada.

O pipeline de Machine Learning foi desenvolvido para processar os dados históricos e gerar previsões experimentais.

A API FastAPI disponibiliza os serviços de previsão, consulta de métricas e gerenciamento do histórico.

O frontend Streamlit complementa a solução, oferecendo uma interface para interação com os recursos disponibilizados pelo backend.

Ao final da implementação, o projeto conta com pipeline serializado, API modular, persistência em SQLite, interface web e 91 testes automatizados aprovados na execução registrada.
