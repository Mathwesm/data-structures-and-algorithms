def busca_binaria_isbn(livros, isbn_procurado):
    inicio = 0
    fim = len(livros) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        isbn_atual = livros[meio]["isbn"]

        if isbn_atual == isbn_procurado:
            return livros[meio]
        elif isbn_atual < isbn_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None
