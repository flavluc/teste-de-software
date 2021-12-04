import pytest

from datalg.sort import quicksort


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
    assert quicksort(empty_array) == empty_array


def test_sort_sorted(sorted_array):
    assert quicksort(sorted_array) == sorted_array


def test_sort_maintains_size(array):
    assert len(quicksort(array)) == len(array)


def test_sort_unsorted(array):
    assert quicksort(array) == [1, 3, 4, 6, 6, 9]
