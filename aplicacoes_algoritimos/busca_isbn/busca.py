from busca_binaria_isbn import busca_binaria_isbn

livros = [
    {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "isbn": "978-3-16-148410-0"},
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "isbn": "978-1-56619-909-4"},
    {"titulo": "1984", "autor": "George Orwell", "isbn": "978-0-452-28423-4"},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "isbn": "978-0-452-28425-8"},
    {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "isbn": "978-0-06-088328-7"}
]

print("Lista de livros disponíveis:")
for livro in livros:
    print(f"Titulo: {livro['titulo']}, Autor: {livro['autor']}, ISBN: {livro['isbn']}")


isbn_procurado = "978-0-452-28423-4"
resultado = busca_binaria_isbn(livros, isbn_procurado)

if resultado:
    print("\nLivro encontrado:")
    print(f"Título: {resultado['titulo']}, Autor: {resultado['autor']}, ISBN: {resultado['isbn']}")
else:
    print(f"\nO livro com ISBN {isbn_procurado} não foi encontrado na biblioteca.")
