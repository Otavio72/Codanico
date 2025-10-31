# Nível 4 - Performance ruim
# Erro: leitura repetida de arquivo dentro de loop, algoritmo O(n^2) desnecessário

import time
import os

def count_word_slow(filepath, word):
    counts = {}
    # cada iteração reabre o arquivo inteiro — horrível para arquivos grandes
    for _ in range(100):  # simula múltiplas passadas desnecessárias
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                for w in line.split():
                    counts[w] = counts.get(w, 0) + 1
    return counts.get(word, 0)  # <- o return estava no lugar errado

if __name__ == "__main__":
    # cria um arquivo grande simulado
    fname = "test_big.txt"

    if not os.path.exists(fname):
        with open(fname, "w", encoding='utf-8') as f:
            for i in range(20000):
                f.write("palavra valor outra palavra\n")

    start = time.time()
    print("Contagem (lenta):", count_word_slow(fname, "palavra"))
    print("Tempo:", time.time() - start)
