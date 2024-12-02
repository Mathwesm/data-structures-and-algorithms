import math
import random
from tempo.time import medir_tempo

def busca_jump(lista, x):
    n = len(lista)
    salto = int(math.sqrt(n))
    prev = 0

    while prev < n and lista[min(salto, n) - 1] < x:
        prev = salto
        salto += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(salto, n)):
        if lista[i] == x:
            return i
    return -1


lista_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x1 = 70
resultado, tempo = medir_tempo(busca_jump, lista_uniforme, x1, iteracoes=1000)
print(f"Elemento {x1} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_nao_uniforme = [3, 7, 15, 25, 40, 65, 110, 200]
x2 = 40
resultado, tempo = medir_tempo(busca_jump, lista_nao_uniforme, x2, iteracoes=1000)
print(f"Elemento {x2} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_uniforme_grande = list(range(1, 10_001))
x3 = 7777
resultado, tempo = medir_tempo(busca_jump, lista_uniforme_grande, x3, iteracoes=1000)
print(f"Elemento {x3} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_nao_uniforme_grande = sorted(random.sample(range(1, 50_001), 10_000))
x4 = 7777
resultado, tempo = medir_tempo(busca_jump, lista_nao_uniforme_grande, x4, iteracoes=1000)
print(f"Elemento {x4} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")
