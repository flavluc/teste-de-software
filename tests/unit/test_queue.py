import pytest

from datalg.queue import Queue


@pytest.fixture
def queue():
    return Queue()


def test_begin_empty(queue):
    assert queue.empty()


def test_not_empty_after_enqueue(queue):
    queue.enqueue(1)
    assert not queue.empty()
    assert queue.front() == 1


def test_empty_after_dequeue(queue):
    queue.enqueue(1)
    assert queue.dequeue() == 1
    assert queue.empty()


def test_front_is_FIFO(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front() == 1


def test_dequeue_is_FIFO(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_size_after_enqueue_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.size() == 0


def test_empty_serialization(queue):
    assert str(queue) == "[]"


def test_populated_serialization(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert str(queue) == "[1, 2]"


def test_to_list(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.to_list() == [1, 2, 3]
