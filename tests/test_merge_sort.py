import pytest

from datalg.merge_sort import merge_sort, merge_sort_inplace


@pytest.fixture
def array():
    return []

@pytest.fixture
def unsorted_array():
    return [5,4,3,2,1]

@pytest.fixture
def sorted_array():
    return [1,2,3,4,5]

def test_merge_sort_empty(array):
    merge_sort(array)
    assert array == []


def test_merge_sort_unsorted(array):
    for i in range(5, 0, -1):
        array.append(i)
    merge_sort(array)
    assert array == [1, 2, 3, 4, 5]


def test_merge_sort_sorted(array):
    for i in range(5):
        array.append(i)
    merge_sort(array)
    assert array == [0, 1, 2, 3, 4]


def test_merge_sort_repeated(array):
    array.append(2)
    for _ in range(3):
        array.append(1)
    array.append(0)
    merge_sort(array)
    assert array == [0, 1, 1, 1, 2]


def test_merge_sort_inplace_empty(array):
    copy_array = array.copy()
    merge_sort_inplace(copy_array)
    assert copy_array == array


def test_merge_sort_unsorted(array):
    copy_array = array.copy()
    merge_sort(array)
    assert array == [1, 2, 3, 4, 5]


def test_merge_sort_sorted(array):
    for i in range(5):
        array.append(i)
    merge_sort(array)
    assert array == [0, 1, 2, 3, 4]


def test_merge_sort_repeated(array):
    array.append(2)
    for _ in range(3):
        array.append(1)
    array.append(0)
    merge_sort(array)
    assert array == [0, 1, 1, 1, 2]
