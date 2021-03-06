class Node:
    def __init__(self, content=None):
        self.adj_list = set()
        self.content = content


class GraphInterface:
    def __init__(self):
        self._nodes = dict()

    def empty(self):
        return len(self._nodes) == 0

    def add_node(self, node_id, node_content):
        if node_id in self._nodes:
            raise "Cannot add node {id},it already exists in the graph".format(
                id=node_id
            )

        self._nodes[node_id] = Node(node_content)

    def has_edge_between(self, start_node_id, end_node_id):
        if start_node_id in self._nodes:
            if end_node_id in self._nodes:
                return end_node_id in self._nodes[start_node_id].adj_list
            else:
                raise "Node {id} does not exist in the graph".format(
                    id=end_node_id
                )
        else:
            raise "Node {id} does not exist in the graph".format(
                id=start_node_id
            )

    def get_node_content(self, node_id):
        if node_id not in self._nodes:
            raise "Node {id} does not exist in the graph".format(id=node_id)

        return self._nodes[node_id].content


class DirectedGraph(GraphInterface):
    def add_edge(self, start_node_id, end_node_id):
        if start_node_id in self._nodes:
            if end_node_id in self._nodes:
                self._nodes[start_node_id].adj_list.add(end_node_id)
            else:
                raise "Node {id} does not exist in the graph".format(
                    id=end_node_id
                )
        else:
            raise "Node {id} does not exist in the graph".format(
                id=start_node_id
            )

    def remove_node(self, node_id):
        if node_id in self._nodes:
            del self._nodes[node_id]
            for node in self._nodes:
                if node_id in self._nodes[node].adj_list:
                    self._nodes[node].adj_list.remove(node_id)


class UndirectedGraph(DirectedGraph):
    def add_edge(self, start_node_id, end_node_id):
        super().add_edge(start_node_id, end_node_id)
        self._nodes[end_node_id].adj_list.add(start_node_id)

    def remove_node(self, node_id):
        if node_id in self._nodes:
            for edged_node in self._nodes[node_id].adj_list:
                self._nodes[edged_node].adj_list.remove(node_id)
            del self._nodes[node_id]
