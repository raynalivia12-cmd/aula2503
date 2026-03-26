# Avaliador de Logs

## Análise de Performance

Resultados da análise de processamento paralelo de arquivos de log com diferentes números de processos:

| Processos | Tempo (s) | Speedup | Eficiência |
|-----------|-----------|---------|-----------|
| 1         | 23.4331   | 1.000   | 1.000     |
| 2         | 24.6948   | 0.949   | 0.475     |
| 4         | 23.8140   | 0.984   | 0.246     |
| 8         | 23.8561   | 0.982   | 0.123     |
| 12        | 24.7704   | 0.946   | 0.079     |

## Gráficos Gerados

Os gráficos de análise foram gerados automaticamente e salvos em `graficos/`:

- `tempo_por_processos.png` - Tempo de execução vs número de processos
- `speedup_vs_processos.png` - Speedup vs número de processos
- `eficiencia_vs_processos.png` - Eficiência vs número de processos
- `comparacao_metricas.png` - Comparação geral de todas as métricas