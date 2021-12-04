import pytest

from datalg.graph import UndirectedGraph

@pytest.fixture
def undirectedGraph():
    return UndirectedGraph()

def test_undirected_graph_empty(undirectedGraph):
    assert undirectedGraph.empty()

def test_undirected_grap_adding_one_node_none_content(undirectedGraph):
    undirectedGraph.add_node(1, None)
    assert undirectedGraph.get_node_content(1) == None

def test_undirected_graph_create_one_undirected_egde(undirectedGraph):
    undirectedGraph.add_node(1, None)
    undirectedGraph.add_node(2, None)
    undirectedGraph.add_edge(1, 2)
    assert undirectedGraph.has_edge_between(1, 2)
    assert undirectedGraph.has_edge_between(2, 1)
