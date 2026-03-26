import matplotlib.pyplot as plt
import os
import numpy as np

# Dados da análise
processos = [1, 2, 4, 8, 12]
tempo = [23.4331, 24.6948, 23.8140, 23.8561, 24.7704]
speedup = [1.000, 0.949, 0.984, 0.982, 0.946]
eficiencia = [1.000, 0.475, 0.246, 0.123, 0.079]

# Criar diretório para gráficos
os.makedirs("graficos", exist_ok=True)

# Configurar estilo
plt.style.use('seaborn-v0_8-darkgrid')

# 1. Tempo por número de processos
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(processos, tempo, marker='o', linewidth=2, markersize=8, color='#2E86AB')
ax.fill_between(processos, tempo, alpha=0.3, color='#2E86AB')
ax.set_xlabel('Número de Processos', fontsize=12, fontweight='bold')
ax.set_ylabel('Tempo (segundos)', fontsize=12, fontweight='bold')
ax.set_title('Tempo de Execução vs Número de Processos', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xticks(processos)
plt.tight_layout()
plt.savefig('graficos/tempo_por_processos.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Speedup vs número de processos
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(processos, speedup, marker='s', linewidth=2, markersize=8, color='#A23B72')
ax.fill_between(processos, speedup, alpha=0.3, color='#A23B72')
ax.set_xlabel('Número de Processos', fontsize=12, fontweight='bold')
ax.set_ylabel('Speedup', fontsize=12, fontweight='bold')
ax.set_title('Speedup vs Número de Processos', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xticks(processos)
plt.tight_layout()
plt.savefig('graficos/speedup_vs_processos.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Eficiência vs número de processos
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(processos, eficiencia, marker='^', linewidth=2, markersize=8, color='#F18F01')
ax.fill_between(processos, eficiencia, alpha=0.3, color='#F18F01')
ax.set_xlabel('Número de Processos', fontsize=12, fontweight='bold')
ax.set_ylabel('Eficiência', fontsize=12, fontweight='bold')
ax.set_title('Eficiência vs Número de Processos', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xticks(processos)
ax.set_ylim([0.035, 0.045])
plt.tight_layout()
plt.savefig('graficos/eficiencia_vs_processos.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Comparação de todas as métricas
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Tempo
axes[0].plot(processos, tempo, marker='o', linewidth=2, markersize=8, color='#2E86AB')
axes[0].fill_between(processos, tempo, alpha=0.3, color='#2E86AB')
axes[0].set_xlabel('Número de Processos', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Tempo (s)', fontsize=11, fontweight='bold')
axes[0].set_title('Tempo de Execução', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)
axes[0].set_xticks(processos)

# Speed
axes[1].plot(processos, speedup, marker='s', linewidth=2, markersize=8, color='#A23B72')
axes[1].fill_between(processos, speedup, alpha=0.3, color='#A23B72')
axes[1].set_xlabel('Número de Processos', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Speedup', fontsize=11, fontweight='bold')
axes[1].set_title('Speedup', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)
axes[1].set_xticks(processos)

# Eficiência
axes[2].plot(processos, eficiencia, marker='^', linewidth=2, markersize=8, color='#F18F01')
axes[2].fill_between(processos, eficiencia, alpha=0.3, color='#F18F01')
axes[2].set_xlabel('Número de Processos', fontsize=11, fontweight='bold')
axes[2].set_ylabel('Eficiência', fontsize=11, fontweight='bold')
axes[2].set_title('Eficiência', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)
axes[2].set_xticks(processos)

plt.suptitle('Análise de Performance - Comparação de Métricas', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('graficos/comparacao_metricas.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Gráficos gerados com sucesso em 'graficos/'")
print("  - tempo_por_processos.png")
print("  - speedup_vs_processos.png")
print("  - eficiencia_vs_processos.png")
print("  - comparacao_metricas.png")
