from algoritimos_busca.busca_interpolacao import busca_por_interpolacao
from bucket_sort import bucket_sort


notas = [85, 92, 75, 67, 89, 95, 100, 74, 83, 88, 90, 61, 79, 68, 93]


notas_ordenadas = bucket_sort(notas)


print("Notas ordenadas:", notas_ordenadas)

# Procurar por uma nota específica
nota_procurada = 90
indice = busca_por_interpolacao(notas_ordenadas, nota_procurada)

if indice != -1:
    print(f"\nA nota {nota_procurada} foi encontrada na posição {indice} da lista ordenada.")
else:
    print(f"\nA nota {nota_procurada} não foi encontrada na lista.")