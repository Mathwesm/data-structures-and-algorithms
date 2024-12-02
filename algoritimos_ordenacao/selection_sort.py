import random
from tempo.time import medir_tempo_selection

def ordenacao_selecao(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):

            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

        if len(lista) <= 10:
            print(f"Iteração {i + 1}: {lista}")

    return lista



lista_pequena = [64, 25, 12, 22, 11]
print("Lista original (pequena):", lista_pequena)
lista_ordenada_pequena = ordenacao_selecao(lista_pequena)
print("\nLista ordenada (pequena):", lista_ordenada_pequena)

lista_media = random.sample(range(1, 1001), 100)
tempo_execucao_media = medir_tempo_selection(ordenacao_selecao, lista_media, iteracoes=1)
print(f"\nTempo de execução para lista média: {tempo_execucao_media:.6f} segundos")


lista_grande = random.sample(range(1, 10001), 1000)
tempo_execucao_grande = medir_tempo_selection(ordenacao_selecao, lista_grande, iteracoes=1)
print(f"\nTempo de execução para lista grande: {tempo_execucao_grande:.6f} segundos")
