def ordenar_por_mercado_strings(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    metade_esquerda = ordenar_por_mercado_strings(lista[:meio])
    metade_direita = ordenar_por_mercado_strings(lista[meio:])

    return mesclar_strings(metade_esquerda, metade_direita)


def mesclar_strings(esquerda, direita):
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


arr_strings = ["banana", "maça", "bolo", "cachorro"]
print("Lista original (strings):", arr_strings)
arr_strings_ordenada = ordenar_por_mercado_strings(arr_strings)
print("Lista ordenada (strings):", arr_strings_ordenada)
