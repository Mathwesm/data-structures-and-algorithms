def ordenar_por_mercado(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    metade_esquerda = ordenar_por_mercado(lista[:meio])
    metade_direita = ordenar_por_mercado(lista[meio:])

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
arr_ordenada = ordenar_por_mercado(arr)
print("Lista ordenada (inteiros):", arr_ordenada)
