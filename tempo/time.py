import time


def medir_tempo(funcao, lista, valor, iteracoes=1000):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        resultado = funcao(lista, valor)
        assert resultado is not None, f"Erro: {valor} não encontrado!"
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return resultado, tempo_medio


def medir_tempo_comparacoes(funcao, lista, iteracoes=1):
    total_comparacoes = 0
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        lista_copia = lista.copy()
        resultado, comparacoes = funcao(lista_copia)
        total_comparacoes += comparacoes

    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return tempo_medio, total_comparacoes

def medir_tempo_selection(funcao, lista, valor=None, iteracoes=1):
    inicio = time.perf_counter()
    for _ in range(iteracoes):
        if valor is not None:
            funcao(lista, valor)
        else:
            funcao(lista)
    fim = time.perf_counter()
    tempo_medio = (fim - inicio) / iteracoes
    return tempo_medio