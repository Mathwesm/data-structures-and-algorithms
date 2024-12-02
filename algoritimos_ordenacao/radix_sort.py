def contagem_ordenada(lista, exp, base=10):
    n = len(lista)
    resultado = [0] * n
    contagem = [0] * base

    for i in range(n):
        indice = (lista[i] // exp) % base
        contagem[indice] += 1

    for i in range(1, base):
        contagem[i] += contagem[i - 1]

    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % base
        resultado[contagem[indice] - 1] = lista[i]
        contagem[indice] -= 1
        i -= 1

    for i in range(n):
        lista[i] = resultado[i]


def radix_sort(lista, base=10):
    max_num = max(lista)

    exp = 1
    while max_num // exp > 0:
        contagem_ordenada(lista, exp, base)
        exp *= base

    return lista


arr_2_digitos = [42, 25, 12, 89, 67]
arr_5_digitos = [54213, 12345, 98765, 87654, 23456]
arr_10_digitos = [1234567890, 9876543210, 4567891230, 2345678901, 6789012345]

print("Lista original (2 dígitos):", arr_2_digitos)
arr_ordenada_2 = radix_sort(arr_2_digitos, base=10)
print("Lista ordenada (2 dígitos):", arr_ordenada_2)

print("\nLista original (5 dígitos):", arr_5_digitos)
arr_ordenada_5 = radix_sort(arr_5_digitos, base=10)
print("Lista ordenada (5 dígitos):", arr_ordenada_5)

print("\nLista original (10 dígitos):", arr_10_digitos)
arr_ordenada_10 = radix_sort(arr_10_digitos, base=10)
print("Lista ordenada (10 dígitos):", arr_ordenada_10)
