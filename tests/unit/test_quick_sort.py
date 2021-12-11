import pytest

from datalg.quick_sort import quicksort, quicksort_inplace


@pytest.fixture
def empty_array():
    return []


@pytest.fixture
def sorted_array():
    return [1, 2, 4, 7, 8, 9]


@pytest.fixture
def array():
    return [6, 1, 3, 6, 9, 4]


def test_quicksort_empty(empty_array):
    assert quicksort(empty_array) == empty_array


def test_quicksort_sorted(sorted_array):
    assert quicksort(sorted_array) == sorted_array


def test_quicksort_maintains_size(array):
    assert len(quicksort(array)) == len(array)


def test_quicksort_unsorted(array):
    assert quicksort(array) == [1, 3, 4, 6, 6, 9]


def test_quicksort_inplace_empty(empty_array):
    copy_array = empty_array.copy()
    quicksort_inplace(copy_array)
    assert copy_array == empty_array


def test_quicksort_inplace_sorted(sorted_array):
    copy_array = sorted_array.copy()
    quicksort_inplace(copy_array)
    assert copy_array == sorted_array


def test_quicksort_inplace_maintains_size(array):
    copy_array = array.copy()
    quicksort_inplace(copy_array)
    assert len(copy_array) == len(array)


def test_quicksort_inplace_unsorted(array):
    copy_array = array.copy()
    quicksort_inplace(copy_array)
    assert copy_array == [1, 3, 4, 6, 6, 9]
