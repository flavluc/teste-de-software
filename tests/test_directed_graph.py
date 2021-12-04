import pytest

from datalg.graph import DirectedGraph


@pytest.fixture
def directedGraph():
    return DirectedGraph()


def test_directed_empty(directedGraph):
    assert directedGraph.empty()


def test_directed_graph_adding_one_node_none_content(directedGraph):
    directedGraph.add_node(1, None)
    assert directedGraph.get_node_content(1) == None


def test_directed_graph_create_one_directed_egde(directedGraph):
    directedGraph.add_node(1, None)
    directedGraph.add_node(2, None)
    directedGraph.add_edge(1, 2)
    assert directedGraph.has_edge_between(1, 2)
    assert not directedGraph.has_edge_between(2, 1)


def test_adding_existent_node(directedGraph):
    directedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert directedGraph.add_node(1, None)


def test_adding_edge_for_unexistent_end_node(directedGraph):
    directedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert directedGraph.edge(1, 2)


def test_adding_edge_for_unexistent_start_node(directedGraph):
    directedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert directedGraph.edge(2, 1)


def test_removing_node(directedGraph):
    directedGraph.add_node(1, None)
    directedGraph.remove_node(1)
    assert directedGraph.empty()


def test_has_edge_between_for_unexistent_start_node(directedGraph):
    with pytest.raises(Exception) as _:
        assert directedGraph.has_edge_between(1, 0)


def test_has_edge_between_for_unexistent_end_node(directedGraph):
    directedGraph.add_node(1, None)
    with pytest.raises(Exception) as _:
        assert directedGraph.has_edge_between(1, 0)


def test_missing_edge_between_nodes(directedGraph):
    directedGraph.add_node(1, None)
    directedGraph.add_node(0, None)
    assert not directedGraph.has_edge_between(1, 0)


def test_if_has_edge_between_nodes(directedGraph):
    directedGraph.add_node(1, None)
    directedGraph.add_node(0, None)
    directedGraph.add_edge(0, 1)
    assert directedGraph.has_edge_between(0, 1)


def test_if_has_not_directed_edge_between_nodes(directedGraph):
    directedGraph.add_node(1, None)
    directedGraph.add_node(0, None)
    directedGraph.add_edge(0, 1)
    assert not directedGraph.has_edge_between(1, 0)


def test_removing_node_with_multiples_adjacencies(directedGraph):
    directedGraph.add_node(1, None)
    directedGraph.add_node(2, None)
    directedGraph.add_node(3, None)
    directedGraph.add_node(4, None)
    directedGraph.add_node(0, None)
    directedGraph.add_edge(0, 1)
    directedGraph.add_edge(0, 2)
    directedGraph.add_edge(0, 3)
    directedGraph.add_edge(0, 4)
    directedGraph.add_edge(4, 0)
    directedGraph.remove_node(0)
    directedGraph.add_node(0, None)
    assert not directedGraph.has_edge_between(4, 0)
