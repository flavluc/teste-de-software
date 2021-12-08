def bfs(graph, start):
    stack = [start]
    i = 0

    while i < len(stack):
        node_id = stack[i]
        for child in graph._nodes[node_id].adj_list:
            if child not in stack:
                stack.append(child)
        i += 1

    return stack
