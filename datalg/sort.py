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
