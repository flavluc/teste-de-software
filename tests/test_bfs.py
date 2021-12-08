import pytest

from datalg.bfs import bfs
from datalg.graph import UndirectedGraph, DirectedGraph
from datalg.tree import Tree


@pytest.fixture
def directed_graph():
    g = DirectedGraph()
    for i in range(5):
        g.add_node(i, None)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    return g


@pytest.fixture
def undirected_graph():
    g = UndirectedGraph()
    for i in range(5):
        g.add_node(i, None)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    return g


def test_bfs_single_node():
    graph = DirectedGraph()
    graph.add_node(0, None)
    assert bfs(graph, 0) == [0]


def test_bfs_no_edge():
    graph = DirectedGraph()
    graph.add_node(0, None)
    graph.add_node(1, None)
    assert bfs(graph, 0) == [0]


def test_bfs_directed_graph(directed_graph):
    traversal = bfs(directed_graph, 0)
    assert (traversal == [0, 1, 2, 3, 4]) | (traversal == [0, 2, 1, 4, 3])


def test_bfs_directed_graph_start_on_leaf(directed_graph):
    traversal = bfs(directed_graph, 4)
    assert traversal == [4]


def test_bfs_directed_graph_cicle(directed_graph):
    directed_graph.add_edge(1, 2)
    traversal = bfs(directed_graph, 0)
    assert (traversal == [0, 1, 2, 3, 4]) | (traversal == [0, 2, 1, 4, 3])


def test_bfs_does_not_change_graph(directed_graph):
    traversal = bfs(directed_graph, 0)
    assert directed_graph.has_edge_between(0, 1)
    assert directed_graph.has_edge_between(0, 2)
    assert directed_graph.has_edge_between(1, 3)
    assert directed_graph.has_edge_between(2, 4)


def test_bfs_undirected_graph_cicle(undirected_graph):
    undirected_graph.add_edge(1, 2)
    traversal = bfs(undirected_graph, 0)
    assert (traversal == [0, 1, 2, 3, 4]) | (traversal == [0, 2, 1, 4, 3])


def test_bfs_undirected_graph(undirected_graph):
    traversal = bfs(undirected_graph, 0)
    assert (traversal == [0, 1, 2, 3, 4]) | (traversal == [0, 2, 1, 4, 3])


def test_bfs_undirected_graph_start_on_leaf(undirected_graph):
    traversal = bfs(undirected_graph, 4)
    assert traversal == [4, 2, 0, 1, 3]


def test_bfs_tree_single_node():
    tree = Tree()
    tree.add_node(0, None)
    assert bfs(tree, 0) == [0]


def test_bfs_tree(tree):
    traversal = bfs(tree, 0)
    assert (traversal == [0, 1, 2, 3, 4]) | (traversal == [0, 2, 1, 4, 3])
