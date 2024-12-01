import time
import random

def ordenacao_shell(lista, tipo_seq="shell"):

    n = len(lista)
    if tipo_seq == "shell":
        gaps = [n // 2, 1]

    elif tipo_seq == "knuth":
        gaps = []
        gap = 1

        while gap < n:
            gaps.append(gap)
            gap = 3 * gap + 1

    elif tipo_seq == "hibbard":
        gaps = []
        gap = 1
        while gap < n:
            gaps.append(gap)
            gap = 2 * gap + 1

    for gap in gaps:
        for i in range(gap, n):
            temp = lista[i]
            j = i

            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp

    return lista

def medir_tempo(funcao, lista, tipo_seq, iteracoes=10):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista.copy(), tipo_seq)
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return tempo_medio

def comparar_algoritmos_shell_sort():
    for n in [100, 1000, 10000]:
        lista = random.sample(range(1, n * 10), n)

        print(f"\nComparando Shell Sort para lista de tamanho {n}:")

        tempo_shell = medir_tempo(ordenacao_shell, lista, "shell", iteracoes=1)
        print(f"Tempo para Shell Sort (sequência Shell): {tempo_shell:.6f} segundos")

        tempo_knuth = medir_tempo(ordenacao_shell, lista, "knuth", iteracoes=1)
        print(f"Tempo para Shell Sort (sequência Knuth): {tempo_knuth:.6f} segundos")

        tempo_hibbard = medir_tempo(ordenacao_shell, lista, "hibbard", iteracoes=1)
        print(f"Tempo para Shell Sort (sequência Hibbard): {tempo_hibbard:.6f} segundos")

comparar_algoritmos_shell_sort()