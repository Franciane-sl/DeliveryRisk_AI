# Plano de Modelagem — DeliveryRisk AI

## 1. Visão geral

Este documento descreve o planejamento e a execução da etapa de modelagem de Machine Learning do projeto **DeliveryRisk AI**.

O objetivo é desenvolver um modelo capaz de estimar o risco de atraso na entrega de pedidos de e-commerce brasileiro, utilizando dados históricos do Brazilian E-Commerce Public Dataset by Olist.

A modelagem foi conduzida considerando a granularidade por pedido, a prevenção de vazamento de dados (*data leakage*) e a separação temporal dos conjuntos de dados.

O modelo possui finalidade acadêmica e experimental, sendo utilizado para demonstrar o desenvolvimento de um pipeline de Machine Learning integrado a uma API e a uma interface web.

## 2. Objetivo da modelagem

Desenvolver um modelo de classificação binária para identificar pedidos com risco de atraso na entrega.

A variável-alvo utilizada é:

- `delivery_delayed = 1`: pedido entregue após a data estimada.
- `delivery_delayed = 0`: pedido entregue dentro do prazo.
- `delivery_delayed = NaN`: pedido sem condições de classificação.

O problema foi tratado como uma tarefa de classificação supervisionada.

## 3. Fonte de dados

A modelagem utiliza o **Brazilian E-Commerce Public Dataset by Olist**.

Foram utilizados cinco conjuntos de dados:

- `olist_orders_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`

Os dados foram integrados em uma base única, mantendo a granularidade de um registro por pedido.

### 3.1 Base integrada

Arquivo principal:

`data/processed/base_integrada.parquet`

Características da base:

- 99.441 pedidos.
- 29 colunas.
- Informações de pedidos, clientes, itens, produtos e vendedores.
- Dados agregados ao nível do pedido.

## 4. Preparação dos dados

A preparação dos dados teve como objetivo construir uma base adequada ao treinamento e à avaliação do modelo.

As principais atividades foram:

1. Carregamento dos arquivos CSV.
2. Integração dos cinco conjuntos de dados.
3. Tratamento das relações entre pedidos, itens, produtos, clientes e vendedores.
4. Agregação das informações de itens para o nível do pedido.
5. Construção da variável-alvo `delivery_delayed`.
6. Identificação dos pedidos elegíveis para classificação.
7. Seleção das variáveis preditoras.
8. Separação dos dados em conjuntos temporais.

### 4.1 Elegibilidade dos pedidos

Nem todos os pedidos podem ser utilizados no treinamento.

Pedidos sem informações suficientes para determinar se houve atraso são mantidos sem classificação na variável-alvo.

Distribuição registrada na base:

| Classificação | Quantidade |
|---|---:|
| Pedidos atrasados | 7.827 |
| Pedidos entregues no prazo | 88.649 |
| Pedidos sem classificação | 2.965 |
| **Total** | **99.441** |

Os registros sem classificação não são utilizados como exemplos rotulados no treinamento supervisionado.

## 5. Seleção das variáveis

Foram selecionadas 24 features para representar características dos pedidos e informações disponíveis para a previsão.

Distribuição:

- 17 variáveis numéricas.
- 7 variáveis categóricas ou booleanas.

A seleção considera informações disponíveis no contexto da previsão, evitando utilizar dados que somente seriam conhecidos depois da entrega.

### 5.1 Prevenção de Data Leakage

Um dos principais cuidados da modelagem foi evitar o vazamento de informações.

Foram excluídas variáveis que poderiam revelar diretamente o resultado da entrega ou informações posteriores ao momento em que a previsão deveria ser realizada.

Entre os exemplos de informações que exigem exclusão estão:

- Data efetiva de entrega.
- Diferença entre a data estimada e a data real de entrega.
- Indicadores derivados diretamente da ocorrência do atraso.
- Outras informações que dependam de eventos posteriores à previsão.

Essa decisão busca garantir que o modelo aprenda padrões associados ao risco de atraso, em vez de utilizar informações que já revelam o resultado.

## 6. Divisão dos dados

Foi adotada uma estratégia de divisão temporal (*temporal split*).

Essa abordagem simula um cenário em que o modelo é treinado com pedidos históricos e avaliado em pedidos de períodos posteriores.

| Conjunto | Período |
|---|---|
| Treinamento | Até 28/02/2018 |
| Validação | Março a maio de 2018 |
| Teste | Junho a agosto de 2018 |

A divisão temporal evita a mistura aleatória de pedidos de diferentes períodos e permite avaliar a capacidade de generalização do modelo em dados temporalmente posteriores.

## 7. Pré-processamento

O pré-processamento foi organizado em um pipeline para manter as transformações consistentes entre treinamento e inferência.

As etapas contemplam o tratamento das variáveis numéricas e categóricas, conforme seus respectivos tipos.

O uso de um pipeline integrado permite:

- Aplicar as mesmas transformações durante treinamento e previsão.
- Evitar inconsistências entre os dados utilizados no treinamento e os dados recebidos pela API.
- Centralizar o pré-processamento e o estimador.
- Facilitar a serialização e reutilização do modelo.

## 8. Algoritmos e experimentos

Foram realizados experimentos de modelagem com o objetivo de identificar uma configuração adequada para o problema de classificação.

O modelo selecionado foi o **Random Forest**, utilizando a configuração do experimento 4.

### 8.1 Configuração selecionada

| Parâmetro | Valor |
|---|---|
| Algoritmo | Random Forest |
| `n_estimators` | 100 |
| `max_depth` | 10 |
| `class_weight` | balanced |

A configuração `class_weight="balanced"` foi utilizada para considerar o desbalanceamento entre as classes.

### 8.2 Critério de seleção

A seleção do modelo foi realizada com base no maior valor de F1-score obtido no conjunto de validação.

O F1-score foi considerado por combinar precisão (*precision*) e revocação (*recall*), sendo uma métrica relevante em problemas de classificação com distribuição desigual entre as classes.

## 9. Avaliação do modelo

A avaliação foi realizada utilizando métricas de classificação.

As principais métricas consideradas foram:

- **Accuracy:** proporção total de previsões corretas.
- **Precision:** proporção de previsões positivas que realmente pertencem à classe positiva.
- **Recall:** proporção de exemplos positivos identificados pelo modelo.
- **F1-score:** média harmônica entre precision e recall.
- **ROC-AUC:** capacidade de discriminação entre as classes.

### 9.1 Resultados no conjunto de teste

Os resultados registrados para o modelo selecionado foram:

| Métrica | Resultado |
|---|---:|
| Accuracy | 66,66% |
| Precision | 4,64% |
| Recall | 26,01% |
| F1-score | 0,0787 |
| ROC-AUC | 0,4266 |

### 9.2 Interpretação dos resultados

Os resultados indicam limitações importantes na capacidade de generalização do modelo para o conjunto de teste.

Embora o modelo consiga identificar parte dos pedidos atrasados, a precisão é baixa, indicando uma quantidade elevada de falsos positivos.

O ROC-AUC de 0,4266 também demonstra uma capacidade de discriminação insatisfatória no conjunto de teste.

Esses resultados devem ser considerados na interpretação das previsões apresentadas pela API e pelo frontend.

A implementação demonstra o desenvolvimento completo de um fluxo de Machine Learning, mas os resultados não indicam que o modelo esteja pronto para utilização operacional.

## 10. Artefatos gerados

O pipeline treinado e os resultados da avaliação são armazenados no projeto.

| Artefato | Caminho |
|---|---|
| Base integrada | `data/processed/base_integrada.parquet` |
| Pipeline treinado | `models/delivery_risk_pipeline.joblib` |
| Métricas | `reports/metrics.json` |

O pipeline serializado contém as etapas necessárias para aplicar o pré-processamento e executar as previsões.

Esse artefato é carregado pela API FastAPI durante a inicialização da aplicação.

## 11. Integração com a API

O modelo selecionado é utilizado pela API FastAPI para realizar previsões a partir dos dados recebidos no endpoint `POST /predict`.

Fluxo simplificado:

1. O frontend envia os dados do pedido.
2. A API valida as informações recebidas.
3. O serviço de previsão prepara os dados de entrada.
4. O pipeline carregado executa a previsão.
5. A API organiza o resultado.
6. A previsão é armazenada no histórico.
7. O resultado é retornado ao frontend.

O modelo é carregado durante o ciclo de vida da aplicação e reutilizado nas requisições, evitando carregar o arquivo novamente a cada previsão.

## 12. Limitações conhecidas

A modelagem apresenta limitações que devem ser consideradas:

- O conjunto de dados representa um contexto histórico específico do e-commerce brasileiro.
- A distribuição das classes é desbalanceada.
- O desempenho no conjunto de teste demonstra baixa precisão.
- A capacidade de generalização temporal precisa ser aprimorada.
- O modelo depende da qualidade e da disponibilidade das variáveis de entrada.
- Os resultados são experimentais e não devem ser interpretados como garantia de atraso ou cumprimento do prazo.

## 13. Possíveis melhorias futuras

Como possibilidades de evolução acadêmica e técnica, podem ser consideradas:

- Investigar novas estratégias para lidar com o desbalanceamento das classes.
- Avaliar outros algoritmos de classificação.
- Realizar engenharia de atributos adicional.
- Investigar a importância das variáveis.
- Ajustar hiperparâmetros com validação temporal.
- Avaliar estratégias de calibração de probabilidades.
- Analisar erros e falsos positivos.
- Comparar diferentes limiares de classificação.
- Investigar a estabilidade do modelo em diferentes períodos.

Essas melhorias não fazem parte das entregas obrigatórias já implementadas.

## 14. Status da modelagem

A etapa de modelagem foi implementada e integrada ao restante da aplicação.

- [x] Integração dos conjuntos de dados.
- [x] Construção da variável-alvo.
- [x] Definição dos pedidos elegíveis.
- [x] Seleção das variáveis preditoras.
- [x] Prevenção de vazamento de dados.
- [x] Divisão temporal dos conjuntos.
- [x] Construção do pipeline de pré-processamento.
- [x] Treinamento e comparação de experimentos.
- [x] Seleção do modelo Random Forest.
- [x] Avaliação no conjunto de teste.
- [x] Serialização do pipeline.
- [x] Integração com a API FastAPI.

## 15. Considerações finais

A etapa de modelagem do DeliveryRisk AI contemplou desde a preparação dos dados até a integração do modelo treinado com a API.

O projeto utiliza uma abordagem de classificação supervisionada, com divisão temporal dos dados e cuidados para evitar vazamento de informações.

O Random Forest foi selecionado com base no F1-score de validação e posteriormente avaliado no conjunto de teste.

Apesar das limitações identificadas nos resultados, a implementação atende ao objetivo acadêmico de demonstrar um fluxo estruturado de Machine Learning, integrado a uma API e a uma interface web.