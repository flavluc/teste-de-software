import pytest

from datalg.merge_sort import merge_sort


@pytest.fixture
def array():
    return []

def test_sort_empty(array):
    merge_sort(array)
    assert(array == [])

def test_sort_unsorted(array):
    for i in range(5, 0, -1):
        array.append(i)
    merge_sort(array)
    assert(array == [1,2,3,4,5])

def test_sort_sorted(array):
    for i in range(5):
        array.append(i)
    merge_sort(array)
    assert(array == [0,1,2,3,4])

def test_sort_repeated(array):
    array.append(2)
    for _ in range(3):
        array.append(1)
    array.append(0)
    merge_sort(array)
    assert(array == [0,1,1,1,2])
