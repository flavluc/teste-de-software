import pytest

from datalg.dfs import dfs
from datalg.graph import DirectedGraph, UndirectedGraph
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


@pytest.fixture
def tree():
    g = Tree()
    for i in range(5):
        g.add_node(i, None)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    return g


def test_dfs_graph_single_node():
    graph = DirectedGraph()
    graph.add_node(0, None)
    assert dfs(graph, 0) == [0]


def test_dfs_graph_no_edge():
    graph = DirectedGraph()
    graph.add_node(0, None)
    graph.add_node(1, None)
    assert dfs(graph, 0) == [0]


def test_dfs_directed_graph(directed_graph):
    traversal = dfs(directed_graph, 0)
    assert (traversal == [0, 1, 3, 2, 4]) | (traversal == [0, 2, 4, 1, 3])


def test_dfs_directed_graph_start_on_leaf(directed_graph):
    traversal = dfs(directed_graph, 4)
    assert traversal == [4]


def test_dfs_directed_graph_cicle(directed_graph):
    directed_graph.add_edge(1, 2)
    traversal = dfs(directed_graph, 0)
    assert (
        (traversal == [0, 1, 3, 2, 4])
        | (traversal == [0, 2, 4, 1, 3])
        | (traversal == [0, 1, 2, 4, 3])
    )


def test_dfs_does_not_change_graph(directed_graph):
    dfs(directed_graph, 0)
    assert directed_graph.has_edge_between(0, 1)
    assert directed_graph.has_edge_between(0, 2)
    assert directed_graph.has_edge_between(1, 3)
    assert directed_graph.has_edge_between(2, 4)


def test_dfs_undirected_graph_cicle(undirected_graph):
    undirected_graph.add_edge(1, 2)
    traversal = dfs(undirected_graph, 0)
    assert (
        (traversal == [0, 1, 3, 2, 4])
        | (traversal == [0, 2, 4, 1, 3])
        | (traversal == [0, 1, 2, 4, 3])
        | (traversal == [0, 2, 1, 3, 4])
    )


def test_dfs_undirected_graph(undirected_graph):
    traversal = dfs(undirected_graph, 0)
    assert (traversal == [0, 1, 3, 2, 4]) | (traversal == [0, 2, 4, 1, 3])


def test_dfs_undirected_graph_start_on_leaf(undirected_graph):
    traversal = dfs(undirected_graph, 4)
    assert traversal == [4, 2, 0, 1, 3]


def test_dfs_tree_single_node():
    tree = Tree()
    tree.add_node(0, None)
    assert dfs(tree, 0) == [0]


def test_dfs_tree(tree):
    traversal = dfs(tree, 0)
    assert (traversal == [0, 1, 3, 2, 4]) | (traversal == [0, 2, 4, 1, 3])
