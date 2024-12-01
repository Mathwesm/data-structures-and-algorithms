import time
import random

def busca_por_interpolacao(lista, x):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto and lista[baixo] <= x <= lista[alto]:
        pos = baixo + ((x - lista[baixo]) * (alto - baixo)) // (lista[alto] - lista[baixo])

        if lista[pos] == x:
            return pos
        elif lista[pos] < x:
            baixo = pos + 1
        else:
            alto = pos - 1

    return -1

def medir_tempo(funcao, lista, valor, iteracoes=1000):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista, valor)
        assert resultado is not None, f"Erro: {valor} não encontrado!"
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return resultado, tempo_medio


lista_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x1 = 70
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_uniforme, x1, iteracoes=1000)
print(f"Elemento {x1} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_nao_uniforme = [3, 7, 15, 25, 40, 65, 110, 200]
x2 = 40
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_nao_uniforme, x2, iteracoes=1000)
print(f"Elemento {x2} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_uniforme_grande = list(range(1, 10_001))
x3 = 7777
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_uniforme_grande, x3, iteracoes=1000)
print(f"Elemento {x3} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_nao_uniforme_grande = sorted(random.sample(range(1, 50_001), 10_000))
x4 = 7777
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_nao_uniforme_grande, x4, iteracoes=1000)
print(f"Elemento {x4} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")
