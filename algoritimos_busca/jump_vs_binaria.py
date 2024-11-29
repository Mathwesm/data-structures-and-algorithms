from busca_binaria import busca_binaria
from busca_jump import busca_jump
import time
import random

def medir_tempo(funcao, lista, valor, iteracoes=100):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista, valor)
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return resultado, tempo_medio

def gerar_lista_ordenada(n):
    return sorted(random.sample(range(n * 10), n))

def comparar_algoritmos_busca():
    for n in [100, 1000, 10_000, 100_000]:
        lista = gerar_lista_ordenada(n)
        x = random.choice(lista)

        resultado, tempo_jump = medir_tempo(busca_jump, lista, x, iteracoes=100)
        resultado, tempo_binaria = medir_tempo(busca_binaria, lista, x, iteracoes=100)

        print(f"Lista de tamanho {n}:")
        print(f"  Busca Jump - Tempo médio: {tempo_jump:.10f} segundos")
        print(f"  Busca Binária - Tempo médio: {tempo_binaria:.10f} segundos\n")

comparar_algoritmos_busca()
