def binary_search(sorted_list: list[int], key: int) -> int:
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if sorted_list[mid] == key:
            return mid
        elif key > mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def recursive_binary_search(sorted_list: list[int], key: int) -> int:
    left = 0
    right = len(sorted_list) - 1

    return binary_search_recursive_step(sorted_list, key, left, right)


def binary_search_recursive_step(
    sorted_list: list[int], key: int, left: int, right: int
) -> int:
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if sorted_list[mid] == key:
        return mid

    if key > mid:
        return binary_search_recursive_step(sorted_list, key, mid + 1, right)

    return binary_search_recursive_step(sorted_list, key, left, mid - 1)
