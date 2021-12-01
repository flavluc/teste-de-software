import pytest

from datalg.stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_empty(stack):
    assert stack.empty()


def test_push(stack):
    stack.push(1)
    assert stack.pop() == 1
