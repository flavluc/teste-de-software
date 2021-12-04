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


def test_adding_existent_node(undirectedGraph):
    undirectedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert undirectedGraph.add_node(1, None)


def test_adding_edge_for_unexistent_end_node(undirectedGraph):
    undirectedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert undirectedGraph.edge(1, 2)


def test_adding_edge_for_unexistent_start_node(undirectedGraph):
    undirectedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert undirectedGraph.edge(2, 1)


def test_removing_node(undirectedGraph):
    undirectedGraph.add_node(1, None)
    undirectedGraph.remove_node(1)
    assert undirectedGraph.empty()


def test_has_edge_between_for_unexistent_start_node(undirectedGraph):
    with pytest.raises(Exception) as _:
        assert undirectedGraph.has_edge_between(1, 0)


def test_has_edge_between_for_unexistent_end_node(undirectedGraph):
    undirectedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert undirectedGraph.has_edge_between(1, 0)


def test_missing_edge_between_nodes(undirectedGraph):
    undirectedGraph.add_node(1, None)
    undirectedGraph.add_node(0, None)
    assert not undirectedGraph.has_edge_between(1, 0)


def test_if_has_edge_between_nodes(undirectedGraph):
    undirectedGraph.add_node(1, None)
    undirectedGraph.add_node(0, None)
    undirectedGraph.add_edge(0, 1)
    assert undirectedGraph.has_edge_between(0, 1)


def test_removing_node_with_multiples_adjacencies(undirectedGraph):
    undirectedGraph.add_node(1, None)
    undirectedGraph.add_node(2, None)
    undirectedGraph.add_node(3, None)
    undirectedGraph.add_node(4, None)
    undirectedGraph.add_node(0, None)
    undirectedGraph.add_edge(0, 1)
    undirectedGraph.add_edge(0, 2)
    undirectedGraph.add_edge(0, 3)
    undirectedGraph.add_edge(0, 4)
    undirectedGraph.add_edge(4, 0)
    undirectedGraph.remove_node(0)
    undirectedGraph.add_node(0, None)
    assert not undirectedGraph.has_edge_between(4, 0)
