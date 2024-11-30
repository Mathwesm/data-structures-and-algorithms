from busca_interpolacao import busca_por_interpolacao
from busca_binaria import busca_binaria
import time
import random

def medir_tempo(funcao, lista, valor, iteracoes=1000):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista, valor)
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return resultado, tempo_medio


lista_uniforme = list(range(1, 10_001, 2))
lista_nao_uniforme = sorted(random.sample(range(1, 50_001), 10_000))


valor1 = 7777
valor2 = 50_000


print("Busca na Lista Uniforme")
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_uniforme, valor1)
print(f"Busca por Interpolação: Elemento {valor1}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")

resultado, tempo = medir_tempo(busca_binaria, lista_uniforme, valor1)
print(f"Busca Binária: Elemento {valor1}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")

print("\nBusca na Lista Não Uniforme:")
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_nao_uniforme, valor2)
print(f"Busca por Interpolação: Elemento {valor2}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")

resultado, tempo = medir_tempo(busca_binaria, lista_nao_uniforme, valor2)
print(f"Busca Binária: Elemento {valor2}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")
from busca_interpolacao import busca_por_interpolacao
from busca_binaria import busca_binaria
import time
import random

def medir_tempo(funcao, lista, valor, iteracoes=1000):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista, valor)
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return resultado, tempo_medio


lista_uniforme = list(range(1, 10_001, 2))
lista_nao_uniforme = sorted(random.sample(range(1, 50_001), 10_000))


valor1 = 7777
valor2 = 50_000


print("Busca na Lista Uniforme")
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_uniforme, valor1)
print(f"Busca por Interpolação: Elemento {valor1}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")

resultado, tempo = medir_tempo(busca_binaria, lista_uniforme, valor1)
print(f"Busca Binária: Elemento {valor1}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")


print("\nBusca na Lista Não Uniforme:")
resultado, tempo = medir_tempo(busca_por_interpolacao, lista_nao_uniforme, valor2)
print(f"Busca por Interpolação: Elemento {valor2}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")

resultado, tempo = medir_tempo(busca_binaria, lista_nao_uniforme, valor2)
print(f"Busca Binária: Elemento {valor2}, Índice: {resultado}, Tempo: {tempo:.10f} segundos")
