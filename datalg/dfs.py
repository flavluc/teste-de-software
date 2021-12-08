def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        node_id = stack.pop()
        visited.append(node_id)
        for child in graph._nodes[node_id].adj_list:
            if (child not in visited) and (child not in stack):
                stack.append(child)

    return visited
