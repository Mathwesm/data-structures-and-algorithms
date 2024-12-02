def bucket_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave


def bucket_sort_float(lista):
    n = len(lista)
    if n <= 1:
        return lista

    baldes = [[] for _ in range(n)]

    for i in lista:
        indice = int(i * n)
        baldes[indice].append(i)

    for i in range(n):
        bucket_sort_float(baldes[i])

    resultado = []
    for balde in baldes:
        resultado.extend(balde)

    return resultado


arr_float = [0.42, 0.32, 0.17, 0.83, 0.91, 0.19, 0.65]
print("Lista original (flutuante):", arr_float)
arr_float_ordenada = ordenacao_baldes_float(arr_float)
print("Lista ordenada (flutuante):", arr_float_ordenada)
