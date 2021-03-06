import sys

import pytest

from datalg.graph import DirectedGraph, UndirectedGraph
from datalg.queue import Queue
from datalg.stack import Stack
from repl.repl import Repl


@pytest.fixture
def repl():
    return Repl(sys.stdout)


def test_empty_repl(repl):
    assert repl.history.empty()
    assert len(repl.env) == 0


def test_stack_creation(repl):
    repl.create("A", Stack())
    assert "A" in repl.env
    assert isinstance(repl.env["A"], Stack)
    assert repl.env["A"].empty()


def test_not_empty_at_stack_in_repl(repl):
    st = Stack()
    repl.create("A", st)
    repl.add_stack_element("A", 1)
    assert not st.empty()


def test_elements_matching_at_stack_in_repl(repl):
    st = Stack()
    repl.create("A", st)
    repl.add_stack_element("A", 1)
    assert st.peek() == 1


def test_stack_elements_push_ordering(repl):
    st = Stack()
    repl.create("A", st)
    repl.add_stack_element("A", 1)
    repl.add_stack_element("A", 2)
    assert st.pop() == 2
    assert st.pop() == 1


def test_multiple_data_strucures_creation(repl):
    repl.create("G", DirectedGraph())
    repl.create("Q", Queue())
    assert isinstance(repl.env["G"], DirectedGraph)
    assert isinstance(repl.env["Q"], Queue)


def test_create_undirected_graph_with_two_connected_nodes(repl):
    repl.create("G", UndirectedGraph())
    repl.add_graph_node("G", 1)
    repl.add_graph_node("G", 2)
    repl.add_graph_edge("G", 1, 2)
    assert repl.bfs_path("G", 2) == "[2, 1]"
