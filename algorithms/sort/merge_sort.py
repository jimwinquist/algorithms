def merge_sort(arr):
    if arr is None or len(arr) < 2:
        return arr
    aux = arr[:]

    return sort(arr, aux, 0, len(arr) - 1)

def sort(arr, aux, lo, hi):
    if lo < hi:
        mid = lo + (hi - lo) / 2
        sort(arr, aux, lo, mid)
        sort(arr, aux, mid + 1, hi)
        merge(arr, aux, lo, mid, hi)

    return arr

def merge(arr, aux, lo, mid, hi):
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        aux[k] = arr[k]

    for k in range(lo, hi+1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1


if __name__ == "__main__":
    assert(merge_sort([]) == [])
    assert(merge_sort(None) is None)
    assert(merge_sort([1]) == [1])
    assert(merge_sort([4, 0, 2, 5, 1, 3]) == [0, 1, 2, 3, 4, 5])
    assert(merge_sort([7, 4, 6, 5, 3, 5, 4, 2, 4, 1]) == [1, 2, 3, 4, 4, 4, 5, 5, 6, 7])
