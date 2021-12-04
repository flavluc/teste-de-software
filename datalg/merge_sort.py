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


def merge_sort_inplace(arr, left, right):
    if (left < right):

        mid = left + (right - left) // 2

        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)

        _merge_inplace(arr, left, mid, right)


def _merge_inplace(arr, start, mid, end):
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return

    while (start <= mid and start2 <= end):

        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2

            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1
