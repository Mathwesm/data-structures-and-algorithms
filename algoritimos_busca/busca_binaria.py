import time
import random

def busca_binaria(lista, valor):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            baixo = meio + 1
        else:
            alto = meio - 1

    return -1

def medir_tempo(funcao, lista, valor, iteracoes=1000):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista, valor)
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return resultado, tempo_medio

lista_ordenada = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
valor1 = 70

resultado, tempo = medir_tempo(busca_binaria, lista_ordenada, valor1, iteracoes=1000)
print(f"Elemento {valor1} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_ordenada_grande = list(range(1, 10_001))
valor2 = 7777
resultado, tempo = medir_tempo(busca_binaria, lista_ordenada_grande, valor2, iteracoes=1000)
print(f"Elemento {valor2} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_nao_ordenada = lista_ordenada_grande.copy()
random.shuffle(lista_nao_ordenada)

valor3 = 7777
resultado, tempo = medir_tempo(busca_binaria, lista_nao_ordenada, valor3, iteracoes=1000)
print(f"Elemento {valor3} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")