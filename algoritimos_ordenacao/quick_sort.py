import random
import sys
from tempo.time import medir_tempo

sys.setrecursionlimit(2000)

def quick_sort(lista, escolha_pivo='primeiro'):
    if len(lista) <= 1:
        return lista
    if escolha_pivo == 'primeiro':
        pivo = lista[0]
    elif escolha_pivo == 'ultimo':
        pivo = lista[-1]
    elif escolha_pivo == 'meio':
        pivo = lista[len(lista) // 2]
    elif escolha_pivo == 'aleatorio':
        pivo = random.choice(lista)

    esquerda = [x for x in lista if x < pivo]
    direita = [x for x in lista if x > pivo]

    return quick_sort(esquerda, escolha_pivo) + [pivo] + quick_sort(direita, escolha_pivo)


def comparar_quick_sort():
    lista_quase_ordenada = [i for i in range(1, 1001)]
    lista_quase_ordenada[500], lista_quase_ordenada[600] = lista_quase_ordenada[600], lista_quase_ordenada[500]

    lista_aleatoria = [i for i in range(1000, 0, -1)]

    print("Tempo para lista quase ordenada:")
    for escolha_pivo in ['primeiro', 'ultimo', 'meio', 'aleatorio']:
        _, tempo_gasto = medir_tempo(quick_sort, lista_quase_ordenada, escolha_pivo)
        print(f"  Pivô {escolha_pivo}: {tempo_gasto:.6f} segundos")

    print("\nTempo para lista completamente desordenada:")
    for escolha_pivo in ['primeiro', 'ultimo', 'meio', 'aleatorio']:
        _, tempo_gasto = medir_tempo(quick_sort, lista_aleatoria, escolha_pivo)
        print(f"  Pivô {escolha_pivo}: {tempo_gasto:.6f} segundos")

comparar_quick_sort()
