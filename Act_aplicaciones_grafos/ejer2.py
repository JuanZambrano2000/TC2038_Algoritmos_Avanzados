from queue import PriorityQueue
import copy

class WeightedGraph:
  """ 
        Class that is used to represent a weighted graph. Internally, the class uses an adjacency list to store 
        the vertices and edges of the graph. This adjacency list is defined by a dictionary, whose keys
        represent the vertices. For each vertex, there is a list of tuples (v,e) that indicate which vertices
        are connected to the vertex and their corresponding weights.

        The graph can be directed or indirected. In the class constructor, this property is set. The
        behaviour of some operations depends on this property.

        This graph class assumes that it is possible to have multiple links between vertices.
    """

  _directed = True  # This flag indicates whether the graph is directed or indirected.

  _adjacency_list = {}  # The adjacency list of the graph.

  def __init__(self, directed: bool = False):
    """ 
            This constructor initializes an empty graph. 

            param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
        """

    self._directed = directed
    self._adjacency_list = {}

  def clear(self):
    """ 
            This method clears the graph. 
        """
    self._adjacency_list = {}

  def number_of_vertices(self):
    """ 
            This method returns the number of vertices of the graph.
        """
    return len(self._adjacency_list)

  def vertices(self):
    """ 
            This method returns the list of vertices.
        """
    v = []
    for vi in self._adjacency_list:
      v.append(vi)
    return v

  def edges(self):
    """ 
            This method returns the list of edges.
        """
    e = []

    if self._directed:
      for v in self._adjacency_list:
        for edge in self._adjacency_list[v]:
          e.append((v, edge[0], edge[1]))

    else:
      for v in self._adjacency_list:
        for edge in self._adjacency_list[v]:
          if (edge[0], v, edge[1]) not in e:
            e.append((v, edge[0], edge[1]))
    return e

  def add_vertex(self, v):
    """ 
            Add vertex to the graph.   

            param v: The new vertex to be added to the graph.   
        """

    if v in self._adjacency_list:
      print("Warning: Vertex ", v, " already exists.")

    else:
      self._adjacency_list[v] = []

  def remove_vertex(self, v):
    """ 
            Remove vertex from the graph.      

            param v: The vertex to be removed from the graph.   
        """

    if v not in self._adjacency_list:
      print("Warning: Vertex ", v, " is not in graph.")

    else:
      # Remove vertex from adjacency list.
      self._adjacency_list.remove(v)

      # Remove edges where the vertex is an end point.
      for vertex in self._adjacency_list:
        for edge in self._adjacency_list[vertex]:
          if edge[0] == v:
            self._adjacency_list[vertex].remove(edge)

  def add_edge(self, v1, v2, e=0):
    """ 
            Add edge to the graph. The edge is defined by two vertices v1 and v2, and
            the weigth e of the edge. 

            param v1: The start vertex of the new edge.   
            param v2: The end vertex of the new edge.
            param e: The weight of the new edge. 
        """

    if v1 not in self._adjacency_list:
      # The start vertex does not exist.
      print("Warning: Vertex ", v1, " does not exist.")

    elif v2 not in self._adjacency_list:
      # The end vertex does not exist.
      print("Warning: Vertex ", v2, " does not exist.")

    elif not self._directed and v1 == v2:
      # The graph is undirected, so it is no allowed to have autocycles.
      print("Warning: An undirected graph cannot have autocycles.")

    elif (v2, e) in self._adjacency_list[v1]:
      # The edge is already in graph.
      print("Warning: The edge (", v1, ",", v2, ",", e, ") already exists.")
    else:
      self._adjacency_list[v1].append((v2, e))
      if not self._directed:
        self._adjacency_list[v2].append((v1, e))

  def remove_edge(self, v1, v2, e):
    """ 
            Remove edge from the graph. 

            param v1: The start vertex of the edge to be removed.
            param v2: The end vertex of the edge to be removed.
            param e: The weight of the edge to be removed. 
        """

    if v1 not in self._adjacency_list:
      # v1 is not a vertex of the graph
      print("Warning: Vertex ", v1, " does not exist.")

    elif v2 not in self._adjacency_list:
      # v2 is not a vertex of the graph
      print("Warning: Vertex ", v2, " does not exist.")

    else:
      for edge in self._adjacency_list[v1]:
        if edge == (v2, e):
          self._adjacency_list[v1].remove(edge)

      if not self._directed:
        for edge in self._adjacency_list[v2]:
          if edge == (v1, e):
            self._adjacency_list[v2].remove(edge)

  def adjacent_vertices(self, v):
    """ 
            Adjacent vertices of a vertex.

            param v: The vertex whose adjacent vertices are to be returned.
            return: The list of adjacent vertices of v.
        """

    if v not in self._adjacency_list:
      # The vertex is not in the graph.
      print("Warning: Vertex ", v, " does not exist.")
      return []

    else:
      return self._adjacency_list[v]

  def is_adjacent(self, v1, v2) -> bool:
    """ 
            This method indicates whether vertex v2 is adjacent to vertex v1.

            param v1: The start vertex of the relation to test.
            param v2: The end vertex of the relation to test.
            return: True if v2 is adjacent to v1, False otherwise.
        """

    if v1 not in self._adjacency_list:
      # v1 is not a vertex of the graph
      print("Warning: Vertex ", v1, " does not exist.")
      return False

    elif v2 not in self._adjacency_list:
      # v2 is not a vertex of the graph
      print("Warning: Vertex ", v2, " does not exist.")
      return False

    else:
      for edge in self._adjacency_list[v1]:
        if edge[0] == v2:
          return True
      return False

  def print_graph(self):
    """ 
            This method shows the edges of the graph.
        """

    for vertex in self._adjacency_list:
      for edges in self._adjacency_list[vertex]:
        print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

class TspUcsNode:
  """ 
        Class that is used to represent a node in the uniform search algorithm for the TSP problem. 
        A node contains the following elements:
        * A reference to its parent.
        * The vertex of the graph that is represented.
        * The total path cost from the root to the node.
        * The list of explored nodes.
    """

  def __init__(self, parent, v, c, explored):
    """ 
            This constructor initializes a node. 

            param parent: The node parent.
            param v: The graph vertex that is represented by the node.
            param c: The path cost to the node from the root.
            param explored: The path from the root to the node.
        """
    self.parent = parent
    self.v = v
    self.c = c
    self.explored = explored

  def __lt__(self, node):
    """ 
            Operator <. This definition is requiered by the PriorityQueue class.
        """
    return False


def tsp_ucs(graph: WeightedGraph, v0):
  """ 
        This method finds the Hamiltonian cycle of minimum cost of a directed graph starting from 
        the given vertex using the uniform cost search algorithm.

        param graph: The graph to traverse.
        param v0: The initial vertex.
        return: A tuple with the Hamiltonian of minimum cost, or null if there is no a path.
    """

  vertices = graph.vertices()
  n = len(vertices)

  if v0 not in vertices:
    print("Warning: Vertex", v0, "is not in Graph")

  frontier = PriorityQueue()
  frontier.put((0, TspUcsNode(None, v0, 0, [(v0, 0)])))

  while True:
    if frontier.empty():
      return None

    node = frontier.get()[1]

    if len(node.explored) == (n + 1) and node.v == v0:
      return {"Path": node.explored, "Cost": node.c}

    adjacent_vertices = gr.adjacent_vertices(node.v)
    for vertex in adjacent_vertices:
      already_included = False

      if vertex[0] == v0 and len(node.explored) < n:
        already_included = True

      for i in range(1, len(node.explored)):
        if vertex[0] == node.explored[i][0]:
          already_included = True
          break

      if not already_included:
        cost = vertex[1] + node.c
        frontier.put(
            (cost, TspUcsNode(node, vertex[0], cost,
                              node.explored + [vertex])))

class TspBBNode:
  def __init__(self, parent, v, c, cpos, explored, m):
    self.parent = parent
    self.v = v
    self.c = c
    self.cpos = cpos
    self.explored = explored
    self.m = m

  def __lt__(self, node):
    return False


def tsp_bb(graph: WeightedGraph, v0):
  """ 
        This method finds the Hamiltonian cycle of minimum cost of a directed graph starting from 
        the given vertex.The estimated cost of each node of the tree is calcualted using the 
        reduction matrix technique.

        param graph: The graph to traverse.
        param v0: The initial vertex.
        return: A tuple with the Hamiltonian of minimum cost, or null if there is no a path.
    """

  vertices = graph.vertices()
  n = len(vertices)

  if v0 not in vertices:
    print("Warning: Vertex", v0, "is not in Graph")

  vindices = {}
  for i, v in enumerate(vertices, 0):
    vindices[v] = i

  # Adyacency matrix
  inf_val = 100000000
  m = [[inf_val] * n for i in range(n)]

  for edge in gr.edges():
    i = vindices[edge[0]]
    j = vindices[edge[1]]
    c = edge[2]
    m[i][j] = c
    m[j][i] = c

  # Reduce rows
  rrows = [0] * n
  for i in range(n):
    rrows[i] = min(m[i])
    if rrows[i] == inf_val:
      rrows[i] = 0

    for j in range(n):
      if m[i][j] != inf_val:
        m[i][j] -= rrows[i]

  # Reduce columns
  rcols = [0] * n
  for j in range(n):
    col = [m[i][j] for i in range(n)]
    rcols[j] = min(col)
    if rcols[j] == inf_val:
      rcols[j] = 0

    for i in range(n):
      if m[i][j] != inf_val:
        m[i][j] -= rcols[j]

  red_cost = sum(rrows) + sum(rcols)

  frontier = PriorityQueue()
  frontier.put((0, TspBBNode(None, v0, 0, red_cost, [(v0, 0)], m)))

  best = None
  best_val = inf_val

  while not frontier.empty():

    # Get node from frontier
    node = frontier.get()[1]

    # Update best solution
    if len(node.explored) == (n + 1) and node.v == v0:
      if node.c < best_val:
        best = node
        best_val = node.c
      continue

    adjacent_vertices = gr.adjacent_vertices(node.v)
    for vertex in adjacent_vertices:
      already_included = False

      if vertex[0] == v0 and len(node.explored) < n:
        already_included = True

      for i in range(1, len(node.explored)):
        if vertex[0] == node.explored[i][0]:
          already_included = True
          break
      if not already_included:
        cost = vertex[1] + node.c
        new_explored = node.explored + [vertex]

        m = copy.deepcopy(node.m)

        row = vindices[node.v]
        col = vindices[vertex[0]]
        for k in range(n):
          m[row][k] = inf_val

        for k in range(n):
          m[k][col] = inf_val

        for i in range(len(new_explored)):
          for j in range(i + 1, len(new_explored)):
            v1 = vindices[new_explored[i][0]]
            v2 = vindices[new_explored[j][0]]
            m[v1][v2] = inf_val
            m[v2][v1] = inf_val

        rrows = [0] * n
        for i in range(n):
          rrows[i] = min(m[i])
          if rrows[i] == inf_val:
            rrows[i] = 0

          for j in range(n):
            if m[i][j] != inf_val:
              m[i][j] -= rrows[i]

        rcols = [0] * n
        for j in range(n):
          col = [m[i][j] for i in range(n)]
          rcols[j] = min(col)
          if rcols[j] == inf_val:
            rcols[j] = 0

          for i in range(n):
            if m[i][j] != inf_val:
              m[i][j] -= rcols[j]

        reduced_cost = sum(rrows) + sum(rcols)

        cpos = vertex[1] + node.cpos + red_cost
        if cpos < best_val:
          frontier.put(
              (cpos, TspBBNode(node, vertex[0], cost, cpos, new_explored, m)))

  return {"Path": best.explored, "Cost": best.c}

gr = WeightedGraph(directed=False)

# Graph provided by chatgpt
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
for vertex in vertices:
    gr.add_vertex(vertex)

edges = [
    ('A', 'B', 6), ('A', 'D', 18), ('A', 'U', 24), ('B', 'C', 22), ('C', 'D', 12), ('C', 'F', 4), ('D', 'E', 36),
    ('E', 'H', 13), ('E', 'J', 7), ('F', 'G', 18), ('G', 'I', 13), ('H', 'I', 7), ('I', 'L', 31), ('J', 'L', 29),
    ('J', 'K', 20), ('K', 'N', 21), ('L', 'M', 24),('M', 'O', 26), ('N', 'O', 11), ('N', 'Q', 9), ('O', 'P', 2),
    ('O', 'T', 31), ('P', 'Q', 23), ('P', 'R', 6), ('Q', 'R', 10), ('R', 'S', 29), ('S', 'U', 21), ('T', 'U', 40),
    ('T', 'S', 23), ('T', 'R', 29), ('F', 'A', 17), ('N', 'Q', 5), ('P', 'L', 39), ('I', 'O', 27), ('T', 'C', 2),
    ('F', 'Q', 27), ('I', 'G', 31), ('U', 'L', 28),('M', 'S', 34),('T', 'D', 7),('J', 'A', 6), ('N', 'C', 30)
]
for edge in edges:
    gr.add_edge(*edge)


print("Uniform cost search")
res1 = tsp_ucs(gr, 'A')
print(res1)

print("Branch and bound")
res2 = tsp_bb(gr, 'A')
print(res2)
