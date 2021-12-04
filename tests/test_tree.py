import pytest

from datalg.tree import Tree

@pytest.fixture
def tree():
    return Tree(0, None)

def test_tree_creation(tree):
    assert tree.get_path_until(0) == [0]
    assert tree.get_node_content(0) is None

def test_tree_correct_path(tree):
    tree.add_node(0, 1, None)
    tree.add_node(1, 2, None)
    tree.add_node(1, 3, None)
    tree.add_node(1, 4, None)
    tree.add_node(2, 5, None)
    tree.add_node(5, 6, None)
    tree.add_node(2, 7, None)
    tree.add_node(0, 8, None)

    assert tree.get_path_until(8) == [0, 8]

def test_tree_path_for_unexistent_node(tree):
    with pytest.raises(Exception) as  exception_info:
        tree.get_path_until(10)
    
def test_content_updating(tree):
    tree.update_node_content(0, 1000)
    assert tree.get_node_content(0) == 1000

def test_content_updating_for_unexistent_node(tree):
    with pytest.raises(Exception) as  exception_info:
        tree.update_node_content(1, None)

def test_adding_node_to_unexistent_parent(tree):
    with pytest.raises(Exception) as  exception_info:
        tree.add_node(1, 2, None)

def test_node_is_not_leaf(tree):
    tree.add_node(0, 1, None)
    assert not tree.is_leaf(0)

def test_node_is_leaf(tree):
    tree.add_node(0, 1, None)
    assert tree.is_leaf(1)

def test_node_is_leaf_for_unexistent_node(tree):
    with pytest.raises(Exception) as  exception_info:
        assert tree.is_leaf(1)

def test_getting_node_content_for_unexistent_node(tree):
    with pytest.raises(Exception) as  exception_info:
        assert tree.get_node_content(1)

def test_adding_repeating_node(tree):
    with pytest.raises(Exception) as  exception_info:
        assert tree.add_node(0, 0, None)