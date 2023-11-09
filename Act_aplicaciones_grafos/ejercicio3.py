from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = [False] * len(residual_graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()

        for ind, capacity in enumerate(residual_graph[u]):
            if not visited[ind] and capacity > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[sink]

def edmonds_karp(graph, source, sink):
    # This will be our flow network where we'll perform the algorithm
    residual_graph = [list(row) for row in graph]
    max_flow = 0
    parent = [-1] * len(graph)

    # As long as there is a path from the source to the sink,
    # with available capacity, we can keep adding flow.
    while bfs(residual_graph, source, sink, parent):
        path_flow = float('inf')

        # Find the minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow through
        # the path found.
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Add this path flow to the overall flow
        max_flow += path_flow

        # update the residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow
