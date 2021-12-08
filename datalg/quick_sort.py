import random


def _find_pivot(array):
    return array[len(array) // 2]


def _quicksort(array):
    pivot = _find_pivot(array)
    smallers = [e for e in array if e < pivot]
    equals = [e for e in array if e == pivot]
    greaters = [e for e in array if e > pivot]
    return quicksort(smallers) + equals + quicksort(greaters)


def quicksort(array):
    if not array:
        return array
    return _quicksort(array)


def _sub_partition(array, start, end, idx_pivot):

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quicksort_inplace(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    pivot = random.randint(start, end)
    i = _sub_partition(array, start, end, pivot)
    quicksort_inplace(array, start, i - 1)
    quicksort_inplace(array, i + 1, end)
