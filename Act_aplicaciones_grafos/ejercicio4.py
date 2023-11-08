import heapq
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item]) 
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]: self.rank[root2] += 1

def kruskal(graph):
    # list to store the minimum spanning tree
    mst = [] 
    # sort the graph edges by weight 
    graph.sort()  
    ds = DisjointSet(set([u for _, u, v in graph] + [v for _, u, v in graph]))  # create disjoint sets

    for weight, u, v in graph:
        if ds.find(u) != ds.find(v):  # if u and v belong to different sets, no cycle will be formed
            mst.append((weight, u, v))  # add the edge to the mst
            ds.union(u, v)  # merge the sets

    return mst

def prim(graph, start_vertex):
    # Convert graph to adjacency list
    adjacency_list = {}
    for edge in graph:
        vertex1, vertex2, weight = edge
        if vertex1 not in adjacency_list:
            adjacency_list[vertex1] = []
        if vertex2 not in adjacency_list:
            adjacency_list[vertex2] = []
        adjacency_list[vertex1].append((vertex2, weight))
        adjacency_list[vertex2].append((vertex1, weight))
    
    # Initialize min heap, visited set, MST and predecessor map
    min_heap = [(0, start_vertex, None)]  # heap elements are tuples (weight, vertex, predecessor)
    visited = set()
    mst = []
    predecessor = {start_vertex: None}

    while min_heap:
        weight, current_vertex, prev_vertex = heapq.heappop(min_heap)
        if current_vertex not in visited:
            visited.add(current_vertex)
            if prev_vertex is not None:  # Avoid adding the starting vertex
                mst.append((prev_vertex, current_vertex, weight))

            for neighbor, edge_weight in adjacency_list[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))
    
    return mst

graph = [
    ('Ylane', 'Goding', 88),
    ('Ylane', 'Strento', 99),
    ('Ylane', 'Oriaron', 117),
    ('Goding', 'Ontdale', 98),
    ('Ontdale', 'Togend', 210),
    ('Ontdale', 'Oriaron', 219),
    ('Ontdale', 'Blebus', 165),
    ('Togend', 'Blebus', 121),
    ('Strento', 'Oriaron', 221),
    ('Strento', 'Zrusall', 112),
    ('Oriaron', 'Blebus', 291),
    ('Blebus', 'Duron', 160),
    ('Zrusall', 'Adaset', 15),
    ('Zrusall', 'Goxmont', 112),
    ('Adaset', 'Ertonwell', 130),
    ('Adaset', 'Goxmont', 103),
    ('Ertonwell', 'Duron', 121),
    ('Ertonwell', 'Niaphia', 56),
    ('Duron', 'Lagos', 119),
    ('Lagos', 'Niaphia', 300),
    ('Goxmont', 'Niaphia', 212)
]

minSpanTreeKruskal = kruskal(graph)
minSpanTreePrim = prim(graph, 'Adaset')
print("Minimum Spanning Tree Kruskal") 
print(minSpanTreeKruskal)
print("Minimum Spanning Tree Prim")
print(minSpanTreePrim)
