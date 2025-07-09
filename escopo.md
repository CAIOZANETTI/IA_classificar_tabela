# **Fábrica de Modelos de Previsão de Custos 2.5**

Versão: 2.5 (Final para Implementação Inicial)  
Data: 2025-07-09  
Autor: Caio M. Zanetti

## **Índice**

1. [Visão Geral e Objetivo Estratégico](https://www.google.com/search?q=%231-vis%C3%A3o-geral-e-objetivo-estrat%C3%A9gico)  
2. [Fase 1: Módulo de Ingestão e Harmonização de Dados](https://www.google.com/search?q=%232-fase-1-m%C3%B3dulo-de-ingest%C3%A3o-e-harmoniza%C3%A7%C3%A3o-de-dados)  
   * [2.1. Schema Mestre](https://www.google.com/search?q=%2321-schema-mestre)  
   * [2.2. Processo de Transformação e Empilhamento](https://www.google.com/search?q=%2322-processo-de-transforma%C3%A7%C3%A3o-e-empilhamento)  
   * [2.3. Teste de Validação da Fase 1](https://www.google.com/search?q=%2323-teste-de-valida%C3%A7%C3%A3o-da-fase-1)  
3. [Fase 2: Módulo de Engenharia de Features Adaptativa](https://www.google.com/search?q=%233-fase-2-m%C3%B3dulo-de-engenharia-de-features-adaptativa)  
   * [3.1. Estrutura do Módulo](https://www.google.com/search?q=%2331-estrutura-do-m%C3%B3dulo)  
   * [3.2. Pipeline de Features Detalhado](https://www.google.com/search?q=%2332-pipeline-de-features-detalhado)  
   * [3.3. Teste de Validação da Fase 2](https://www.google.com/search?q=%2333-teste-de-valida%C3%A7%C3%A3o-da-fase-2)  
4. [Fase 3: A "Fábrica de Modelos" (Treinamento e Avaliação)](https://www.google.com/search?q=%234-fase-3-a-f%C3%A1brica-de-modelos-treinamento-e-avalia%C3%A7%C3%A3o)  
   * [4.1. Lógica da Fábrica](https://www.google.com/search?q=%2341-l%C3%B3gica-da-f%C3%A1brica)  
   * [4.2. Teste de Validação da Fase 3](https://www.google.com/search?q=%2342-teste-de-valida%C3%A7%C3%A3o-da-fase-3)  
5. [Fase 4: Aplicação Interativa com Streamlit](https://www.google.com/search?q=%235-fase-4-aplica%C3%A7%C3%A3o-interativa-com-streamlit)  
   * [5.1. Estrutura da Aplicação](https://www.google.com/search?q=%2351-estrutura-da-aplica%C3%A7%C3%A3o)  
   * [5.2. Teste de Validação da Fase 4](https://www.google.com/search?q=%2352-teste-de-valida%C3%A7%C3%A3o-da-fase-4)  
6. [Configuração e Boas Práticas](https://www.google.com/search?q=%236-configura%C3%A7%C3%A3o-e-boas-pr%C3%A1ticas)  
7. [Propósito, Uso e Evolução do Projeto](https://www.google.com/search?q=%237-prop%C3%B3sito-uso-e-evolu%C3%A7%C3%A3o-do-projeto)  
   * [7.1. Para que Serve Tudo Isso? (O Propósito)](https://www.google.com/search?q=%2371-para-que-serve-tudo-isso-o-prop%C3%B3sito)  
   * [7.2. Como Eu Uso a Ferramenta Hoje?](https://www.google.com/search?q=%2372-como-eu-uso-a-ferramenta-hoje)  
   * [7.3. O que Dá para Fazer Agora? (Capacidades Atuais)](https://www.google.com/search?q=%2373-o-que-d%C3%A1-para-fazer-agora-capacidades-atuais)  
   * [7.4. Esclarecendo Casos de Uso Específicos](https://www.google.com/search?q=%2374-esclarecendo-casos-de-uso-espec%C3%ADficos)  
   * [7.5. E Agora? Quais os Objetivos Futuros?](https://www.google.com/search?q=%2375-e-agora-quais-os-objetivos-futuros)  
8. [Manuais de Uso](https://www.google.com/search?q=%238-manuais-de-uso)  
   * [8.1. Manual do Usuário Final (Aplicação Streamlit)](https://www.google.com/search?q=%2381-manual-do-usu%C3%A1rio-final-aplica%C3%A7%C3%A3o-streamlit)  
   * [8.2. Manual do Desenvolvedor (Uso via Código para Lotes)](https://www.google.com/search?q=%2382-manual-do-desenvolvedor-uso-via-c%C3%B3digo-para-lotes)  
9. [Backlog de Desenvolvimento e Controle de Status](https://www.google.com/search?q=%239-backlog-de-desenvolvimento-e-controle-de-status)

## **1\. Visão Geral e Objetivo Estratégico**

Este documento detalha a arquitetura e os requisitos para a construção de um sistema automatizado, apelidado de **"Fábrica de Modelos"**, para a previsão de custos de **insumos e serviços** da construção civil.

O objetivo final é transcender a criação de um único modelo e estabelecer um pipeline escalável e de fácil manutenção que:

1. Ingere e harmoniza dados de múltiplas fontes (SINAPI, TCPO, etc.), **respeitando e registrando a temporalidade de cada fonte**.  
2. Identifica inteligentemente "famílias" de itens.  
3. Aplica engenharia de features adaptativa para cada família.  
4. Treina, avalia e armazena um modelo de Machine Learning **especialista** para cada família.  
5. Disponibiliza esses especialistas para previsões através de uma **aplicação web interativa construída com Streamlit**.

Este escopo servirá como um guia técnico completo para o desenvolvimento.

## **2\. Fase 1: Módulo de Ingestão e Harmonização de Dados**

Diretório: src/data/  
Script Principal: harmonizacao.py  
**Objetivo:** Criar um processo de ETL (Extração, Transformação e Carga) robusto que unifica dados de fontes heterogêneas em um **Schema Mestre** padronizado, permitindo o "empilhamento" de múltiplas fontes de dados de diferentes períodos para alimentar os modelos.

### **2.1. Schema Mestre**

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

### **2.2. Processo de Transformação e Empilhamento**

O script harmonizacao.py implementará a lógica para ler, limpar, transformar e empilhar os dados.

1. **Geração de Template de Mapeamento (Helper Script):**  
   * Um script auxiliar src/config/generate\_mapping\_template.py será criado. Sua função é ler o cabeçalho de um arquivo de dados brutos (ex: sinapi\_insumos\_05\_2025.xlsx) e gerar um template data\_mapping.json com os nomes das colunas originais. **Este template será então preenchido manualmente pelo usuário (Caio) para definir o mapeamento correto.**  
2. **Execução Principal (Orquestrador):**  
   * O script principal irá escanear o diretório data/raw/ por arquivos com nomes padronizados.  
   * Para cada arquivo, ele identificará a fonte, o tipo e a data a partir do nome do arquivo e chamará a função de processamento específica.  
   * Cada função de processamento retornará um DataFrame já no **Schema Mestre**.  
   * O orquestrador irá coletar todos esses DataFrames em uma lista e, ao final, usará pd.concat() para "empilhá-los" em um único DataFrame mestre.  
   * Este DataFrame mestre será então salvo como catalogo\_harmonizado.parquet.  
3. **Funções de Processamento por Fonte (Exemplo Detalhado):**  
   * **def processar\_sinapi(caminho\_arquivo, tipo\_de\_item):**  
     * **a. Leitura:** Carrega a planilha.  
     * **b. Mapeamento de Colunas:** Renomeia as colunas conforme config/data\_mapping.json.  
     * **c. Limpeza e Normalização de Texto:** Converte para minúsculas, remove acentos e espaços extras.  
     * **d. Padronização de Unidades:** Aplica o mapeamento de unidades definido no data\_mapping.json.  
     * **e. Tratamento de Tipos de Dados e Temporalidade:** Converte custo\_referencia para float, extrai data\_referencia do nome do arquivo e cria os IDs.  
     * **f. Identificação da Família:** Usa a regra da "primeira palavra" como principal identificador, com fallback para a segunda palavra.  
     * **g. Validação e Retorno:** Verifica a conformidade com o Schema Mestre e o retorna.

### **2.3. Teste de Validação da Fase 1**

* **Objetivo:** Garantir que o processo de harmonização gerou um arquivo de saída válido e consistente.  
* **Critérios de Sucesso:**  
  1. Existência do arquivo catalogo\_harmonizado.parquet.  
  2. Validação do Schema (colunas e tipos de dados).  
  3. Validação de Conteúdo (sem nulos em colunas críticas, sem unidades não padronizadas).  
* **Resultado:** O teste classifica a etapa como **Aprovada** ou **Reprovada**.

## **3\. Fase 2: Módulo de Engenharia de Features Adaptativa**

Diretório: src/features/  
Script Principal: engenharia\_features.py  
**Objetivo:** Transformar os dados textuais e categóricos de cada família em um conjunto rico de features numéricas que o modelo possa entender.

### **3.1. Estrutura do Módulo**

O script deve conter uma função principal criar\_features(df\_familia, nome\_familia) que orquestra a criação de features.

### **3.2. Pipeline de Features Detalhado**

1. **Tratamento de Features Categóricas Comuns:**  
   * Converte unidade\_padrao e tipo\_item em colunas binárias usando One-Hot Encoding.  
2. **Extração de Features Técnicas (Baseada em Regras):**  
   * A função extrair\_features\_especificas aplicará regras de extração com base na família do item. A extração resultará em NaN se o padrão não for encontrado.  
   * **Modo de Segurança:** Se uma família não tiver regras de extração de features definidas no script, a função registrará um aviso e retornará o DataFrame sem novas features técnicas. O treinamento para esta família será pulado na Fase 3\.  
3. **Análise de Palavras-Chave Descritivas (Baseada em Impacto):**  
   * A função analisar\_palavras\_chave irá capturar sinais de custo adicionais de palavras descritivas.  
4. **Orquestração em criar\_features:**  
   * Executa os passos acima para retornar os DataFrames X e y.

### **3.3. Teste de Validação da Fase 2**

* **Objetivo:** Garantir que a engenharia de features produziu DataFrames válidos.  
* **Critérios de Sucesso:**  
  1. X e y são DataFrames/Séries do Pandas.  
  2. Todas as colunas em X são numéricas (com exceção dos NaN esperados).  
  3. y não contém valores nulos.  
  4. len(X) \== len(y).  
* **Resultado:** O teste classifica a etapa como **Aprovada** ou **Reprovada**.

## **4\. Fase 3: A "Fábrica de Modelos" (Treinamento e Avaliação)**

Diretório: src/training/  
Script Principal: fabrica\_modelos.py  
**Objetivo:** Automatizar o ciclo completo de treinamento, avaliação e armazenamento para cada modelo especialista.

### **4.1. Lógica da Fábrica**

O script fabrica\_modelos.py deve:

1. Carregar catalogo\_harmonizado.parquet.  
2. Iterar sobre cada familia\_item única.  
3. Para cada família:  
   a. Filtrar Dados: Criar um df\_familia.  
   b. Limiar de Dados: Verificar se len(df\_familia) \> 100\.  
   c. Engenharia de Features: Chamar criar\_features.  
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
   j. Armazenamento de Artefatos: Salvar o modelo, metadados, importância das features e relatórios.

### **4.2. Teste de Validação da Fase 3**

* **Objetivo:** Garantir que o modelo treinado atende aos critérios mínimos de performance.  
* **Critérios de Sucesso (Configuráveis):**  
  1. Existência de todos os artefatos.  
  2. r2\_score \> 0.70 e taxa\_aceitacao\_percentual \> 80.0.  
* **Resultado:** O modelo é marcado como **Aprovado para Implantação** ou **Reprovado**.

## **5\. Fase 4: Aplicação Interativa com Streamlit**

Diretório: src/app/  
Script Principal: app.py  
**Objetivo:** Criar uma interface web interativa para que usuários finais possam explorar os modelos, fazer previsões e analisar a performance.

### **5.1. Estrutura da Aplicação**

A aplicação Streamlit será multipágina:

1. **Página Principal: "Dashboard da Fábrica"**: Mostra métricas globais e uma tabela de modelos aprovados.  
2. **Página: "Simulador de Custos"**:  
   * **Input do Usuário:** Um st.text\_area para a **descrição** e um st.text\_input para a **unidade**.  
   * **Lógica:** Identifica a família, carrega o modelo aprovado, executa o pipeline de features, faz a previsão (em log) e reverte a transformação (np.expm1) para exibir o custo final.  
3. **Página: "Análise de Performance por Família"**: Permite selecionar um modelo aprovado e visualizar suas métricas, gráfico de dispersão, tabela de desvios e um gráfico de barras com as features mais importantes.

### **5.2. Teste de Validação da Fase 4**

* **Objetivo:** Garantir que a aplicação Streamlit está funcional.  
* **Critérios de Sucesso:**  
  1. Aplicação inicia sem erros.  
  2. Dashboard carrega os dados corretamente.  
  3. Simulador retorna uma previsão numérica válida.  
  4. Página de análise exibe todos os gráficos e tabelas.  
* **Resultado:** O teste classifica a aplicação como **Pronta para o Usuário** ou **Com Bugs**.

## **6\. Configuração e Boas Práticas**

* **Gerenciamento de Dependências:** Um arquivo requirements.txt.  
* **Configuração Centralizada:** Arquivos .json e .yaml no diretório config/.  
* **Logging:** Implementar logging em todos os scripts.  
* **Estrutura de Diretórios Esperada:**  
  .  
  ├── config/  
  │   ├── data\_mapping.json  
  │   ├── critical\_features.json  
  │   └── settings.yaml  
  ├── data/  
  ├── models/  
  ├── notebooks/  
  ├── reports/  
  ├── src/  
  │   ├── app/  
  │   ├── data/  
  │   ├── features/  
  │   ├── training/  
  │   └── analysis/  
  │       └── discover\_critical\_features.py  
  ├── tests/  
  ├── ESCOPO.md  
  └── requirements.txt

## **7\. Propósito, Uso e Evolução do Projeto**

### **7.1. Para que Serve Tudo Isso? (O Propósito)**

O objetivo desta ferramenta é transformar o processo de orçamentação na construção civil em um **sistema de suporte à decisão rápido, consistente e orientado por dados**. A plataforma centraliza conhecimento, automatiza a criação de inteligência e democratiza o acesso a estimativas de custo confiáveis.

### **7.2. Como Eu Uso a Ferramenta Hoje?**

O uso principal é através da aplicação Streamlit, que permite:

1. **Visão Geral (Dashboard da Fábrica):** Ver quais modelos estão disponíveis e sua confiabilidade.  
2. **Estimativa Rápida (Simulador de Custos):** Digitar a descrição e a unidade de um item para obter um custo estimado.  
3. **Análise Profunda (Análise de Performance):** Investigar a performance detalhada de cada modelo.

### **7.3. O que Dá para Fazer Agora? (Capacidades Atuais)**

* **Estimar custos de insumos e serviços** para famílias com modelos aprovados.  
* **Avaliar a confiabilidade** de cada modelo (R², MAE, Taxa de Aceitação).  
* **Explorar visualmente** os erros e acertos.  
* **Automatizar o retreinamento** de todos os modelos.

### **7.4. Esclarecendo Casos de Uso Específicos**

* **"Esta ferramenta avalia ou estima o custo de um serviço?"**  
  * **Sim.** O sistema foi explicitamente projetado para isso.  
* **"Se eu inputar uma planilha vazia, ela coloca os custos?"**  
  * **Não na versão atual.** A funcionalidade de processamento em lote é um objetivo futuro.

### **7.5. E Agora? Quais os Objetivos Futuros?**

1. **Previsão em Lote:** Permitir o upload de planilhas para orçamentação em massa.  
2. **Análise de Tendência de Custos:** Usar a data\_referencia para visualizar a evolução dos custos.  
3. **Validação Temporal:** Implementar a estratégia de divisão de dados temporal (treino com dados antigos, teste com recentes) para uma avaliação mais rigorosa.  
4. **Modelo de Previsão de Composições (CPU):** Prever o custo de um serviço completo a partir de seus insumos.  
5. **Otimização de Hiperparâmetros:** Usar GridSearchCV para refinar cada modelo.  
6. **Integração com Bancos de Dados:** Migrar o armazenamento para um sistema mais robusto.

## **8\. Manuais de Uso**

### **8.1. Manual do Usuário Final (Aplicação Streamlit)**

**Objetivo:** Obter uma estimativa de custo para um insumo ou serviço.

**Passo a Passo:**

1. **Acesse a Aplicação** e navegue para **"Simulador de Custos"**.  
2. **Descreva o Item:** Nos campos apropriados, digite a **descrição** detalhada e a **unidade** de medida.  
3. **Execute a Previsão:** Clique em **"Estimar Custo"**.  
4. **Analise o Resultado:** A aplicação exibirá a família identificada e o custo estimado.

### **8.2. Manual do Desenvolvedor (Uso via Código para Lotes)**

**Objetivo:** Obter previsões para uma lista de itens programaticamente.

**Contexto:** As funções modulares do projeto podem ser importadas e usadas em outros scripts para automação.

**Exemplo de Script batch\_prediction.py:**

import pandas as pd  
import joblib  
import re  
import numpy as np  
from pathlib import Path

\# ... (código do script de lote, que agora receberia descrição e unidade) ...

## **9\. Backlog de Desenvolvimento e Controle de Status**

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
| **Doc** | Documentação e Manuais (este arquivo) | Em Progresso | 2.5 | \- |

