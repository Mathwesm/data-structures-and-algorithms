import random
import matplotlib.pyplot as plt
from algoritimos_busca.busca_binaria import busca_binaria
from algoritimos_busca.busca_jump import busca_jump
from tempo.time import medir_tempo


def gerar_lista_ordenada(n):
    return sorted(random.sample(range(n * 10), n))

def comparar_algoritmos_busca():
    tamanhos_lista = [100, 1000, 10_000, 100_000]
    tempos_jump = []
    tempos_binaria = []

    for n in tamanhos_lista:
        lista = gerar_lista_ordenada(n)
        x = random.choice(lista)

        _, tempo_jump = medir_tempo(busca_jump, lista, x, iteracoes=100)
        _, tempo_binaria = medir_tempo(busca_binaria, lista, x, iteracoes=100)

        tempos_jump.append(tempo_jump)
        tempos_binaria.append(tempo_binaria)

        print(f"Lista de tamanho {n}:")
        print(f"  Busca Jump - Tempo médio: {tempo_jump:.10f} segundos")
        print(f"  Busca Binária - Tempo médio: {tempo_binaria:.10f} segundos\n")

    plt.figure(figsize=(10, 6))

    plt.plot(tamanhos_lista, tempos_jump, label="Busca Jump", color='blue', marker='o')
    plt.plot(tamanhos_lista, tempos_binaria, label="Busca Binária", color='red', marker='o')

    plt.title("Comparação de Tempos - Busca Jump vs Busca Binária")
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Tempo Médio (segundos)")
    plt.legend()
    plt.grid(True)
    plt.show()

comparar_algoritmos_busca()
