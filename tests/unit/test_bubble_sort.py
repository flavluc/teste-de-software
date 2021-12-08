import pytest

from datalg.bubble_sort import bubble_sort


@pytest.fixture
def empty_array():
    return []


@pytest.fixture
def sorted_array():
    return [1, 2, 4, 7, 8, 9]


@pytest.fixture
def array():
    return [6, 1, 3, 6, 9, 4]


def test_sort_empty(empty_array):
    bubble_sort(empty_array)
    assert empty_array == empty_array


def test_sort_sorted(sorted_array):
    bubble_sort(sorted_array)
    assert sorted_array == sorted_array


def test_sort_maintains_size(array):
    old_len = len(array)
    bubble_sort(array)
    assert len(array) == old_len


def test_sort_unsorted(array):
    bubble_sort(array)
    assert array == [1, 3, 4, 6, 6, 9]


def test_sort_repeated(empty_array):
    empty_array.append(2)
    for _ in range(3):
        empty_array.append(1)
    empty_array.append(0)
    bubble_sort(empty_array)
    assert empty_array == [0, 1, 1, 1, 2]
