

def ordenacao_shell_comparacoes(arr):
    comparacoes = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparacoes += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr, comparacoes


def ordenacao_merge_comparacoes(arr):
    def merge(arr, temp_arr, left, right):
        comparacoes = 0
        if left == right:
            return comparacoes
        mid = (left + right) // 2
        comparacoes += merge(arr, temp_arr, left, mid)
        comparacoes += merge(arr, temp_arr, mid + 1, right)
        comparacoes += merge_sorted(arr, temp_arr, left, mid, right)
        return comparacoes

    def merge_sorted(arr, temp_arr, left, mid, right):
        comparacoes = 0
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            comparacoes += 1
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                j += 1
            k += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
        return comparacoes

    temp_arr = [0] * len(arr)
    comparacoes = merge(arr, temp_arr, 0, len(arr) - 1)
    return arr, comparacoes


def ordenacao_selecao_comparacoes(arr):
    comparacoes = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, comparacoes


def ordenacao_quick_comparacoes(arr):
    comparacoes = 0

    def quick_sort(arr, low, high):
        nonlocal comparacoes
        if low < high:
            pi, comps = partition(arr, low, high)
            comparacoes += comps
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        comparacoes = 0
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparacoes += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1, comparacoes

    quick_sort(arr, 0, len(arr) - 1)
    return arr, comparacoes


def ordenacao_bucket_comparacoes(arr):
    comparacoes = 0
    if len(arr) == 0:
        return arr, comparacoes
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / len(arr) or 1
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index = min(int((num - min_val) // bucket_range), len(arr) - 1)
        buckets[index].append(num)
        comparacoes += 1
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        sorted_arr.extend(sorted_bucket)
    return sorted_arr, comparacoes


def ordenacao_radix_comparacoes(arr):
    comparacoes = 0

    def counting_sort(arr, exp1):
        nonlocal comparacoes
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = arr[i] // exp1
            count[index % 10] += 1
            comparacoes += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]

    def radix_sort(arr):
        nonlocal comparacoes
        max1 = max(arr)
        exp = 1
        while max1 // exp > 0:
            counting_sort(arr, exp)
            exp *= 10

    radix_sort(arr)
    return arr, comparacoes
