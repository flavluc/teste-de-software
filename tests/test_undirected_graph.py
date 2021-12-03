import pytest

from datalg.graph import DirectedGraph


@pytest.fixture
def directedGraph():
    return DirectedGraph()


def test_empty(directedGraph):
    assert directedGraph.empty()


def test_adding_one_node_none_content(directedGraph):
    directedGraph.add_node(1, None)
    assert directedGraph.get_node_content(1) == None


def test_create_one_directed_egde(directedGraph):
    directedGraph.add_node(1, None)
    directedGraph.add_node(2, None)
    directedGraph.add_edge(1, 2)
    assert directedGraph.has_edge_between(1, 2) == True
    assert not directedGraph.has_edge_between(2, 1)
