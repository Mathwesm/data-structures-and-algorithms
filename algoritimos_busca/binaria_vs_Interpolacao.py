import time
import random
import matplotlib.pyplot as plt
from busca_interpolacao import busca_por_interpolacao
from busca_binaria import busca_binaria


def medir_tempo(funcao, lista, valor, iteracoes=1000):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista, valor)
        assert resultado is not None, f"Erro: {valor} não encontrado!"
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return resultado, tempo_medio

# Criando as listas de teste
lista_uniforme = list(range(1, 10_001, 2))
lista_nao_uniforme = sorted(random.sample(range(1, 50_001), 10_000))


valor1 = 7777
valor2 = 50_000


tempos_binaria_uniforme = []
tempos_interpolacao_uniforme = []
tempos_binaria_nao_uniforme = []
tempos_interpolacao_nao_uniforme = []


tamanhos = range(100, 1001, 100)


for i in tamanhos:
    lista_uniforme_parcial = lista_uniforme[:i]
    _, tempo_binaria = medir_tempo(busca_binaria, lista_uniforme_parcial, valor1)
    tempos_binaria_uniforme.append(tempo_binaria)
    _, tempo_interpolacao = medir_tempo(busca_por_interpolacao, lista_uniforme_parcial, valor1)
    tempos_interpolacao_uniforme.append(tempo_interpolacao)


for i in tamanhos:
    lista_nao_uniforme_parcial = lista_nao_uniforme[:i]
    _, tempo_binaria = medir_tempo(busca_binaria, lista_nao_uniforme_parcial, valor2)
    tempos_binaria_nao_uniforme.append(tempo_binaria)
    _, tempo_interpolacao = medir_tempo(busca_por_interpolacao, lista_nao_uniforme_parcial, valor2)
    tempos_interpolacao_nao_uniforme.append(tempo_interpolacao)

# Plotando os gráficos
plt.figure(figsize=(12, 6))

# Gráfico para lista uniforme
plt.subplot(1, 2, 1)
plt.plot(tamanhos, tempos_binaria_uniforme, label="Busca Binária", color='blue', marker='o')
plt.plot(tamanhos, tempos_interpolacao_uniforme, label="Busca por Interpolação", color='red', marker='o')
plt.title("Comparação de Tempos - Lista Uniforme")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo (segundos)")
plt.legend()

# Gráfico para lista não uniforme
plt.subplot(1, 2, 2)
plt.plot(tamanhos, tempos_binaria_nao_uniforme, label="Busca Binária", color='blue', marker='o')
plt.plot(tamanhos, tempos_interpolacao_nao_uniforme, label="Busca por Interpolação", color='red', marker='o')
plt.title("Comparação de Tempos - Lista Não Uniforme")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo (segundos)")
plt.legend()

plt.tight_layout()
plt.show()
