# Relatório da Atividade de Processamento Paralelo de Arquivos de Log

**Disciplina:** Programação Concorrente e Paralela  
**Aluno(s):** Rayna Lívia Oliveira Pereira  
**Turma:** ADS04N1  
**Professor:** Rafael  
**Data:** 25 de março de 2026

---

## 1. Descrição do Problema

### Problema Computacional

O problema abordado é o **processamento paralelo de arquivos de log para análise de texto em larga escala**. Um conjunto de 400 arquivos de texto (cada um contendo múltiplas linhas de logs) precisa ser processado para extrair estatísticas como:
- Número total de linhas
- Número total de palavras
- Número total de caracteres
- Contagem de palavras-chave específicas (erro, warning, info)

### Algoritmo Utilizado

O programa implementa um **modelo de processamento paralelo baseado em Pool de Processos** utilizando a biblioteca `multiprocessing` do Python. O algoritmo segue o padrão:

1. **Distribuição de trabalho:** Os arquivos são distribuídos entre os processos disponíveis
2. **Processamento paralelo:** Cada processo lê e analisa seus arquivos atribuídos
3. **Agregação de resultados:** Os resultados parciais são combinados para obter estatísticas totais

### Tamanho da Entrada

- **Número de arquivos:** 400 arquivos de log
- **Localização:** Diretório `log2/`
- **Tamanho aproximado:** Centenas de MB de dados textuais

### Objetivo da Paralelização

O objetivo é investigar como a paralelização com múltiplos processos afeta o desempenho na análise de um grande volume de dados, respondendo às seguintes questões:

- **Qual algoritmo foi utilizado?** Pool de processos com distribuição de carga
- **Qual é o objetivo do programa?** Processar logs em paralelo para extrair estatísticas
- **Qual o volume de dados processado?** 400 arquivos de log (~400-500 MB)
- **Qual a complexidade aproximada do algoritmo?** O(n/p) onde n é o tamanho total dos dados e p é o número de processos
- **O speedup é próximo do ideal?** Os resultados revelam escalabilidade limitada (analisado na seção 10)

---

## 2. Ambiente Experimental

| Item | Descrição |
|------|-----------|
| **Processador** | 12th Gen Intel Core i7-12700 |
| **Número de núcleos físicos** | 12 |
| **Número de processadores lógicos** | 20 (incluindo Hyper-Threading) |
| **Memória RAM** | 16 GB (DDR4) |
| **Sistema Operacional** | Microsoft Windows 11 Pro |
| **Linguagem utilizada** | Python 3.13.2 |
| **Biblioteca de paralelização** | `multiprocessing.Pool` |
| **Versão do Python** | 3.13.2 |
| **Ambiente de execução** | VirtualEnvironment (venv) |

### Características Relevantes

- O processador suporta até 12 processos verdadeiramente paralelos (núcleos físicos)
- A máquina possui 20 processadores lógicos, permitindo escalonamento de até 20 threads
- A memória disponível (16 GB) é suficiente para manter múltiplos processos em execução
- Executor em ambiente Windows, com overhead de contexto específico

---

## 3. Metodologia de Testes

### Procedimento Experimental

Os testes foram conduzidos seguindo um protocolo rigoroso:

**Configurações testadas:**
- 1 processo (versão serial/baseline)
- 2 processos
- 4 processos
- 8 processos
- 12 processos

**Número de execuções:** 1 execução para cada configuração  
**Forma de cálculo:** Tempo de execução obtido diretamente do `time.time()`  
**Cálculo da métrica:** Tempo decorrido = tempo_final - tempo_inicial

### Condições de Execução

- Todos os testes foram executados na mesma máquina
- Machine foi mantida em estado similar (sem programas pesados em background)
- O mesmo conjunto de 400 arquivos foi utilizado para todos os testes
- Não houve variações significativas no tamanho da entrada entre os testes

---

## 4. Resultados Experimentais

### Tempos de Execução

| Nº Threads/Processos | Tempo de Execução (s) |
|----------------------|----------------------|
| 1                    | 87.6029               |
| 2                    | 50.2153               |
| 4                    | 22.7033               |
| 8                    | 14.1275               |
| 12                   | 13.8232               |

### Observações

- O tempo de execução com 1 processo (serial): **87.6029 segundos**
- Variação de tempo com múltiplos processos: ~87.6 a 13.8 segundos
- Houve redução significativa no tempo total com o aumento de processos
- Há benefício claro da paralelização neste caso

---

## 5. Cálculo de Speedup e Eficiência

### Fórmulas Utilizadas

**Speedup(p)** = T(1) / T(p)

Onde:
- T(1) = tempo da execução serial (23.4331 s)
- T(p) = tempo com p processos

**Eficiência(p)** = Speedup(p) / p

Onde:
- p = número de processos

### Cálculos Realizados

**Para p = 2:**
- Speedup(2) = 87.6029 / 50.2153 = **1.743**
- Eficiência(2) = 1.743 / 2 = **0.871**

**Para p = 4:**
- Speedup(4) = 87.6029 / 22.7033 = **3.858**
- Eficiência(4) = 3.858 / 4 = **0.964**

**Para p = 8:**
- Speedup(8) = 87.6029 / 14.1275 = **6.202**
- Eficiência(8) = 6.202 / 8 = **0.775**

**Para p = 12:**
- Speedup(12) = 87.6029 / 13.8232 = **6.339**
- Eficiência(12) = 6.339 / 12 = **0.528**

---

## 6. Tabela de Resultados

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
|-------------------|-----------|---------|-----------|
| 1                 | 87.6029   | 1.000   | 1.000     |
| 2                 | 50.2153   | 1.743   | 0.871     |
| 4                 | 22.7033   | 3.858   | 0.964     |
| 8                 | 14.1275   | 6.202   | 0.775     |
| 12                | 13.8232   | 6.339   | 0.528     |

---

## 7. Gráficos de Desempenho (Tempo, Speedup e Eficiência)

<figure>
  <img src="./graficos/tempo_por_processos.png" alt="Tempo por Processos" width="45%" style="margin-right:10px"/>
  <img src="./graficos/speedup_vs_processos.png" alt="Speedup vs Processos" width="45%"/>
</figure>

<figure>
  <img src="./graficos/eficiencia_vs_processos.png" alt="Eficiência vs Processos" width="45%" style="margin-right:10px"/>
  <img src="./graficos/comparacao_metricas.png" alt="Comparação de Métricas" width="45%"/>
</figure>

**Análise geral:**
- O tempo de execução diminui de 87.6 segundos (1 processo) para 13.8 segundos (12 processos).
- O speedup aumenta progressivamente: de 1.0 (1 processo) para 6.339 (12 processos).
- A eficiência permanece alta até 4 processos (0.964), mas decai com mais processos.
- O gráfico de comparação mostra que a paralelização trouxe ganhos significativos de desempenho.

---

## 10. Análise dos Resultados

### 10.1 Questões a Serem Respondidas

#### O speedup obtido foi próximo do ideal?

**Sim, relativamente.** O speedup obtido foi significativo e crescente:
- Speedup com 1 processo: 1.0 (baseline)
- Speedup com 2 processos: 1.743 (74% do ideal)
- Speedup com 12 processos: 6.339 (53% do ideal)

O speedup aumenta com o número de processos, demonstrando que a paralelização está trazendo ganhos de desempenho, embora não lineares devido a overheads.

#### A aplicação apresentou escalabilidade?

**Sim. A aplicação apresentou boa escalabilidade até 8 processos.** 
- Com 2 processos: speedup de 1.743 (tempo reduzido de 87.6s para 50.2s)
- Com 4 processos: speedup de 3.858 (tempo reduzido para 22.7s)
- Com 8 processos: speedup de 6.202 (tempo reduzido para 14.1s)
- Com 12 processos: speedup de 6.339 (tempo reduzido para 13.8s)

A aplicação escala bem até 8 processos, com redução significativa no tempo de execução.

#### Em qual ponto a eficiência começou a cair?

A eficiência começou a cair **a partir de 8 processos**:
- 2 processos: 0.871 (alta eficiência)
- 4 processos: 0.964 (eficiência quase ideal)
- 8 processos: 0.775 (queda significativa)
- 12 processos: 0.528 (eficiência reduzida)

A eficiência permanece alta até 4 processos, mas decai quando ultrapassa o número de núcleos físicos disponíveis (12 núcleos).
- 12 processos: 0.079

#### O número de threads ultrapassa o número de núcleos físicos da máquina?

Sim, a partir de 8 processos, o número de processos começa a superar os núcleos físicos disponíveis (12):
- 1-12 processos: compatível com 12 núcleos físicos
- No entanto, com 20 processadores lógicos (Hyper-Threading), há espaço para até 20 threads

#### Houve overhead de paralelização?

**Sim, mas compensado pelos benefícios até 8 processos.** O overhead é evidente na redução da eficiência com 12 processos:
- Tempo com 1 processo: 87.6029 s
- Tempo com 8 processos: 14.1275 s (6.2x speedup)
- Tempo com 12 processos: 13.8232 s (6.3x speedup, apenas 0.5s mais rápido)

O overhead se torna mais significativo quando o número de processos excede os núcleos físicos.

### 10.2 Discussão de Possíveis Causas

#### Perda de Desempenho

**Causas principais:**

1. **Overhead de criação de processos:** Em Python, criar um novo processo é custoso. O overhead de inicializar cada processo (cópia de espaço de memória, setup de runtime) pode superar os benefícios da paralelização para este caso de uso.

2. **Comunicação entre processos:** A IPC (Inter-Process Communication) envolve serialização/desserialização de dados (usando pickle no Python), o que é custoso.

3. **GIL (Global Interpreter Lock) alternativo:** Embora `multiprocessing` evite o GIL, existem sincronizações internas que podem serializar parte do trabalho.

#### Gargalos no Algoritmo

1. **Distribuição desigual de carga:** Se alguns arquivos são muito maiores que outros, haverá desbalanceamento de carga entre processos.

2. **I/O como gargalo:** O processamento dos logs é I/O-bound. Em contraste com CPU-bound, a paralelização em I/O-bound raramente traz melhorias significativas.

3. **Pool overhead:** O Pool de processos tem overhead de gerenciamento (queue de tarefas, sincronização, etc.).

#### Sincronização e Comunicação

1. **Sincronização implícita:** O `Pool.map()` é uma operação síncrona que aguarda todos os resultados antes de retornar.

2. **Agregação de resultados:** O código agrega resultados sequencialmente no processo principal, criando um ponto de serialização.

#### Contenção de Memória e Cache

1. **Contenção de cache L3:** Com múltiplos processos compondo pelo mesmo cache L3 compartilhado, há degradação de performance.

2. **Falta de localidade espacial:** Cada processo tem seu próprio espaço de memória, perdendo oportunidades de cache compartilhado.

---

## 11. Conclusão

### Resumo dos Achados

Os resultados experimentais revelam que **a paralelização não trouxe ganho significativo de desempenho** para este caso de uso específico. Os tempos de execução permaneceram consistentemente próximos a 23.4-24.8 segundos, independentemente do número de processos utilizados.

### Pontos Principais

#### O paralelismo trouxe ganho significativo de desempenho?

**Não.** Na verdade, há indicações de que a paralelização trouxe **degradação de desempenho** em alguns casos. O tempo com 2 processos (24.6948 s) foi 1.26 segundos mais lento que a versão serial (23.4331 s).

#### Qual foi o melhor número de threads/processos?

**1 processo (versão serial)** foi a mais eficiente com tempo de execução de **23.4331 segundos**.

Entre as configurações paralelas:
- Melhor: **4 processos** (23.8140 s, apenas 0.38 s mais lento que serial)
- Pior: **2 processos** (24.6948 s, 1.26 s mais lento)

#### O programa escala bem com o aumento do paralelismo?

**Não. O programa apresenta escalabilidade negativa ou nula:**
- Esperado para escalabilidade linear: T(12) ≈ 23.4331/12 ≈ 1.95 s
- Observado: T(12) = 24.7704 s
- Razão: ~12.7x pior que o ideal

#### Quais melhorias poderiam ser feitas na implementação?

**Recomendações:**

1. **Otimização para 8 processos:** Configuração ideal baseada nos resultados
2. **Balanceamento de carga:** Verificar se arquivos têm tamanhos similares
3. **Redução de comunicação:** Minimizar IPC entre processos
4. **Cache awareness:** Considerar afinidade de processo para melhor uso de cache
5. **Monitoramento de recursos:** Adicionar profiling para identificar gargalos específicos

### Conclusão Final

**A implementação de processamento paralelo com `multiprocessing` demonstrou ser altamente efetiva para este caso de uso.** Os resultados mostram redução significativa no tempo de execução, com speedup de até 6.3x e eficiência mantida acima de 0.5 mesmo com 12 processos.

O programa demonstra **escalabilidade positiva**, onde:
- Esperado para escalabilidade linear: T(12) ≈ 87.6029/12 ≈ 7.3 s
- Observado: T(12) = 13.8232 s
- Razão: ~6.3x speedup, próximo ao ideal considerando overheads

**Recomendação:** A configuração de **8 processos** oferece o melhor equilíbrio entre desempenho e eficiência para este workload. Para workloads similares, multiprocessing é uma escolha adequada quando o overhead de processos é justificado pelo volume de dados.

---

## Apêndice: Referências aos Gráficos

Todos os gráficos gerados estão disponíveis em alta resolução (300 DPI) no diretório `graficos/`:

- **tempo_por_processos.png** - Visualiza o tempo de execução vs número de processos
- **speedup_vs_processos.png** - Mostra a evolução do speedup
- **eficiencia_vs_processos.png** - Demonstra a queda de eficiência
- **comparacao_metricas.png** - Sintese comparativa de todas as métricas

---

**Relatório elaborado em:** 25 de março de 2026
