from algoritimos_busca.busca_binaria import busca_binaria
from tempo.time import medir_tempo

def busca_ternaria(lista, x):
    baixo, alto = 0, len(lista) - 1

    while alto >= baixo:
        meio1 = baixo + (alto - baixo) // 3
        meio2 = alto - (alto - baixo) // 3

        if lista[meio1] == x:
            return meio1
        elif lista[meio2] == x:
            return meio2
        elif x < lista[meio1]:
            alto = meio1 - 1
        elif x > lista[meio2]:
            baixo = meio2 + 1
        else:
            baixo = meio1 + 1
            alto = meio2 - 1

    return -1


def comparar_algoritmos_busca():
    lista = [i for i in range(1, 10001)]
    x = 9876

    _, tempo_ternario = medir_tempo(busca_ternaria, lista, x, iteracoes=100)
    print(f"Tempo médio de Busca Ternária: {tempo_ternario:.6f} segundos")

    _, tempo_binaria = medir_tempo(busca_binaria, lista, x, iteracoes=100)
    print(f"Tempo médio de Busca Binária: {tempo_binaria:.6f} segundos")


comparar_algoritmos_busca()
