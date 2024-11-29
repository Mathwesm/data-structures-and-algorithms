import time
import random

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


        if len(arr) <= 10:
            print(f"Iteração {i + 1}: {arr}")

    return arr

def measure_time(func, arr, iterations=10):
    start = time.perf_counter()
    for _ in range(iterations):
        result = func(arr)
    end = time.perf_counter()
    avg_time = (end - start) / iterations
    return avg_time

# Testando com lista pequena
arr_small = [64, 25, 12, 22, 11]
print("Lista original (pequena):", arr_small)
sorted_arr_small = selection_sort(arr_small)
print("\nLista ordenada (pequena):", sorted_arr_small)

# Testando com lista média
arr_medium = random.sample(range(1, 1001), 100)  # Lista média de tamanho 100
time_taken_medium = measure_time(selection_sort, arr_medium, iterations=1)
print(f"\nTempo de execução para lista média: {time_taken_medium:.6f} segundos")

# Testando com lista grande
arr_large = random.sample(range(1, 10001), 1000)  # Lista grande de tamanho 1000
time_taken_large = measure_time(selection_sort, arr_large, iterations=1)
print(f"\nTempo de execução para lista grande: {time_taken_large:.6f} segundos")
