def insertion_sort(arr):
    if arr is None or len(arr) < 2:
        return arr

    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    assert(insertion_sort([]) == [])
    assert(insertion_sort(None) is None)
    assert(insertion_sort([1]) == [1])
    assert(insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
    assert(insertion_sort([7, 4, 6, 5, 3, 5, 4, 2, 4, 1]) == [1, 2, 3, 4, 4, 4, 5, 5, 6, 7])

