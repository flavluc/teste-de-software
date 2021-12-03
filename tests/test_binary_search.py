import pytest

from datalg.binary_search import binary_search, recursive_binary_search


@pytest.fixture
def array():
    return [i for i in range(11)]

@pytest.fixture
def empty_array():
    return []


def test_search_middle_element(array):
    assert binary_search(array, 5) == 5


def test_search_element_in_left_half(array):
    assert binary_search(array, 2) == 2


def test_search_element_in_right_half(array):
    assert binary_search(array, 7) == 7


def test_search_first_element(array):
    assert binary_search(array, 0) == 0


def test_search_last_element(array):
    assert binary_search(array, 10) == 10


def test_search_nonexisting_element(array):
    assert binary_search(array, 20) == -1


def test_search_in_empty_array(empty_array):
    assert binary_search(empty_array, 20) == -1


def test_recursive_search_middle_element(array):
    assert recursive_binary_search(array, 5) == 5


def test_recursive_search_element_in_left_half(array):
    assert recursive_binary_search(array, 2) == 2


def test_recursive_search_element_in_right_half(array):
    assert recursive_binary_search(array, 7) == 7


def test_recursive_search_first_element(array):
    assert recursive_binary_search(array, 0) == 0


def test_recursive_search_last_element(array):
    assert recursive_binary_search(array, 10) == 10


def test_recursive_search_nonexisting_element(array):
    assert recursive_binary_search(array, 20) == -1


def test_recursive_search_in_empty_array(empty_array):
    assert recursive_binary_search(empty_array, 20) == -1
