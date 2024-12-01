import time
import random
import matplotlib.pyplot as plt
from busca_interpolacao import busca_por_interpolacao
from busca_binaria import busca_binaria
from busca_jump import busca_jump
from busca_expotencial import busca_exponencial

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


algoritmos = [busca_binaria, busca_por_interpolacao, busca_jump, busca_exponencial]
nomes_algoritmos = ["Busca Binária", "Busca por Interpolação", "Busca Jump", "Busca Exponencial"]

tempos_uniformes = {nome: [] for nome in nomes_algoritmos}
tempos_nao_uniformes = {nome: [] for nome in nomes_algoritmos}


tamanhos = list(range(1, 1001, 100))

for i in tamanhos:
    lista_uniforme_parcial = lista_uniforme[:i]
    for alg, nome in zip(algoritmos, nomes_algoritmos):
        _, tempo = medir_tempo(alg, lista_uniforme_parcial, valor1)
        tempos_uniformes[nome].append(tempo)


for i in tamanhos:
    lista_nao_uniforme_parcial = lista_nao_uniforme[:i]
    for alg, nome in zip(algoritmos, nomes_algoritmos):
        _, tempo = medir_tempo(alg, lista_nao_uniforme_parcial, valor2)
        tempos_nao_uniformes[nome].append(tempo)


plt.figure(figsize=(14, 6))


plt.subplot(1, 2, 1)
for nome, cor in zip(nomes_algoritmos, ['blue', 'red', 'green', 'purple']):
    plt.plot(tamanhos, tempos_uniformes[nome], label=nome, color=cor, marker='o')
plt.title("Comparação de Tempos - Lista Uniforme")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo Médio (segundos)")
plt.legend()


plt.subplot(1, 2, 2)
for nome, cor in zip(nomes_algoritmos, ['blue', 'red', 'green', 'purple']):
    plt.plot(tamanhos, tempos_nao_uniformes[nome], label=nome, color=cor, marker='o')
plt.title("Comparação de Tempos - Lista Não Uniforme")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo Médio (segundos)")
plt.legend()

plt.tight_layout()
plt.show()
