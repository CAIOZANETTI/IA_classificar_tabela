# **Fábrica de Modelos de Previsão de Custos**

Versão: 2.6 (Expandida)  
Data: 2025-07-10  
Autor: Caio M. Zanetti

## **Índice**

1. [Visão Geral e Objetivo Estratégico](https://www.google.com/search?q=%231-vis%C3%A3o-geral-e-objetivo-estrat%C3%A9gico)  
2. [Arquitetura de Dados em Camadas](https://www.google.com/search?q=%232-arquitetura-de-dados-em-camadas)  
3. [Fase 1: Módulo de Ingestão e Harmonização de Dados (Camada Processed)](https://www.google.com/search?q=%233-fase-1-m%C3%B3dulo-de-ingest%C3%A3o-e-harmoniza%C3%A7%C3%A3o-de-dados-camada-processed)  
   * [3.1. Schema Mestre](https://www.google.com/search?q=%2331-schema-mestre)  
   * [3.2. Processo de Transformação e Empilhamento](https://www.google.com/search?q=%2332-processo-de-transforma%C3%A7%C3%A3o-e-empilhamento)  
   * [3.3. Teste de Validação da Fase 1](https://www.google.com/search?q=%2333-teste-de-valida%C3%A7%C3%A3o-da-fase-1)  
4. [Fase 2: Módulo de Engenharia de Features Adaptativa (Camada Feature Store)](https://www.google.com/search?q=%234-fase-2-m%C3%B3dulo-de-engenharia-de-features-adaptativa-camada-feature-store)  
   * [4.1. Estrutura do Módulo](https://www.google.com/search?q=%2341-estrutura-do-m%C3%B3dulo)  
   * [4.2. Pipeline de Features Detalhado](https://www.google.com/search?q=%2342-pipeline-de-features-detalhado)  
   * [4.3. Teste de Validação da Fase 2](https://www.google.com/search?q=%2343-teste-de-valida%C3%A7%C3%A3o-da-fase-2)  
5. [Fase 3: A "Fábrica de Modelos" (Treinamento e Avaliação)](https://www.google.com/search?q=%235-fase-3-a-f%C3%A1brica-de-modelos-treinamento-e-avalia%C3%A7%C3%A3o)  
   * [5.1. Lógica da Fábrica](https://www.google.com/search?q=%2351-l%C3%B3gica-da-f%C3%A1brica)  
   * [5.2. Teste de Validação da Fase 3](https://www.google.com/search?q=%2352-teste-de-valida%C3%A7%C3%A3o-da-fase-3)  
6. [Fase 4: Aplicação Interativa com Streamlit](https://www.google.com/search?q=%236-fase-4-aplica%C3%A7%C3%A3o-interativa-com-streamlit)  
   * [6.1. Estrutura da Aplicação](https://www.google.com/search?q=%2361-estrutura-da-aplica%C3%A7%C3%A3o)  
   * [6.2. Teste de Validação da Fase 4](https://www.google.com/search?q=%2362-teste-de-valida%C3%A7%C3%A3o-da-fase-4)  
7. [Configuração e Boas Práticas](https://www.google.com/search?q=%237-configura%C3%A7%C3%A3o-e-boas-pr%C3%A1ticas)  
8. [Propósito, Uso e Evolução do Projeto](https://www.google.com/search?q=%238-prop%C3%B3sito-uso-e-evolu%C3%A7%C3%A3o-do-projeto)  
   * [8.1. Para que Serve Tudo Isso? (O Propósito)](https://www.google.com/search?q=%2381-para-que-serve-tudo-isso-o-prop%C3%B3sito)  
   * [8.2. Como Eu Uso a Ferramenta Hoje? (Casos de Uso)](https://www.google.com/search?q=%2382-como-eu-uso-a-ferramenta-hoje-casos-de-uso)  
   * [8.3. O que Dá para Fazer Agora? (Capacidades Atuais)](https://www.google.com/search?q=%2383-o-que-d%C3%A1-para-fazer-agora-capacidades-atuais)  
   * [8.4. Esclarecendo Limitações e Casos de Uso Específicos](https://www.google.com/search?q=%2384-esclarecendo-limita%C3%A7%C3%B5es-e-casos-de-uso-espec%C3%ADficos)  
   * [8.5. E Agora? O Roadmap de Evolução](https://www.google.com/search?q=%2385-e-agora-o-roadmap-de-evolu%C3%A7%C3%A3o)  
9. [Manuais de Uso](https://www.google.com/search?q=%239-manuais-de-uso)  
   * [9.1. Manual do Usuário Final (Aplicação Streamlit)](https://www.google.com/search?q=%2391-manual-do-usu%C3%A1rio-final-aplica%C3%A7%C3%A3o-streamlit)  
   * [9.2. Manual do Desenvolvedor (Uso via Código para Lotes)](https://www.google.com/search?q=%2392-manual-do-desenvolvedor-uso-via-c%C3%B3digo-para-lotes)  
10. [Backlog de Desenvolvimento e Controle de Status](https://www.google.com/search?q=%2310-backlog-de-desenvolvimento-e-controle-de-status)

## **1\. Visão Geral e Objetivo Estratégico**

Este documento detalha a arquitetura e os requisitos para a construção de um sistema automatizado, apelidado de **"Fábrica de Modelos"**, para a previsão de custos de **insumos e serviços** da construção civil.

O objetivo final é transcender a criação de um único modelo e estabelecer um pipeline escalável e de fácil manutenção que:

1. Ingere e harmoniza dados de múltiplas fontes (SINAPI, TCPO, etc.), **respeitando e registrando a temporalidade de cada fonte**.  
2. Identifica inteligentemente "famílias" de itens.  
3. Aplica engenharia de features adaptativa para cada família.  
4. Treina, avalia e armazena um modelo de Machine Learning **especialista** para cada família.  
5. Disponibiliza esses especialistas para previsões através de uma **aplicação web interativa construída com Streamlit**.

Este escopo servirá como um guia técnico completo para o desenvolvimento.

## **2\. Arquitetura de Dados em Camadas**

Para garantir organização, rastreabilidade e eficiência, o projeto adotará uma arquitetura de dados em múltiplas camadas, uma prática moderna de engenharia de dados.

* **Camada Raw (data/raw/):** Ponto de entrada do sistema. Contém os arquivos originais e imutáveis das fontes de dados (SINAPI, TCPO, etc.) exatamente como foram recebidos.  
* **Camada Processed (data/processed/):** O resultado da Fase 1\. Contém o catalogo\_harmonizado.parquet, que é a nossa fonte única da verdade ("Single Source of Truth"), com dados limpos, padronizados, unificados e enriquecidos.  
* **Camada Feature Store (data/feature\_store/):** O resultado da Fase 2\. Contém datasets prontos para o treinamento, um para cada família (ex: tubo\_features.parquet). Esta camada desacopla a engenharia de features do treinamento, permitindo que os modelos sejam retreinados rapidamente sem a necessidade de reprocessar as features.  
* **Armazenamento de Modelos (models/):** Contém os artefatos finais do modelo.  
  * models/staging/: Área temporária onde todos os modelos treinados e seus metadados são salvos após a execução da Fase 3\.  
  * models/approved/: Diretório final. Apenas os modelos que passam nos testes de validação da Fase 3 são movidos para cá. A aplicação Streamlit **somente** lerá os modelos deste diretório, garantindo que apenas modelos de qualidade sejam expostos ao usuário.

## **3\. Fase 1: Módulo de Ingestão e Harmonização de Dados (Camada Processed)**

Diretório: src/data/  
Script Principal: harmonizacao.py  
**Objetivo:** Criar um processo de ETL (Extração, Transformação e Carga) robusto que unifica dados da camada **Raw** e os salva na camada **Processed**.

### **3.1. Schema Mestre**

Todos os dados processados devem ser conformados à seguinte estrutura, a ser salva em um arquivo Parquet (data/processed/catalogo\_harmonizado.parquet):

| Nome da Coluna | Tipo de Dado | Descrição | Exemplo |
| :---- | :---- | :---- | :---- |
| id\_item | string | ID original do item na fonte. | SINAPI-88308 |
| descricao\_item | string | Descrição completa, limpa e normalizada. | tubo pvc esgoto dn 100mm |
| unidade\_padrao | string | **Unidade de medida padronizada e consolidada.** | un |
| custo\_referencia | float64 | Custo unitário do item (insumo ou serviço). | 15.78 |
| data\_referencia | datetime64\[ns\] | Data de vigência do custo. | 2025-05-01 |
| fonte\_dados | string | Identificador da tabela de origem. | sinapi |
| tipo\_item | string | Classificação do item como 'insumo' ou 'servico'. | insumo |
| familia\_item | string | Categoria de alto nível do item. | tubo |

### **3.2. Processo de Transformação e Empilhamento**

O script harmonizacao.py implementará a lógica para ler, limpar, transformar e empilhar os dados.

1. **Geração de Template de Mapeamento (Helper Script):**  
   * Um script auxiliar src/config/generate\_mapping\_template.py será criado. Sua função é ler o cabeçalho de um arquivo de dados brutos (ex: sinapi\_insumos\_05\_2025.xlsx) e gerar um template data\_mapping.json com os nomes das colunas originais. **Este template será então preenchido manualmente pelo usuário (Caio) para definir o mapeamento correto.**  
2. **Execução Principal (Orquestrador):**  
   * O script principal irá escanear o diretório data/raw/ por arquivos com nomes padronizados.  
   * Para cada arquivo, ele identificará a fonte, o tipo e a data a partir do nome do arquivo e chamará a função de processamento específica.  
   * Cada função de processamento retornará um DataFrame já no **Schema Mestre**.  
   * O orquestrador irá coletar todos esses DataFrames em uma lista e, ao final, usará pd.concat() para "empilhá-los" em um único DataFrame mestre.  
   * Este DataFrame mestre será então salvo como catalogo\_harmonizado.parquet na camada processed.  
3. **Funções de Processamento por Fonte (Exemplo Detalhado):**  
   * **def processar\_sinapi(caminho\_arquivo, tipo\_de\_item):**  
     * **a. Leitura:** Carrega a planilha.  
     * **b. Mapeamento de Colunas:** Renomeia as colunas conforme config/data\_mapping.json.  
     * **c. Limpeza e Normalização de Texto:** Converte para minúsculas, remove acentos e espaços extras.  
     * **d. Padronização de Unidades:** Aplica o mapeamento de unidades definido no data\_mapping.json.  
     * **e. Tratamento de Tipos de Dados e Temporalidade:** Converte custo\_referencia para float, extrai data\_referencia do nome do arquivo e cria os IDs.  
     * **f. Identificação da Família:** Usa a regra da "primeira palavra" como principal identificador, com fallback para a segunda palavra.  
     * **g. Validação e Retorno:** Verifica a conformidade com o Schema Mestre e o retorna.

### **3.3. Teste de Validação da Fase 1**

* **Objetivo:** Garantir que o processo de harmonização gerou um arquivo de saída válido e consistente.  
* **Critérios de Sucesso:**  
  1. Existência do arquivo data/processed/catalogo\_harmonizado.parquet.  
  2. Validação do Schema (colunas e tipos de dados).  
  3. Validação de Conteúdo (sem nulos em colunas críticas, sem unidades não padronizadas).  
* **Resultado:** O teste classifica a etapa como **Aprovada** ou **Reprovada**.

## **4\. Fase 2: Módulo de Engenharia de Features Adaptativa (Camada Feature Store)**

Diretório: src/features/  
Script Principal: engenharia\_features.py  
**Objetivo:** Ler os dados da camada **Processed**, criar as features para cada família e salvar os resultados na camada **Feature Store**.

### **4.1. Estrutura do Módulo**

O script deve conter uma função principal criar\_features(df\_familia, nome\_familia) que orquestra a criação de features.

### **4.2. Pipeline de Features Detalhado**

1. **Tratamento de Features Categóricas Comuns:**  
   * Converte unidade\_padrao e tipo\_item em colunas binárias usando One-Hot Encoding.  
2. **Extração de Features Técnicas (Baseada em Regras):**  
   * A função extrair\_features\_especificas aplicará regras de extração com base na família do item. A extração resultará em NaN se o padrão não for encontrado.  
   * **Modo de Segurança:** Se uma família não tiver regras de extração de features definidas no script, a função registrará um aviso e retornará o DataFrame sem novas features técnicas. O treinamento para esta família será pulado na Fase 3\.  
3. **Análise de Palavras-Chave Descritivas (Baseada em Impacto):**  
   * A função analisar\_palavras\_chave irá capturar sinais de custo adicionais de palavras descritivas.  
4. **Orquestração em criar\_features:**  
   * Executa os passos acima para retornar os DataFrames X e y.

### **4.3. Teste de Validação da Fase 2**

* **Objetivo:** Garantir que a engenharia de features produziu DataFrames válidos.  
* **Critérios de Sucesso:**  
  1. X e y são DataFrames/Séries do Pandas.  
  2. Todas as colunas em X são numéricas (com exceção dos NaN esperados).  
  3. y não contém valores nulos.  
  4. len(X) \== len(y).  
* **Resultado:** O teste classifica a etapa como **Aprovada** ou **Reprovada**.

## **5\. Fase 3: A "Fábrica de Modelos" (Treinamento e Avaliação)**

Diretório: src/training/  
Script Principal: fabrica\_modelos.py  
**Objetivo:** Automatizar o ciclo completo de treinamento, avaliação e armazenamento para cada modelo especialista, lendo da camada **Feature Store** e salvando na camada de **Modelos**.

### **5.1. Lógica da Fábrica**

O script fabrica\_modelos.py deve:

1. Carregar catalogo\_harmonizado.parquet.  
2. Iterar sobre cada familia\_item única.  
3. Para cada família:  
   a. Filtrar Dados: Criar um df\_familia.  
   b. Limiar de Dados: Verificar se len(df\_familia) \> 100\.  
   c. Engenharia de Features: Chamar criar\_features para obter X e y. O resultado (X e y combinados) será salvo em data/feature\_store/{familia}\_features.parquet.  
   d. Filtragem de Dados Incompletos: Remover linhas onde as features técnicas críticas (definidas em config/critical\_features.json) forem nulas.  
   e. Divisão (Aleatória):  
   \- Processo: Usar a função padrão train\_test\_split do Scikit-learn para uma divisão aleatória de 80/20. A validação temporal será considerada uma evolução futura.  
   f. Transformação do Alvo (CRÍTICO):  
   \- Processo: Aplicar a transformação logarítmica: y\_train\_log \= np.log1p(y\_train).  
   g. Treinamento:  
   \- Instanciar e treinar RandomForestRegressor com (X\_train, y\_train\_log).  
   h. Avaliação Detalhada:  
   \- Fazer previsões em X\_test e reverter a transformação logarítmica para obter previsoes\_final.  
   \- Criar o Relatório de Validação detalhado.  
   i. Cálculo de Métricas Agregadas: Calcular MAE, R² e a Taxa de Aceitação.  
   j. Armazenamento de Artefatos: Salvar o modelo, metadados, importância das features e relatórios no diretório models/staging/.

### **5.2. Teste de Validação da Fase 3**

* **Objetivo:** Garantir que o modelo treinado atende aos critérios mínimos de performance para ser promovido.  
* **Execução:** Após o armazenamento em staging, um processo de validação será executado.  
* **Critérios de Sucesso (Configuráveis):**  
  1. Existência de todos os artefatos em staging.  
  2. r2\_score \> 0.70 e taxa\_aceitacao\_percentual \> 80.0.  
* **Resultado:** Se aprovado, os artefatos do modelo são movidos de models/staging/ para models/approved/. Caso contrário, permanecem em staging para análise e não são disponibilizados.

## **6\. Fase 4: Aplicação Interativa com Streamlit**

Diretório: src/app/  
Script Principal: app.py  
**Objetivo:** Criar uma interface web interativa para que usuários finais possam explorar os modelos, fazer previsões e analisar a performance.

### **6.1. Estrutura da Aplicação**

A aplicação Streamlit será multipágina e **lerá os modelos exclusivamente do diretório models/approved/**:

1. **Página Principal: "Dashboard da Fábrica"**: Mostra métricas globais e uma tabela de modelos aprovados.  
2. **Página: "Simulador de Custos"**:  
   * **Input do Usuário:** Um st.text\_area para a **descrição** e um st.text\_input para a **unidade**.  
   * **Lógica:** Identifica a família, carrega o modelo aprovado, executa o pipeline de features, faz a previsão (em log) e reverte a transformação (np.expm1) para exibir o custo final.  
3. **Página: "Análise de Performance por Família"**: Permite selecionar um modelo aprovado e visualizar suas métricas, gráfico de dispersão, tabela de desvios e um gráfico de barras com as features mais importantes.

### **6.2. Teste de Validação da Fase 4**

* **Objetivo:** Garantir que a aplicação Streamlit está funcional.  
* **Critérios de Sucesso:**  
  1. Aplicação inicia sem erros.  
  2. Dashboard carrega os dados corretamente.  
  3. Simulador retorna uma previsão numérica válida.  
  4. Página de análise exibe todos os gráficos e tabelas.  
* **Resultado:** O teste classifica a aplicação como **Pronta para o Usuário** ou **Com Bugs**.

## **7\. Configuração e Boas Práticas**

* **Gerenciamento de Dependências (requirements.txt):** Um arquivo requirements.txt deve listar todas as bibliotecas necessárias para o projeto.

| Pacote | Versão Sugerida | Função Principal no Projeto |
| :---- | :---- | :---- |
| pandas | \~=2.2.0 | Espinha dorsal para manipulação de dados em tabelas (DataFrames). |
| numpy | \~=1.26.0 | Essencial para cálculos numéricos, especialmente a transformação logarítmica. |
| scikit-learn | \~=1.4.0 | Caixa de ferramentas de Machine Learning (modelo, divisão de dados, métricas). |
| streamlit | \~=1.36.0 | Framework para construir a aplicação web interativa da Fase 4\. |
| matplotlib | \~=3.8.0 | Utilizado para gerar os gráficos de análise de performance no Streamlit. |
| pyarrow | \~=16.1.0 | Motor de alta performance para o Pandas ler e escrever arquivos .parquet. |
| openpyxl | \~=3.1.0 | Dependência para o Pandas poder ler arquivos do Excel (.xlsx). |
| joblib | \~=1.4.0 | Forma padrão e eficiente de salvar e carregar os modelos treinados. |
| PyYAML | \~=6.0.1 | Para carregar os arquivos de configuração .yaml (como o settings.yaml). |

* **Configuração Centralizada:** Arquivos .json e .yaml no diretório config/ para parâmetros de negócio e de modelo, evitando hardcoding.  
* **Logging:** Implementar logging em todos os scripts para registrar o progresso, avisos e erros, facilitando a depuração da "Fábrica".  
* **Estrutura de Diretórios Esperada:**  
  .  
  ├── config/  
  │   ├── data\_mapping.json  
  │   ├── critical\_features.json  
  │   └── settings.yaml  
  ├── data/  
  │   ├── raw/  
  │   ├── processed/  
  │   └── feature\_store/  
  ├── models/  
  │   ├── staging/  
  │   └── approved/  
  ├── notebooks/  
  ├── reports/  
  ├── src/  
  │   ├── app/  
  │   │   └── app.py  
  │   ├── data/  
  │   │   └── harmonizacao.py  
  │   ├── features/  
  │   │   └── engenharia\_features.py  
  │   └── training/  
  │       └── fabrica\_modelos.py  
  ├── tests/  
  │   ├── test\_harmonizacao.py  
  │   └── (outros scripts de teste)  
  ├── ESCOPO.md  
  └── requirements.txt

## **8\. Propósito, Uso e Evolução do Projeto**

### **8.1. Para que Serve Tudo Isso? (O Propósito)**

O objetivo desta ferramenta é transformar o processo de orçamentação na construção civil, saindo de um modelo manual, lento e sujeito a inconsistências para um **sistema de suporte à decisão rápido, consistente e orientado por dados**.

A "Fábrica de Modelos" não é apenas um preditor de preços, mas uma plataforma que:

* **Centraliza o Conhecimento:** Consolida múltiplas tabelas de referência em uma base de dados única e padronizada.  
* **Automatiza a Inteligência:** Cria e mantém modelos especialistas para diferentes categorias de insumos, garantindo alta precisão.  
* **Democratiza o Acesso:** Oferece uma interface simples (via Streamlit) para que orçamentistas, engenheiros e gestores possam obter estimativas de custo confiáveis em segundos.  
* **Promove a Transparência:** Permite que os usuários não apenas vejam a previsão, mas também entendam a performance e a confiabilidade de cada modelo.

### **8.2. Como Eu Uso a Ferramenta Hoje? (Casos de Uso)**

O uso principal é através da aplicação Streamlit, que oferece três funcionalidades chave:

1. **Para uma visão geral (Dashboard da Fábrica):** Você pode rapidamente ver quais "famílias" de insumos já possuem um modelo de previsão confiável, qual a precisão de cada um e quando foram treinados.  
2. **Para uma estimativa rápida (Simulador de Custos):** Você simplesmente digita a descrição de um insumo que precisa orçar (ex: "concreto fck 25mpa bombeavel") e a ferramenta te dá um preço estimado instantaneamente, usando o modelo especialista apropriado.  
3. **Para uma análise profunda (Análise de Performance):** Se você quiser entender o quão confiável é o modelo para "concreto", pode ir a esta página, ver o gráfico de erros e até mesmo a tabela com todas as previsões de teste, comparando o valor real com o previsto.

### **8.3. O que Dá para Fazer Agora? (Capacidades Atuais)**

* **Estimar custos de insumos e serviços** para qualquer família que tenha um modelo treinado e aprovado.  
* **Avaliar a confiabilidade** de cada modelo especialista através de métricas claras (R², MAE, Taxa de Aceitação).  
* **Explorar visualmente** os erros e acertos de cada modelo.  
* **Automatizar o retreinamento** de todos os modelos simplesmente adicionando novas planilhas de referência na pasta data/raw/ e executando o script da "Fábrica".

### **8.4. Esclarecendo Limitações e Casos de Uso Específicos**

* **"Esta ferramenta avalia ou estima o custo de um serviço?"**  
  * **Sim.** O sistema foi explicitamente projetado para isso. Um serviço como "escavação manual de vala" ou "pintura latex" será tratado como uma familia\_item e terá seu próprio modelo especialista.  
* **"Se eu inputar uma planilha vazia, ela coloca os custos?"**  
  * **Não na versão atual.** A aplicação Streamlit foi projetada para previsões **item a item**. Ela não possui uma funcionalidade de "upload de planilha para preenchimento em lote". Esta é uma excelente ideia para uma evolução futura.

### **8.5. E Agora? O Roadmap de Evolução**

A plataforma foi projetada para ser modular, permitindo futuras expansões. O roadmap de evolução inclui:

1. **Previsão em Lote:** Permitir o upload de planilhas para orçamentação em massa.  
2. **Análise de Tendência de Custos:** Usar a data\_referencia para visualizar a evolução dos custos.  
3. **Validação Temporal:** Implementar a estratégia de divisão de dados temporal (treino com dados antigos, teste com recentes) para uma avaliação mais rigorosa.  
4. **Modelo de Previsão de Composições (CPU):** Prever o custo de um serviço completo a partir de seus insumos.  
5. **Otimização de Hiperparâmetros:** Usar GridSearchCV para refinar cada modelo.  
6. **Integração com Bancos de Dados:** Migrar o armazenamento para um sistema mais robusto.  
7. **Evolução para uma Plataforma Genérica de IA:** Transformar a "Fábrica de Modelos" em uma plataforma AutoML mais versátil, capaz de resolver diferentes tipos de problemas de negócio, incluindo geração de texto.

## **9\. Manuais de Uso**

### **9.1. Manual do Usuário Final (Aplicação Streamlit)**

Este guia destina-se a usuários como orçamentistas, engenheiros e gestores que irão interagir com a aplicação web.

**Objetivo:** Obter uma estimativa de custo para um insumo ou serviço de forma rápida.

**Passo a Passo:**

1. **Acesse a Aplicação** e navegue para **"Simulador de Custos"**.  
2. **Descreva o Item:** Nos campos apropriados, digite a **descrição** detalhada e a **unidade** de medida.  
3. **Execute a Previsão:** Clique em **"Estimar Custo"**.  
4. **Analise o Resultado:** A aplicação exibirá a família identificada e o custo estimado.

### **9.2. Manual do Desenvolvedor (Uso via Código para Lotes)**

**Objetivo:** Obter previsões para uma lista de itens programaticamente.

**Contexto:** As funções modulares do projeto podem ser importadas e usadas em outros scripts para automação.

**Exemplo de Script batch\_prediction.py:**

import pandas as pd  
import joblib  
import re  
import numpy as np  
from pathlib import Path

\# ... (código do script de lote, que agora receberia descrição e unidade) ...

## **10\. Backlog de Desenvolvimento e Controle de Status**

**Objetivo:** Manter um registro claro e atualizado do progresso do desenvolvimento. Este backlog deve ser usado como uma ferramenta de gerenciamento, onde o status de cada componente é atualizado à medida que o código correspondente é implementado e testado.

**Instrução para a IA de Codificação:** Ao implementar uma das tarefas abaixo, por favor, atualize o status nesta tabela na próxima interação.

| Fase | Componente / Tarefa | Status | Versão Implementada | Data de Conclusão |
| :---- | :---- | :---- | :---- | :---- |
| **Config** | Estrutura de diretórios e arquivos de configuração | Pendente | \- | \- |
| **Config** | Script generate\_mapping\_template.py | Pendente | \- | \- |
| **Análise** | Script discover\_critical\_features.py | Pendente | \- | \- |
| **Fase 1** | Script de Harmonização (harmonizacao.py) | Pendente | \- | \- |
| **Fase 1** | Teste de Validação (test\_harmonizacao.py) | Pendente | \- | \- |
| **Fase 2** | Script de Engenharia de Features (engenharia\_features.py) | Pendente | \- | \- |
| **Fase 3** | Script da Fábrica de Modelos (fabrica\_modelos.py) | Pendente | \- | \- |
| **Fase 4** | Aplicação Streamlit (app.py) | Pendente | \- | \- |
| **Doc** | Documentação e Manuais (este arquivo) | Em Progresso | 2.6 | \- |

