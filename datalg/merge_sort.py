def merge_sort(array: list[int]) -> None:
    left = 0
    right = len(array) - 1
    _merge_sort(array, left, right)


def _merge_sort(array: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    mid = left + (right - left) // 2

    _merge_sort(array, left, mid)
    _merge_sort(array, mid+1, right)

    return _merge(array, left, mid, right)


def _merge(array: list[int], left: int, mid: int, right: int) -> None:
    array_left = array[left:mid+1]
    array_right = array[mid+1:right+1]

    size_left = len(array_left)
    size_right = len(array_right)
    l = r = 0
    i = left

    while (l < size_left) and (r < size_right):
        if array_left[l] < array_right[r]:
            array[i] = array_left[l]
            l += 1
            i += 1
        else:
            array[i] = array_right[r]
            r += 1
            i += 1

    while l < size_left:
        array[i] = array_left[l]
        l += 1
        i += 1
    while r < size_right:
        array[i] = array_right[r]
        r += 1
        i += 1
        