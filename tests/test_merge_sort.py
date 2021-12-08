import pytest

from datalg.merge_sort import merge_sort, merge_sort_inplace


@pytest.fixture
def empty_array():
    return []


@pytest.fixture
def sorted_array():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def repeated_array():
    return [2, 5, 2, 8, 3, 8]


@pytest.fixture
def array():
    return [5, 4, 3, 2, 1]


def test_mergesort_empty(empty_array):
    assert merge_sort(empty_array) == empty_array


def test_mergesort_sorted(sorted_array):
    assert merge_sort(sorted_array) == sorted_array


def test_mergesort_maintains_size(array):
    assert len(merge_sort(array)) == len(array)


def test_mergesort_repeated(repeated_array):
    assert merge_sort(repeated_array) == [2, 2, 3, 5, 8, 8]


def test_mergesort_unsorted(array):
    assert merge_sort(array) == [1, 2, 3, 4, 5]


def test_mergesort_inplace_empty(empty_array):
    copy_array = empty_array.copy()
    merge_sort_inplace(copy_array)
    assert copy_array == empty_array


def test_mergesort_inplace_sorted(sorted_array):
    copy_array = sorted_array.copy()
    merge_sort_inplace(copy_array)
    assert copy_array == sorted_array


def test_mergesort_inplace_maintains_size(array):
    copy_array = array.copy()
    merge_sort_inplace(copy_array)
    assert len(copy_array) == len(array)


def test_mergesort_inplace_repeated(repeated_array):
    copy_array = repeated_array.copy()
    merge_sort_inplace(copy_array)
    assert copy_array == [2, 2, 3, 5, 8, 8]


def test_mergesort_inplace_unsorted(array):
    copy_array = array.copy()
    merge_sort_inplace(copy_array)
    assert copy_array == [1, 2, 3, 4, 5]
