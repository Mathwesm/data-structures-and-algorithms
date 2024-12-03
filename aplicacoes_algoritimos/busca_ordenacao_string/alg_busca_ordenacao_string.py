from algoritimos_busca.busca_binaria import busca_binaria
from desafio.quick_sort import quick_sort
from aplicacoes_algoritimos.busca_ordenacao_string.merge_sort import merge_sort

palavras = ["banana", "maçã", "laranja", "uva", "abacaxi"]

print("Lista original:")
print(palavras)


merge_sort(palavras)
print("\nLista ordenada com Merge Sort:")
print(palavras)


palavra_para_buscar = "laranja"
resultado = busca_binaria(palavras, palavra_para_buscar)
if resultado:
    print(f"\nA palavra '{palavra_para_buscar}' foi encontrada na lista!")
else:
    print(f"\nA palavra '{palavra_para_buscar}' não está na lista.")


palavras = ["banana", "maçã", "laranja", "uva", "abacaxi"]
palavras_ordenadas = quick_sort(palavras)
print("\nLista ordenada com Quick Sort:")
print(palavras_ordenadas)


palavra_para_buscar = "abacaxi"
resultado = busca_binaria(palavras_ordenadas, palavra_para_buscar)
if resultado:
    print(f"\nA palavra '{palavra_para_buscar}' foi encontrada na lista!")
else:
    print(f"\nA palavra '{palavra_para_buscar}' não está na lista.")