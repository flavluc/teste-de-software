from io import StringIO

import pytest

from repl.repl import Repl


@pytest.fixture
def repl_ostream():
    ostream = StringIO()
    return Repl(ostream), ostream


def test_empty_repl(repl_ostream):
    (repl, ostream) = repl_ostream
    assert repl.history.empty()
    assert len(repl.env) == 0


def test_repl_stack_creation(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create stack S")
    repl.eval("add S 1")
    repl.eval("remove S")
    assert ostream.getvalue() == "1\n"


def test_repl_check_stack_with_two_elements(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create stack S")
    repl.eval("add S 1")
    repl.eval("add S 2")
    repl.eval("remove S")
    assert ostream.getvalue() == "2\n"
    ostream.seek(0)
    ostream.truncate(0)
    repl.eval("remove S")
    assert ostream.getvalue() == "1\n"


def test_repl_undirected_graph_creation(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create undirected_graph G")
    repl.eval("add G node 1")
    repl.eval("add G node 2")
    repl.eval("add G edge 2 1")
    repl.eval("remove G 2")
    assert ostream.getvalue() == "2\n"


def test_repl_directed_graph_creation(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create directed_graph G")
    repl.eval("add G node 1")
    repl.eval("add G node 2")
    repl.eval("add G edge 2 1")
    repl.eval("remove G 2")
    assert ostream.getvalue() == "2\n"


def test_undirected_graph_bfs(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create undirected_graph G")
    repl.eval("add G node 1")
    repl.eval("add G node 2")
    repl.eval("add G edge 2 1")
    repl.eval("search bfs G 2")
    assert ostream.getvalue() == "[2, 1]\n"


def test_undirected_graph_dfs(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create undirected_graph G")
    repl.eval("add G node 1")
    repl.eval("add G node 2")
    repl.eval("add G edge 2 1")
    repl.eval("search dfs G 2")
    assert ostream.getvalue() == "[2, 1]\n"


def test_repl_queue_creation(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create queue Q")
    repl.eval("add Q 1")
    repl.eval("add Q 2")
    repl.eval("remove Q")
    assert ostream.getvalue() == "1\n"


def test_repl_list_removing_from_tail(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create list L")
    repl.eval("add L 1 head")
    repl.eval("add L 2 head")
    repl.eval("remove L tail")
    assert ostream.getvalue() == "1\n"
    ostream.seek(0)
    ostream.truncate(0)
    repl.eval("remove L tail")
    assert ostream.getvalue() == "2\n"


def test_repl_list_removing_from_head(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create list L")
    repl.eval("add L 1 tail")
    repl.eval("add L 2 tail")
    repl.eval("remove L head")
    assert ostream.getvalue() == "1\n"
    ostream.seek(0)
    ostream.truncate(0)
    repl.eval("remove L head")
    assert ostream.getvalue() == "2\n"


def test_repl_list_removing_from_nth(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create list L")
    repl.eval("add L 1 tail")
    repl.eval("add L 2 tail")
    repl.eval("add L 3 1")
    repl.eval("remove L head")
    assert ostream.getvalue() == "1\n"
    ostream.seek(0)
    ostream.truncate(0)
    repl.eval("remove L 0")
    assert ostream.getvalue() == "3\n"


def test_repl_tree_creation(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create tree T 0 0")
    repl.eval("add T 0 1 1")
    assert repl.env["T"].get_node_content(0) == 0
    assert repl.env["T"].get_node_content(1) == 1
    assert repl.env["T"].get_path_until(1) == [0, 1]


def test_repl_quicksort(repl_ostream):
    (repl, ostream) = repl_ostream
    repl.eval("create stack S")
    repl.eval("add S 2")
    repl.eval("add S 0")
    repl.eval("add S 1")
    repl.eval("sort quick_sort S")
    assert ostream.getvalue().split("\n")[0] == "[0, 1, 2]"
