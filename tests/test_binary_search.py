import pytest

from datalg.binary_search import binary_search, recursive_binary_search


@pytest.fixture
def stack():
    return []


def test_search_middle_element(stack):
    for i in range(11):
        stack.append(i)
    assert binary_search(stack, 5) == 5


def test_search_element_in_left_half(stack):
    for i in range(10):
        stack.append(i)
    assert binary_search(stack, 2) == 2


def test_search_element_in_right_half(stack):
    for i in range(10):
        stack.append(i)
    assert binary_search(stack, 7) == 7


def test_search_first_element(stack):
    for i in range(10):
        stack.append(i)
    assert binary_search(stack, 0) == 0


def test_search_last_element(stack):
    for i in range(10):
        stack.append(i)
    assert binary_search(stack, 9) == 9


def test_search_nonexisting_element(stack):
    for i in range(10):
        stack.append(i)
    assert binary_search(stack, 20) == -1


def test_search_in_empty_stack(stack):
    assert binary_search(stack, 20) == -1


def test_recursive_search_middle_element(stack):
    for i in range(11):
        stack.append(i)
    assert recursive_binary_search(stack, 5) == 5


def test_recursive_search_element_in_left_half(stack):
    for i in range(10):
        stack.append(i)
    assert recursive_binary_search(stack, 2) == 2


def test_recursive_search_element_in_right_half(stack):
    for i in range(10):
        stack.append(i)
    assert recursive_binary_search(stack, 7) == 7


def test_recursive_search_first_element(stack):
    for i in range(10):
        stack.append(i)
    assert recursive_binary_search(stack, 0) == 0


def test_recursive_search_last_element(stack):
    for i in range(10):
        stack.append(i)
    assert recursive_binary_search(stack, 9) == 9


def test_recursive_search_nonexisting_element(stack):
    for i in range(10):
        stack.append(i)
    assert recursive_binary_search(stack, 20) == -1


def test_recursive_search_in_empty_stack(stack):
    assert recursive_binary_search(stack, 20) == -1
