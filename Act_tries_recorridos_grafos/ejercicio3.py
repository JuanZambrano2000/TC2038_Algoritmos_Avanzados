from queue import Queue, LifoQueue, PriorityQueue
import heapq

class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2, weight))
            self.adjacency_list[vertex2].append((vertex1, weight))

    def neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def bfs(self, start_vertex, target_vertex):
        visited = set()
        queue = Queue()
        queue.put((start_vertex, [start_vertex], 0))  # Start with weight 0

        while not queue.empty():
            current_vertex, path, total_weight = queue.get()
            if current_vertex == target_vertex:
                return path, total_weight

            visited.add(current_vertex)
            for (neighbor, weight) in self.neighbors(current_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    new_weight = total_weight + weight
                    queue.put((neighbor, new_path, new_weight))
        return [], 0


    def dfs(self, start_vertex, target_vertex):
        visited = set()
        stack = LifoQueue()
        stack.put((start_vertex, [start_vertex], 0))  # Start with cost 0

        while not stack.empty():
            current_vertex, path, cost = stack.get()
            if current_vertex == target_vertex:
                return path, cost

            visited.add(current_vertex)
            for (neighbor, weight) in self.neighbors(current_vertex):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    stack.put((neighbor, new_path, new_cost))
        return [], 0


    def ucs(self, start_vertex, target_vertex):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, start_vertex, [start_vertex]))

        while not queue.empty():
            cost, current_vertex, path = queue.get()
            if current_vertex == target_vertex:
                return path, cost

            visited.add(current_vertex)
            for (neighbor, weight) in self.neighbors(current_vertex):
                if neighbor not in visited:
                    total_cost = cost + weight
                    new_path = path + [neighbor]
                    queue.put((total_cost, neighbor, new_path))
        return [], 0
    
    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.adjacency_list}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            for neighbor, weight in self.neighbors(current_vertex):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

graph = WeightedGraph()

vertices = ["Zrusall", "Goxmont", "Niaphia", "Adaset", "Ertonwell", "Duron", "Lagos", 
            "Oriaron", "Blebus", "Ontdale", "Goding", "Ylane", "Strento", "Togend"]
for vertex in vertices:
    graph.add_vertex(vertex)

edges = [
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

for edge in edges:
    graph.add_edge(*edge)

distances = graph.dijkstra('Goding')
for vertex, distance in distances.items():
    print(f"Distance from Goding to {vertex}: {distance}")