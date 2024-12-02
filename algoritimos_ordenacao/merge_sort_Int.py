def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    metade_esquerda = merge_sort(lista[:meio])
    metade_direita = merge_sort(lista[meio:])

    return mesclar(metade_esquerda, metade_direita)

def mesclar(esquerda, direita):
    lista_ordenada = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1

    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])

    return lista_ordenada


arr = [64, 25, 12, 22, 11]
print("Lista original (inteiros):", arr)
arr_ordenada = merge_sort(arr)
print("Lista ordenada (inteiros):", arr_ordenada)
