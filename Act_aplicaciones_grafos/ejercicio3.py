from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = {node: False for node in residual_graph}
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v, capacity in residual_graph[u].items():
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

    return visited[sink]

def edmonds_karp(graph, source, sink):
    # Create a residual graph where for each edge (u, v, w), 
    # we also add a reverse edge (v, u, 0) if it doesn't exist
    residual_graph = {u: {} for u in graph}
    for u in graph:
        for v, w in graph[u]:
            residual_graph[u][v] = w
            residual_graph[v].setdefault(u, 0)

    parent = {node: None for node in graph}
    max_flow = 0

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

'''
#example provided by chatgpt
graph = {
    'A': [('B', 10), ('C', 10)],
    'B': [('C', 2), ('D', 4), ('E', 8)],
    'C': [('E', 9)],
    'D': [('F', 10)],
    'E': [('D', 6), ('F', 10)],
    'F': []  # No outgoing edges for the sink
}
'''
graph = {
    'A': [('B', 70), ('F', 37), ('C', 80)],
    'B': [('H', 72)],
    'C': [('D', 54)],
    'D': [('L', 82)],
    'E': [('C', 44), ('D', 69), ('L', 71)],
    'F': [('A', 43), ('G', 24), ('E', 47)],
    'G': [('F', 25), ('K', 76)],
    'H': [('I', 23), ('G', 61), ('B', 85)],
    'I': [('G', 82), ('J', 60)],
    'J': [('G', 42), ('N', 90)],
    'K': [('N', 34), ('M', 42), ('L', 50), ('E', 66)],
    'L': [('M', 66)],
    'M': [('N', 75)],
    'N': [('K', 55)]
}
# Apply the Edmonds-Karp algorithm to the example graph
max_flow1 = edmonds_karp(graph, 'A', 'N')
print(f"El flujo maximo de 'A' a 'N' es de: {max_flow1}\n")

max_flow2 = edmonds_karp(graph, 'F', 'N')
print(f"El flujo maximo de 'F' a 'N' es de: {max_flow2}\n")

max_flow3 = edmonds_karp(graph, 'H', 'N')
print(f"El flujo maximo de 'H' a 'N' es de: {max_flow3}\n")

max_flow4 = edmonds_karp(graph, 'B', 'N')
print(f"El flujo maximo de 'B' a 'N' es de: {max_flow4}\n")
