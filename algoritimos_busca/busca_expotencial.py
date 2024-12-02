from tempo.time import medir_tempo

def busca_binaria(lista, baixo, alto, valor):
    while baixo <= alto:
        meio = baixo + (alto - baixo) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

def busca_exponencial(lista, valor):
    if lista[0] == valor:
        return 0
    i = 1
    while i < len(lista) and lista[i] <= valor:
        i *= 2
    return busca_binaria(lista, i // 2, min(i, len(lista) - 1), valor)


lista_pequeno = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
y = 15
resultado, tempo = medir_tempo(busca_exponencial, lista_pequeno, y, iteracoes=1000)
print(f"Elemento {y} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")

lista_grande = list(range(1, 10_001))
x = 7777
resultado, tempo = medir_tempo(busca_exponencial, lista_grande, x, iteracoes=1000)
print(f"Elemento {x} encontrado no índice: {resultado}, Tempo médio: {tempo:.10f} segundos")
