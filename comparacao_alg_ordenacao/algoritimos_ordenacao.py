def shell_sort_comparisons(arr):
    comparisons = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr, comparisons


def merge_sort_comparisons(arr):
    def merge(arr, temp_arr, left, right):
        comparisons = 0
        if left == right:
            return comparisons
        mid = (left + right) // 2
        comparisons += merge(arr, temp_arr, left, mid)
        comparisons += merge(arr, temp_arr, mid + 1, right)
        comparisons += merge_sorted(arr, temp_arr, left, mid, right)
        return comparisons

    def merge_sorted(arr, temp_arr, left, mid, right):
        comparisons = 0
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            comparisons += 1
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
        return comparisons

    temp_arr = [0] * len(arr)
    comparisons = merge(arr, temp_arr, 0, len(arr) - 1)
    return arr, comparisons


def selection_sort_comparisons(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, comparisons


def quick_sort_comparisons(arr):
    comparisons = 0

    def quick_sort(arr, low, high):
        nonlocal comparisons
        if low < high:
            pi, comps = partition(arr, low, high)
            comparisons += comps
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        comparisons = 0
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1, comparisons

    quick_sort(arr, 0, len(arr) - 1)
    return arr, comparisons


def bucket_sort_comparisons(arr):
    comparisons = 0
    if len(arr) == 0:
        return arr, comparisons
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / len(arr) or 1
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index = min(int((num - min_val) // bucket_range), len(arr) - 1)
        buckets[index].append(num)
        comparisons += 1
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        sorted_arr.extend(sorted_bucket)
    return sorted_arr, comparisons


def radix_sort_comparisons(arr):
    comparisons = 0

    def counting_sort(arr, exp1):
        nonlocal comparisons
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = arr[i] // exp1
            count[index % 10] += 1
            comparisons += 1
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
        nonlocal comparisons
        max1 = max(arr)
        exp = 1
        while max1 // exp > 0:
            counting_sort(arr, exp)
            exp *= 10

    radix_sort(arr)
    return arr, comparisons
