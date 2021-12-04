import pytest

from datalg.linked_list import LinkedList


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def sorted_list():
    sorted_list = LinkedList()
    for i in range(11):
        sorted_list.insert_tail(i)
    return sorted_list


def test_empty(empty_list):
    assert empty_list.empty()


def test_insert_head_empty_list(empty_list):
    empty_list.insert_head(0)
    assert empty_list.to_python_list() == [0]


def test_insert_tail_empty_list(empty_list):
    empty_list.insert_tail(0)
    assert empty_list.to_python_list() == [0]


def test_insert_nth_empty_list(empty_list):
    empty_list.insert_nth(0, 0)
    assert empty_list.to_python_list() == [0]