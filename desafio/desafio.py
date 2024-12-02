import time
from busca_binaria import busca_binaria
from quick_sort import quick_sort

def main():
    print("Escolha um algoritmo de ordenação ou busca:")
    print("1 - Quick Sort")
    print("2 - Binary Search")

    escolha = int(input("Digite o número correspondente ao algoritmo escolhido: "))

    if escolha == 1:
        arr = list(map(int, input("Digite os números separados por espaço para ordenar: ").split()))
        start_time = time.time()

        arr = quick_sort(arr)

        end_time = time.time()
        print(f"Lista ordenada: {arr}")
        print(f"Tempo de execução: {end_time - start_time} segundos")

    elif escolha == 2:
        arr = list(map(int, input("Digite os números separados por espaço para a busca: ").split()))
        x = int(input("Digite o número a ser procurado: "))

        arr.sort()
        start_time = time.time()

        result = busca_binaria(arr, x)

        end_time = time.time()

        if result != -1:
            print(f"Elemento {x} encontrado na posição {result}.")
        else:
            print(f"Elemento {x} não encontrado.")

        print(f"Tempo de execução: {end_time - start_time} segundos")
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()
