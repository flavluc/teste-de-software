import pytest

from datalg.stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_begin_empty(stack):
    assert stack.empty()


def test_not_empty_after_push(stack):
    stack.push(1)
    assert not stack.empty()
    assert stack.peek() == 1


def test_empty_after_pop(stack):
    stack.push(1)
    assert stack.pop() == 1
    assert stack.empty()


def test_peek_is_LIFO(stack):
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2


def test_pop_is_LIFO(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_size_after_push_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.size() == 0


def test_serialization(stack):
    assert str(stack) == "[]"
    stack.push(1)
    stack.push(2)
    assert str(stack) == "[1, 2]"
