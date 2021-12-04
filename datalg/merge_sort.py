def merge_sort(array: list[int]) -> None:
    left = 0
    right = len(array) - 1
    _merge_sort(array, left, right)


def _merge_sort(array: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    mid = left + (right - left) // 2

    _merge_sort(array, left, mid)
    _merge_sort(array, mid + 1, right)

    return _merge(array, left, mid, right)


def _merge(array: list[int], left: int, mid: int, right: int) -> None:
    array_left = array[left : mid + 1]
    array_right = array[mid + 1 : right + 1]

    size_left = len(array_left)
    size_right = len(array_right)
    lo = hi = 0
    i = left

    while (lo < size_left) and (hi < size_right):
        if array_left[lo] < array_right[hi]:
            array[i] = array_left[lo]
            lo += 1
            i += 1
        else:
            array[i] = array_right[hi]
            hi += 1
            i += 1

    while lo < size_left:
        array[i] = array_left[lo]
        lo += 1
        i += 1
    while hi < size_right:
        array[i] = array_right[hi]
        hi += 1
        i += 1
