import os
import time
from multiprocessing import Pool

KEYWORDS = ["erro", "warning", "info"]

def process_file(filepath):
    linhas = 0
    palavras = 0
    caracteres = 0
    contagem = {k: 0 for k in KEYWORDS}

    with open(filepath, "r", encoding="utf-8") as f:
        for linha in f:
            linhas += 1
            caracteres += len(linha)
            palavras_lista = linha.split()
            palavras += len(palavras_lista)

            for p in palavras_lista:
                if p.lower() in contagem:
                    contagem[p.lower()] += 1

    return linhas, palavras, caracteres, contagem


def executar(pasta, n_processos):
    arquivos = [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if os.path.isfile(os.path.join(pasta, f))
    ]

    inicio = time.time()

    with Pool(n_processos) as p:
        resultados = p.map(process_file, arquivos)

    total_linhas = sum(r[0] for r in resultados)
    total_palavras = sum(r[1] for r in resultados)
    total_caracteres = sum(r[2] for r in resultados)

    total_contagem = {k: 0 for k in KEYWORDS}
    for r in resultados:
        for k in KEYWORDS:
            total_contagem[k] += r[3][k]

    fim = time.time()

    print("\n=== RESULTADO CONSOLIDADO ===")
    print(f"Linhas: {total_linhas}")
    print(f"Palavras: {total_palavras}")
    print(f"Caracteres: {total_caracteres}")

    print("\nPalavras-chave:")
    for k in KEYWORDS:
        print(f"{k}: {total_contagem[k]}")

    print(f"\nTempo: {fim - inicio:.4f} segundos")


if __name__ == "__main__":
    for p in [1, 2, 4, 8, 12]:
        print(f"\n=== {p} PROCESSOS ===")
        executar("log2",1)