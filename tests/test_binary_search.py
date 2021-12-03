import pytest

from datalg.binary_search import binary_search, recursive_binary_search


@pytest.fixture
def array():
    return []


def test_search_middle_element(array):
    for i in range(11):
        array.append(i)
    assert binary_search(array, 5) == 5


def test_search_element_in_left_half(array):
    for i in range(10):
        array.append(i)
    assert binary_search(array, 2) == 2


def test_search_element_in_right_half(array):
    for i in range(10):
        array.append(i)
    assert binary_search(array, 7) == 7


def test_search_first_element(array):
    for i in range(10):
        array.append(i)
    assert binary_search(array, 0) == 0


def test_search_last_element(array):
    for i in range(10):
        array.append(i)
    assert binary_search(array, 9) == 9


def test_search_nonexisting_element(array):
    for i in range(10):
        array.append(i)
    assert binary_search(array, 20) == -1


def test_search_in_empty_array(array):
    assert binary_search(array, 20) == -1


def test_recursive_search_middle_element(array):
    for i in range(11):
        array.append(i)
    assert recursive_binary_search(array, 5) == 5


def test_recursive_search_element_in_left_half(array):
    for i in range(10):
        array.append(i)
    assert recursive_binary_search(array, 2) == 2


def test_recursive_search_element_in_right_half(array):
    for i in range(10):
        array.append(i)
    assert recursive_binary_search(array, 7) == 7


def test_recursive_search_first_element(array):
    for i in range(10):
        array.append(i)
    assert recursive_binary_search(array, 0) == 0


def test_recursive_search_last_element(array):
    for i in range(10):
        array.append(i)
    assert recursive_binary_search(array, 9) == 9


def test_recursive_search_nonexisting_element(array):
    for i in range(10):
        array.append(i)
    assert recursive_binary_search(array, 20) == -1


def test_recursive_search_in_empty_array(array):
    assert recursive_binary_search(array, 20) == -1
