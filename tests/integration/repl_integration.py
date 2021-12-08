import pytest

from repl import Repl
from datalg.stack import Stack
from datalg.graph import DirectedGraph
from datalg.queue import Queue

@pytest.fixture
def repl():
    return Repl(dict())

def test_empty_repl(repl):
    assert len(repl.history) == 0
    assert len(repl.env) == 0

def test_stack_creation(repl):
    repl.create_stack(Stack(), 'A')
    assert 'A' in repl.env
    assert isinstance(repl.env['A'] , Stack)
    assert repl.env['A'].empty()

def test_not_empty_at_stack_in_repl(repl):
    st = Stack()
    repl.create_stack(st, 'A')
    repl.addStack_element(1, 'A')
    assert not st.empty()

def test_elements_matching_at_stack_in_repl(repl):
    st = Stack()
    repl.create_stack(st, 'A')
    repl.add_stack_element(1, 'A')
    assert st.peek() == 1

def test_stack_elements_push_ordering(repl):
    st = Stack()
    repl.create_stack(st, 'A')
    repl.addStack_element(1, 'A')
    repl.addStack_element(2, 'A')
    assert st.pop() == 2
    assert st.pop() == 1

def test_multiple_data_strucures_creation(repl):
    repl.create_stack(DirectedGraph(), 'G')
    repl.create_stack(Queue(), 'Q')
    assert isinstance(repl.env['G'] , DirectedGraph)
    assert isinstance(repl.env['Q'] , Queue)

