import pytest

from datalg.linked_list import LinkedList


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def sorted_list():
    sorted_list = LinkedList()
    for i in range(5):
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


def test_insert_out_of_index(sorted_list):
    with pytest.raises(Exception):
        sorted_list.insert_nth(0,20)


def test_insert_head(sorted_list):
    sorted_list.insert_head(0)
    assert sorted_list.to_python_list() == [0,0,1,2,3,4]


def test_insert_tail(sorted_list):
    sorted_list.insert_tail(0)
    assert sorted_list.to_python_list() == [0,1,2,3,4,0]


def test_insert_nth(sorted_list):
    sorted_list.insert_nth(0, 3)
    assert sorted_list.to_python_list() == [0,1,2,0,3,4]


def test_insert_nth_head(sorted_list):
    sorted_list.insert_nth(0,0)
    assert sorted_list.to_python_list() == [0,0,1,2,3,4]


def test_insert_nth_tail(sorted_list):
    sorted_list.insert_nth(0,5)
    assert sorted_list.to_python_list() == [0,1,2,3,4,0]


def test_delete_empty_list(empty_list):
    with pytest.raises(Exception):
        empty_list.delete_head()


def test_delete_out_of_index(sorted_list):
    with pytest.raises(Exception):
        sorted_list.delete_nth(20)


def test_delete_head(sorted_list):
    deleted = sorted_list.delete_head()
    assert deleted.content == 0
    assert sorted_list.to_python_list() == [1,2,3,4]


def test_delete_tail(sorted_list):
    deleted = sorted_list.delete_tail()
    assert deleted.content == 4
    assert sorted_list.to_python_list() == [0,1,2,3]


def test_delete_nth(sorted_list):
    deleted = sorted_list.delete_nth(3)
    assert deleted.content == 3
    assert sorted_list.to_python_list() == [0,1,2,4]


def test_delete_nth_head(sorted_list):
    deleted = sorted_list.delete_nth(0)
    assert deleted.content == 0
    assert sorted_list.to_python_list() == [1,2,3,4]


def test_delete_nth_tail(sorted_list):
    deleted = sorted_list.delete_nth(4)
    assert deleted.content == 4
    assert sorted_list.to_python_list() == [0,1,2,3]
