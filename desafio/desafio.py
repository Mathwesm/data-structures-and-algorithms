import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


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

        result = binary_search(arr, x)

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
