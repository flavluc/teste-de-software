from graph import Node

class Tree:

    def __init__(self, rootId, rootContent):
        self.__root_content = rootContent
        self.__root_id = rootId
        self._nodes = {}
        self._nodes[rootId] = Node(rootContent)

    def __validate_node_existence(self, node_id):
        if(node_id not in self._nodes):
            raise "The node {id} does not exists in this tree".format(id=node_id)

    def add_node(self, parent_id, node_id, node_content):
        self.__validate_node_existence(parent_id)
        if(node_id in self._nodes): 
            raise "Cannot add node {id}, it already exists in the tree".format(id=node_id)
        
        self._nodes[node_id] = Node(node_content)
        self._nodes[parent_id].adj_list.add(node_id)
    
    def is_leaf(self, node_id)
        self.__validate_node_existence(node_id)
        
        adjacency_list_size = len(self._nodes[node_id].adj_list)
        return adjacency_list_size == 0

    def get_path_until(self, node_id):
        self.__validate_node_existence(node_id)
        return self.__get_path(self.__root_id)

    def __get_path(self, current_element_id, end_node_id, accumaltive_list)
        accumaltive_list.push_back(current_element_id)
        if(end_node_id == current_element):
            return accumaltive_list
        else:
            curr_node = self._nodes[current_element_id]
            for next_node in curr_node.adj_list:
                result = self.__get_path(next_node, end_node_id, accumaltive_list)
                if(len(result) > 0):
                    return result
            
            return []

    def update_node_content(self, node_id, new_content):
        self.__validate_node_existence(node_id)
        self._nodes[node_id].content = new_content

    def get_node_content(self, node_id, new_content):
        self.__validate_node_existence(node_id)        
        return self._nodes[node_id].content



        