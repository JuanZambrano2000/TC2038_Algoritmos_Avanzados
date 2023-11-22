#Equipo 2, Stefano, Fabian, Juan, Sebastian

#Librerias
#Libreris para la parte 1
#pip install --user numpy
#pip install --user matplotlib

import numpy as np
import matplotlib.pyplot as plt

#Libreris para la parte 2

from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

#Libreris para la parte 3


import math

#Librerias para la parte 5

#import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
#import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


"""
Etapa 1 - Registro de señales de EEG
"""

#Funcion para graficar los recorridos de la matriz de 8 electrodos

def graficasCaminos8(caminos):
    channels = ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']

    points3D = [[0,0.71934,0.694658], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0,-0.71934,0.694658], [-0.587427,-0.808524,-0.0348995], [0,-0.999391,-0.0348995], [0.587427,-0.808524,-0.0348995]]
    points3D = np.array(points3D)

    r = np.sqrt(points3D[:,0]**2 + points3D[:,1]**2 + points3D[:,2]**2)
    t = r/(r + points3D[:,2])
    x = r*points3D[:,0]
    y = r*points3D[:,1]
    points2D = np.column_stack((x,y))

    circle = plt.Circle((0,0),1, color = 'r', alpha = 0.25, fill = False)
    plt.scatter(points2D[:,0], points2D[:,1])
    plt.gca().add_patch(circle)

    for i in range(len(points2D)):
        plt.text(points2D[i,0]-0.02, points2D[i,1]+0.025, channels[i])

    index = []

    for x in caminos:
        index.append(channels.index(x))
    
    print("index : ",index)
    

    # Resaltar la aristas
   
    for i in range (len(index)-1):
        plt.plot([points2D[index[i], 0], points2D[index[i+1], 0]],
                [points2D[index[i], 1], points2D[index[i+1], 1]],
                color='blue', linestyle='--', linewidth=2)    
        
    plt.axis('equal')
    plt.show()


#Funcion para graficar los recorridos de la matriz de 32 electrodos

def graficasCaminos32(caminos):
    channels = ['Fp1','Fp2', 'AF3', 'AF4', 'F7', 'F3', 'Fz', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO3', 'PO4', 'O1', 'Oz', 'O2']

    points3D = [[-0.308829,0.950477,-0.0348995], [0.308829,0.950477,-0.0348995], [-0.406247,0.871199,0.275637], [0.406247,0.871199,0.275637], [-0.808524,0.587427,-0.0348995], [-0.545007,0.673028,0.5], [0,0.71934,0.694658], [0.545007,0.673028,0.5], [0.808524,0.587427,-0.0348995], [-0.887888,0.340828,0.309017], [-0.37471,0.37471,0.848048], [0.37471,0.37471,0.848048], [0.887888,0.340828,0.309017], [-0.999391,0,-0.0348995], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0.999391,0,-0.0348995], [-0.887888,-0.340828,0.309017], [-0.37471,-0.37471,0.848048], [0.37471,-0.37471, 0.848048], [0.887888,-0.340828,0.309017], [-0.808524,-0.587427,-0.0348995], [-0.545007,-0.673028,0.5], [0,-0.71934,0.694658], [0.545007,-0.673028,0.5], [0.808524,-0.587427,-0.0348995], [-0.406247,-0.871199,0.275637], [0.406247,-0.871199,0.275637], [-0.308829,-0.950477,-0.0348995], [0,-0.999391,-0.0348995], [0.308829,-0.950477,-0.0348995]]
    points3D = np.array(points3D)

    r = np.sqrt(points3D[:,0]**2 + points3D[:,1]**2 + points3D[:,2]**2)
    t = r/(r + points3D[:,2])
    x = r*points3D[:,0]
    y = r*points3D[:,1]
    points2D = np.column_stack((x,y))

    circle = plt.Circle((0,0),1, color = 'r', alpha = 0.25, fill = False)
    plt.scatter(points2D[:,0], points2D[:,1])
    plt.gca().add_patch(circle)

    for i in range(len(points2D)):
        plt.text(points2D[i,0]-0.02, points2D[i,1]+0.025, channels[i])
    
    index = []
    for x in caminos:
        index.append(channels.index(x))
    

    # Resaltar la arista entre Fz y PO8
    for i in range (len(index)-1):
        plt.plot([points2D[index[i], 0], points2D[index[i+1], 0]],
                [points2D[index[i], 1], points2D[index[i+1], 1]],
                color='blue', linestyle='--', linewidth=2)

    plt.axis('equal')
    plt.show()

"""
ETAPA 2: - Análisis de caminos en los grafos de conectividad
"""

class WeightedGraph:
    #Representacion de la grafica con peso. 
    #Lista de adjacencia para guardar vertices y aristas. La lista es un diccionario cuyas llaves representar los vertices.
    #Para cada vertice dentro del diccionario hay una lista de tuples, que tienen el vertice vecino y su peso
    #La grafica puede ser dirigida o no dirigida

    _directed = True 
    _adjacency_list = {} #Lista de adjacencia

    def __init__(self, directed:bool = False):
        """ 
            This constructor initializes an empty graph. 

            param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
        """

        self._directed = directed
        self._adjacency_list = {}

    def clear(self):
        #Limpia la lista de adyacencia
        self._adjacency_list = {}

    def numer_of_vertices(self):
        #Regresa el numero de vertices de la grafica
        return len(self._adjacency_list)

    def vertices(self):
        #Regresa una lista de vertices
        v = []
        for vi in self._adjacency_list:
            v.append(vi)
        return v

    def edges(self):
        #Regresa lisa de aristas
        e = []
        if self._directed:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    e.append((v, edge[0], edge[1]))
        else:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    if(edge[0], v, edge[1]) not in e:
                        e.append((v, edge[0], edge[1]))
        return e

    def add_vertex(self, v):
        #Añade vertices a la grafica
        #Necesita el nuevo vertice

        if v in self._adjacency_list:
            print("ALERTA : vertice ",v, " ya existe")
        else:
            self._adjacency_list[v] = []


    def remove_vertex(self, v):
        #Elimina un vertice
        if v not in self._adjacency_list:
            print("ALERTA vertice ",v," no existe")
        else:
            #Remover vertice de la lista de adjacencia
            self._adjacency_list.remove(v)

            #Remover aristar donde el vertice es destino
            for vertex in self._adjacency_list:
                for edge in self._adjacency_list[vertex]:
                    if edge[0] == v:
                        self._adjacency_list[vertex].remove(edge)

    def add_edge(self, v1, v2, e = 0):
        #Añade una arista, vertice origen, vectice destino, peso del camino si no se incluye el valor el peso es 0

        if v1 not in self._adjacency_list:
            #El vertice de inicio no exite
            print("ALERTA vertice ",v1," de origen no existe")

        elif v2 not in self._adjacency_list:
            #El vertice de destino no existe
            print("ALERTE vertice ",v2," de destino no existe")

        elif not self._directed and v1 == v2:
            #La grafica no es dirigida y hay un autociclo
            print("ALERTA no se puede tener autociclos en una grafica no-dirigida")

        elif (v2,e) in self._adjacency_list[v1]:
            #La arista ya existe
            print("ALERTA: la arista de ",v1," a ",v2," con peso :",e," ya existe")

        else:
            self._adjacency_list[v1].append((v2,e))
            if not self._directed:
                self._adjacency_list[v2].append((v1,e))

    def remove_edge(self, v1, v2, e):
        #Quitar una arista, vertice de origen, vertice destino, costo del camino
        if v1 not in self._adjacency_list:
            print("ALERTA vertice ",v1," no existe")

        elif v2 not in self._adjacency_list:
            print("ALERTA vertice ",v2," no existe" )

        else:
            for edge in self._adjacency_list[v1]:
                if edge == (v2,e):
                    self._adjacency_list[v1].remove(edge)

            if not self._directed:
                for edge in self._adjacency_list[v2]:
                    if edge == (v1,e):
                        self._adjacency_list[v2].remove(edge)

    def adjacent_vertices(self,v):
        #Lista de adyacencia del vertice

        if v not in self._adjacency_list:
            #El vertice no existe
            print("ALERTA vertice 123",v," no existe")
            return []
        else:
            return self._adjacency_list[v]


    def is_adjacent(self, v1, v2) -> bool:
        #Comprueba si v2 es vecino de v1
        #Regresa true si son vecinos y false si no hay camino directo

        if v1 not in self._adjacency_list:
            #No existe v1
            print("ALERTA vertice ",v1," no existe")
            return False
        elif v2 not in self._adjacency_list:
            #No existe v2
            print("ALERTA vertice",v2," no exsite")
            return False

        else:
            for edge in self._adjacency_list[v1]:
                if edge[0] == v2:
                    return True
            return False

    def print_graph(self):
        #Muestra las aristas de la grafica
        for vertex in self._adjacency_list:
            for edges in self._adjacency_list[vertex]:
                print(vertex," -> ",edges[0], " peso ",edges[1])

class TreeNode:
    def __init__(self, parent, v, c):
        """ 
            This constructor initializes a node. 

            param parent: The node parent.
            param v: The graph vertex that is represented by the node.
            param c: The path cost to the node from the root.
        """
        self.parent = parent
        self.v = v
        self.c = c

    def __lt__(self, node):
        """ 
            Operator <. This definition is requiered by the PriorityQueue class.
        """
        return False; 

    def path(self):
        #Crea la lista de vertices de la raiz al nodo
        node = self
        path = []
        while node != None:
            path.insert(0,node.v) #--------------que es el 0 ?
            node = node.parent 
        return path


#Funciones para obtener los caminos
def bfs(graph:WeightedGraph, v0,  vg):
    #Recorrido en anchura (Breadth-first), de v0 a vg
    #Regresa una tupla con el camino de vi a vg y el costo, en caso de no existir regresa null

    #Checar si los vrtices no existen
    if v0 not in graph.vertices():
        print("ALERTA;--- vertex ",v0," no existe")

    if vg not in graph.vertices():
        print("ALERTA -  vertice ",vg," no existe")

    #Inicializar frontera
    frontier = Queue()
    frontier.put(TreeNode(None, v0,0))

    #Inicialilzar set de exploracion
    explored_set = {}

    while True:
        if frontier.empty():
            return None

        node = frontier.get()

        #Checar si el nodo es el destino
        if node.v == vg:
            return{"Path":node.path(), "Cost":node.c}

        #Expandir nodo
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1]+ node.c))

        explored_set[node.v] = 0

def dfs(graph:WeightedGraph, v0, vg):
    #Busqueda de profundidad, del v0 a vg
    #Regresa una tupla con el camino de vi a vg

    #checar si existen los nodos
    if v0 not in graph.vertices():
        print("ALERTA vertice", v0," no existe")

    if vg not in graph.vertices():
        print("ALERTA vertice ",vg," no existe")

    #Inicializar frontera
    frontier = LifoQueue()
    frontier.put(TreeNode(None,v0,0))

    explored_set = {}

    while True:
        if frontier.empty():
            return None

        node = frontier.get()

        #Checar node
        if node.v == vg:
            return {"Path": node.path(), "Cost":node.c}

        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1]+node.c))

        explored_set[node.v] = 0

def uniform_cost(graph:WeightedGraph, v0,vg):
    #Costo uniforme de v0 a vg
    #Regresa  una tupla del camino entre v0 a vg con su costo

    #Checar si existen
    if v0 not in graph.vertices():
        print("ALERTA vertice", v0," no existe")

    if vg not in graph.vertices():
        print("ALETA vertice ",vg," no existe")

    #Inicializar frontera
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, v0, 0)))

    explored_set = {}

    while True:
        if frontier.empty():
            return None

        node = frontier.get()[1]

        #Checar si el node es el que se busca
        if node.v == vg:
            #Regresa el camino y costo como diccionario
            return {"Path":node.path(),"Cost":node.c}

        #Expandir nodo
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                cost = vertex[1]+ node.c
                frontier.put((cost, TreeNode(node, vertex[0], vertex[1]+node.c)))


        explored_set[node.v] = 0

#Funcion para medir la distancia 3d entre 2 puntos para obtener el peso
def distancia(xA, yA, zA, xB, yB, zB):
    punto1 = np.array([xA, yA, zA])
    punto2 = np.array([xB, yB, zB])
    distancia = np.linalg.norm(punto2 - punto1)
    return distancia

#Funcion para llenar la grafica
def graficas(matrizTexto, coordenadasTexto,grafica=WeightedGraph):
    print(matrizTexto)
    matriz = np.loadtxt(matrizTexto, dtype=int)
    coordenadas = np.loadtxt(coordenadasTexto,  dtype=str)

    for i in range(len(coordenadas)):
        grafica.add_vertex(coordenadas[i][0])
    
    for i in range(len(coordenadas)):
        for x in range(len(matriz[i])):
            if (matriz[i][x] == 1 and grafica.is_adjacent(coordenadas[i][0],coordenadas[x][0])== False):
                
                costo = distancia(float(coordenadas[i][1]),float(coordenadas[i][2]),float(coordenadas[i][3]),float(coordenadas[x][1]),float(coordenadas[x][2]),float(coordenadas[x][3]))
                grafica.add_edge(coordenadas[i][0], coordenadas[x][0], costo)
        
    #grafica.print_graph()

#Funcion para llamar a hacer los caminos, BFD, DFS, Uniform cost
def prepCaminos(arregloO_D, graficar, grafica = WeightedGraph):
    print("-----Recorridos de grafos-----")
    
    print("-----BFS-----")

    for x in range(len(arregloO_D)):
        print("Viaje de ",arregloO_D[x][0]," -> ",arregloO_D[x][1])
        res = bfs(grafica, arregloO_D[x][0], arregloO_D[x][1])
        if res != None:
            if graficar == 0:
                graficasCaminos8(res["Path"])
            else :
                graficasCaminos32(res["Path"])
        print(res)

    print("-----DFS-----")

    for x in range(len(arregloO_D)):
        print("Viaje de ",arregloO_D[x][0]," -> ",arregloO_D[x][1])
        res = dfs(grafica, arregloO_D[x][0], arregloO_D[x][1])
        if res != None:
            if graficar == 0:
                graficasCaminos8(res["Path"])
            else :
                graficasCaminos32(res["Path"])
        print(res)

    print("-----Uniform Cost-----")

    for x in range(len(arregloO_D)):
        print("Viaje de ",arregloO_D[x][0]," -> ",arregloO_D[x][1])
        res = uniform_cost(grafica, arregloO_D[x][0], arregloO_D[x][1])
        if res != None:
            if graficar == 0:
                graficasCaminos8(res["Path"])
            else :
                graficasCaminos32(res["Path"])
        print(res)

#Funciones para graficar las graficas con todos sus caminos
def graficarGraficas8(grafica = WeightedGraph):
    channels = ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']

    points3D = [[0,0.71934,0.694658], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0,-0.71934,0.694658], [-0.587427,-0.808524,-0.0348995], [0,-0.999391,-0.0348995], [0.587427,-0.808524,-0.0348995]]
    points3D = np.array(points3D)

    r = np.sqrt(points3D[:,0]**2 + points3D[:,1]**2 + points3D[:,2]**2)
    t = r/(r + points3D[:,2])
    x = r*points3D[:,0]
    y = r*points3D[:,1]
    points2D = np.column_stack((x,y))

    circle = plt.Circle((0,0),1, color = 'r', alpha = 0.25, fill = False)
    plt.scatter(points2D[:,0], points2D[:,1])
    plt.gca().add_patch(circle)

    for i in range(len(points2D)):
        plt.text(points2D[i,0]-0.02, points2D[i,1]+0.025, channels[i])

    index = []

    vertices = grafica.vertices()

    for x in range(len(vertices)):
        numeroV =  channels.index(vertices[x])
        index = grafica.adjacent_vertices(vertices[x])
        if len(index) == 0:
            continue
        for y in range(len(index)):
            numeroI = channels.index(index[y][0])
            plt.plot(
                [points2D[numeroV, 0],points2D[numeroI, 0]],
                [points2D[numeroV, 1], points2D[numeroI, 1]],
                color='blue', linestyle='--', linewidth=2
            )
        
    plt.axis('equal')
    plt.show()

def graficarGraficas32(grafica = WeightedGraph):
    channels = ['Fp1','Fp2', 'AF3', 'AF4', 'F7', 'F3', 'Fz', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO3', 'PO4', 'O1', 'Oz', 'O2']

    points3D = [[-0.308829,0.950477,-0.0348995], [0.308829,0.950477,-0.0348995], [-0.406247,0.871199,0.275637], [0.406247,0.871199,0.275637], [-0.808524,0.587427,-0.0348995], [-0.545007,0.673028,0.5], [0,0.71934,0.694658], [0.545007,0.673028,0.5], [0.808524,0.587427,-0.0348995], [-0.887888,0.340828,0.309017], [-0.37471,0.37471,0.848048], [0.37471,0.37471,0.848048], [0.887888,0.340828,0.309017], [-0.999391,0,-0.0348995], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0.999391,0,-0.0348995], [-0.887888,-0.340828,0.309017], [-0.37471,-0.37471,0.848048], [0.37471,-0.37471, 0.848048], [0.887888,-0.340828,0.309017], [-0.808524,-0.587427,-0.0348995], [-0.545007,-0.673028,0.5], [0,-0.71934,0.694658], [0.545007,-0.673028,0.5], [0.808524,-0.587427,-0.0348995], [-0.406247,-0.871199,0.275637], [0.406247,-0.871199,0.275637], [-0.308829,-0.950477,-0.0348995], [0,-0.999391,-0.0348995], [0.308829,-0.950477,-0.0348995]]
    points3D = np.array(points3D)

    r = np.sqrt(points3D[:,0]**2 + points3D[:,1]**2 + points3D[:,2]**2)
    t = r/(r + points3D[:,2])
    x = r*points3D[:,0]
    y = r*points3D[:,1]
    points2D = np.column_stack((x,y))

    circle = plt.Circle((0,0),1, color = 'r', alpha = 0.25, fill = False)
    plt.scatter(points2D[:,0], points2D[:,1])
    plt.gca().add_patch(circle)

    for i in range(len(points2D)):
        plt.text(points2D[i,0]-0.02, points2D[i,1]+0.025, channels[i])
    
        index = []

    vertices = grafica.vertices()

    for x in range(len(vertices)):
        numeroV =  channels.index(vertices[x])
        index = grafica.adjacent_vertices(vertices[x])
        for y in range(len(index)):
            numeroI = channels.index(index[y][0])
            plt.plot(
                [points2D[numeroV, 0],points2D[numeroI, 0]],
                [points2D[numeroV, 1], points2D[numeroI, 1]],
                color='blue', linestyle='--', linewidth=2
            )

    plt.axis('equal')
    plt.show()

#--------------------------------FLOYD-----------------------------------

class WeightedGraphFloyd:
    """ 
        Class that is used to represent a weighted graph. Internally, the class uses an adjacency matrix to 
        store the vertices and edges of the graph. This adjacency matrix is defined by a list of lists, whose 
        elements indicate the weights of the edges. A weight of 0 indicates that there is no connection
        between nodes.
        
        The graph can be directed or indirected. In the class constructor, this property is set. The
        behaviour of some operations depends on this property.
        
        This graph class assumes that it is not possible to have multiple links between vertices.
    """
    
    _directed = True            # This flag indicates whether the graph is directed or indirected.

    _vertices = []              # The list of vertices.
    
    _adjacency_matrix = []      # The adjacency matrix.
    
    
    def __init__(self, directed:bool = False):
        """ 
            This constructor initializes an empty graph. 
            
            param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
        """
        
        self._directed = directed
        self._vertices = []
        self._adjacency_matrix = []
        
    def clear(self):
        """ 
            This method clears the graph. 
        """        
        self._vertices = []
        self._adjacency_matrix = []
    
    def number_of_vertices(self):
        """ 
            This method returns the number of vertices of the graph.
        """        
        return len(self._vertices)
    
    def vertices(self):
        """ 
            This method returns the list of vertices.
        """
        return self._vertices
    
    def edges(self):
        """ 
            This method returns the list of edges.
        """
        e = []

        n = len(self._vertices)

        if self._directed: 
            for i in range(n):
                for j in range(n):
                    if (self._adjacency_matrix[i][j] > 0):
                        e.append((self._vertices[i], self._vertices[j], self._adjacency_matrix[i][j]))    
        
        else:
            for i in range(n):
                for j in range(i+1, n):
                    if (self._adjacency_matrix[i][j] > 0):
                        e.append((self._vertices[i], self._vertices[j], self._adjacency_matrix[i][j]))

        return e

        
    def add_vertex(self, v):
        """ 
            Add vertex to the graph.   
            
            param v: The new vertex to be added to the graph.   
        """
        
        if v in self._vertices:
            print("Warning: Vertex ", v, " already exists")
        else:
            
            self._vertices.append(v)
            n = len(self._vertices)
                        
            if n > 1:
                for vertex in self._adjacency_matrix:
                    vertex.append(0)                    
                
            self._adjacency_matrix.append(n*[0])

            
    def remove_vertex(self, v):
        """ 
            Remove vertex from the graph.      
            
            param v: The vertex to be removed from the graph.   
        """
        
        if v not in self._vertices:
            print("Warning: Vertex ", v, " does not exist")
            
        else:
            index = self._vertices.index(v)
            
            self._vertices.pop(index)
            
            for row in self._adjacency_matrix:
                row.pop(index)
            
            self._adjacency_matrix.pop(index)
        

    def add_edge(self, v1, v2, e = 0):
        """ 
            Add edge to the graph. The edge is defined by two vertices v1 and v2, and
            the weigth e of the edge. 
            
            param v1: The start vertex of the new edge.   
            param v2: The end vertex of the new edge.
            param e: The weight of the new edge. 
        """   
        
        if v1 not in self._vertices:
            # The start vertex does not exist.
            print("Warning: Vertex ", v1, " does not exist.")  
            
        elif v2 not in self._vertices:
            # The end vertex does not exist.
            print("Warning: Vertex ", v2, " does not exist.")
            
        elif not self._directed and v1 == v2:
            # The graph is undirected, so it is no allowed to have autocycles.
            print("Warning: An undirected graph cannot have autocycles.")
        
        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = e
            
            if not self._directed:
                self._adjacency_matrix[index2][index1] = e

    def remove_edge(self, v1, v2):
        """ 
            Remove edge from the graph. 
            
            param v1: The start vertex of the edge to be removed.
            param v2: The end vertex of the edge to be removed.
            param e: The weight of the edge to be removed. 
        """     
        
        if v1 not in self._vertices:
            # v1 is not a vertex of the graph
            print("Warning: Vertex ", v1, " does not exist.")   
            
        elif v2 not in self._vertices:
            # v2 is not a vertex of the graph
            print("Warning: Vertex ", v2, " does not exist.")
            
        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = 0
            
            if not self._directed:
                self._adjacency_matrix[index2][index1] = 0

    def adjacent_vertices(self, v):
        """ 
            Adjacent vertices of a vertex.
            
            param v: The vertex whose adjacent vertices are to be returned.
            return: The list of adjacent vertices of v.
        """      
                
        if v not in self._vertices:
            # The vertex is not in the graph.
            print("Warning: Vertex ", v, " does not exist.")
            return []        
        
        else:
            adjacent_list = []
            
            n = len(self._vertices)
            i = self._vertices.index(v)
                       
            for j in range(n):
                if self._adjacency_matrix[i][j] != 0:
                    adjacent_list.append((self._vertices[j], self._adjacency_matrix[i][j]))

            return adjacent_list 
            
    def is_adjacent(self, v1, v2) -> bool:
        """ 
            This method indicates whether vertex v2 is adjacent to vertex v1.
            
            param v1: The start vertex of the relation to test.
            param v2: The end vertex of the relation to test.
            return: True if v2 is adjacent to v1, False otherwise.
        """
        
        if v1 not in self._vertices:
            # v1 is not a vertex of the graph
            print("Warning: Vertex ", v1, " does not exist.") 
            return False
            
        elif v2 not in self._vertices:
            # v2 is not a vertex of the graph
            print("Warning: Vertex ", v2, " does not exist.")
            return False
        
        else:
                      
            i = self._vertices.index(v1)
            j = self._vertices.index(v2)
                       
            return self._adjacency_matrix[i][j] != 0

    def print_graph(self):
        """ 
            This method shows the edges of the graph.
        """
        
        n = len(self._vertices)
        for i in range(n):
            for j in range(n):
                if self._adjacency_matrix[i][j] != 0:
                    print(self._vertices[i], " -> ", self._vertices[j], " edge weight: ", self._adjacency_matrix[i][j])


def floyd_marshall(adjacency_matrix):
    """ 
        This method finds the length of the shortest paths between all the vertices
        of a undirected graph.
            
        param adjacency_matrix: The adjacency matrix of the undirected graph.
        return: A matrix with the length of the shortest paths between vertices of 
        the graph.
    """

    print("Floyd")
    
    BIG_NUMBER = 100000000
    n = len(adjacency_matrix)   

    matrix = np.array(adjacency_matrix)    
    matrix[matrix == 0] = BIG_NUMBER 

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] != BIG_NUMBER and matrix[k][j] != BIG_NUMBER and (matrix[i][k]+matrix[k][j]) < matrix[i][j]:
                    matrix[i][j] = matrix[i][k]+matrix[k][j]
                    
    return matrix

def graficas(matrizTexto, coordenadasTexto,grafica=WeightedGraphFloyd):
    print(matrizTexto)
    matriz = np.loadtxt(matrizTexto, dtype=int)
    coordenadas = np.loadtxt(coordenadasTexto,  dtype=str)

    for i in range(len(coordenadas)):
        grafica.add_vertex(coordenadas[i][0])
    
    for i in range(len(coordenadas)):
        for x in range(len(matriz[i])):
            if (matriz[i][x] == 1 and grafica.is_adjacent(coordenadas[i][0],coordenadas[x][0])== False):
                
                costo = distancia(float(coordenadas[i][1]),float(coordenadas[i][2]),float(coordenadas[i][3]),float(coordenadas[x][1]),float(coordenadas[x][2]),float(coordenadas[x][3]))
                grafica.add_edge(coordenadas[i][0], coordenadas[x][0], costo)
        
    #grafica.print_graph()

"""
#Etapa 3 - Análisis de árboles de mínima expansión de los grafos de conectividad
"""
def prim(v0, graph=WeightedGraph, newGraph = WeightedGraph):
    
    cost = 0
    selected = [v0]
    newGraph.add_vertex(v0)
    remain = []
    vnext = None
    padre = None

    

    for i in graph.vertices():
        if i != v0 and len(graph.adjacent_vertices(i)) > 0:
            remain.append(i)
        
    while len(remain) > 0:
        minCost = float('inf')
        padre = None
        vnext = None

        for vector in selected:
            vecinos = graph._adjacency_list[vector]
            
            for vecino in vecinos:
                cn = vecino[1]

                if(cn < minCost and vecino[0] not in selected):
                    padre = vector
                    minCost = cn
                    vnext = vecino[0]
        
        if (vnext == None):
            print("No hay solucion")
            return None
        
        
        newGraph.add_vertex(vnext)
        newGraph.add_edge(padre,vnext,minCost)

        selected.append(vnext)
        remain.remove(vnext)

        cost = cost + minCost



    print(selected, cost)
    return(selected, cost)


"""
Etapa 4 - Cascos convexos de los vértices de los árboles de mínima expansión
"""

#Funcion para calcular el angulo entre 2 puntos, solo se considera x,y
def calcular_angulo_entre_puntos(xA,yA,xB,yB):

    angulo_rad = math.atan2(yB - yA, xB - xA)
    angulo_deg = math.degrees(angulo_rad)

    return angulo_deg

#Funcion para calcular si el giro es positivo
def giro(coordenadas, a,b,c):

    giros = (  (float(coordenadas[b][1]) - float(coordenadas[a][1])) * 
        (float(coordenadas[c][2]) - float(coordenadas[a][2])) 
        -
        (float(coordenadas[b][2]) - float(coordenadas[a][2])) * 
        (float(coordenadas[c][1]) - float(coordenadas[a][1]) )
        )
    return giros

#Funcion para obtener el casco convexo
#Se necesita el texto de las coordenadas y una grafica 
def graham(coordenadasTexto, graph=WeightedGraph):

    #Se leen el archivo para obtener los nombres y coordenadas
    coordenadas = np.loadtxt(coordenadasTexto,  dtype=str)

    #Se inicializan un par de variables en infinito y menos infinito
    minY = float('inf')
    minX = float('-inf')

    #Pivote temporal
    pivote = -1

    #Se busca el pivote que este más abajo hasta la derecha
    for i in range(len(coordenadas)):
        if (float(coordenadas[i][2]) <= minY and float(coordenadas[i][1]) > minX):
            minY = float(coordenadas[i][2])
            pivote = i
    
    #Se obtiene y se ordena la lista de los angulos en comparacion al pivote
    listaAngulos = []
    for x in range(len(coordenadas)):
        if x != pivote:
            angulo = calcular_angulo_entre_puntos(float(coordenadas[pivote][1]),float(coordenadas[pivote][2]),float(coordenadas[x][1]),float(coordenadas[x][2]))
            z = float(coordenadas[pivote][1])
            distancia = math.sqrt((float(coordenadas[x][1]) - float(coordenadas[pivote][1]))**2 + (float(coordenadas[x][2]) - float(coordenadas[pivote][2]))**2)
            listaAngulos.append((angulo,x, distancia))

    #angulo, vertice 
    listaAngulos = sorted(listaAngulos, key = lambda x: (x[0], x[2]))

    casco = [pivote, listaAngulos[0][1]]
    
 
    for s in listaAngulos[1:]:
        x = s[1]
        while giro(coordenadas, casco[-2], casco[-1],x) < 0:
            del casco[-1]
            if len(casco)<2:
                break
        
        casco.append(x)
    return casco

#Funcion para graficar los puntos dados por el algoritmo de graham4+
#Se necesita el texto de donde salen las coordenadas, y el return que da la funcion de graham
def plotGraham(mapatxt,hull):
    coordenadas = np.loadtxt(mapatxt,  dtype=str)
    x = []
    y = []

    for i in range(len(coordenadas)):
        if i in hull:
            x.append(float(coordenadas[i][1]))
            y.append(float(coordenadas[i][2]))
    plt.scatter(x,y)
    plt.show()


"""
Etapa 5 - Representación del grado de cada arista con diagramas de Voronoi
"""

def voronoi(coordenadastxt, gr = WeightedGraph):
    coordenadas = np.loadtxt(coordenadastxt, dtype=float, usecols=(1, 2))
    nombres = np.loadtxt(coordenadastxt, dtype=str, usecols=(0))

    aristas = []
    for x in range(len(nombres)):
        vecinos = gr.adjacent_vertices(nombres[x])
        aristas.append(len(vecinos))


    # generate Voronoi tessellation
    vor = Voronoi(coordenadas)

    # find min/max values for normalization
    minima = min(aristas)
    maxima = max(aristas)

    # normalize chosen colormap
    norm = mpl.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=cm.Blues_r)

    # plot Voronoi diagram, and fill finite regions with color mapped from speed value
    voronoi_plot_2d(vor, show_points=True, show_vertices=False, s=1)

    for r in range(len(vor.point_region)):
        region = vor.regions[vor.point_region[r]]
        if not -1 in region:
            polygon = [vor.vertices[i] for i in region]
            plt.fill(*zip(*polygon), color=mapper.to_rgba(aristas[r]))
    circle = plt.Circle((0,0),1, color = 'r', alpha = 0.25, fill = False)
    plt.gca().add_patch(circle)
    plt.show()


"""
Etapa 6 - Reporte
Llamar a las funciones
"""

#Etapa 1 -----------------------------------------------------------------
#Crear la grafica
gr = WeightedGraph(directed = False)

#Enviar a la funcion de graficas, el nombre de la matriz que vas a usar, el mapa de electrodos, y la grafica
#Esto sirve para llenar la grafica de sus vectores y aristas

#8 electerodos, las personales
#graficas('Lectura_Stef.txt','mapa8electrodos.txt',gr)
#graficas('Memoria_Stef.txt','mapa8electrodos.txt',gr)
#graficas('Operaciones_Stef.txt','mapa8electrodos.txt',gr)

#Las de 32 electrodos
#graficas('LecturaS0A.txt', 'mapa32electrodos.txt', gr)
graficas('MemoriaS0A.txt', 'mapa32electrodos.txt', gr)
#graficas('OperacionesS0A.txt', 'mapa32electrodos.txt', gr)


#Para graficar la grafica junto con sus caminos
#graficarGraficas8(gr)
graficarGraficas32(gr)

"""
    Para ver los caminos se usa la funcion de prepCaminos
    se envia el arregloOD correspondiente y la grafica
    Para ver los caminos, 0 grafica de 8, 1 grafica de 32
"""
#Arreglo origen destino, tuplas de donde parte a donde va el camino a explorar
#Arreglo para los viajes de 8 electrodos
arregloOD8 = [('Fz','PO8'),('C3','Oz'),('PO7','C4'),('Oz','PO7'),('Cz','Pz')]

#Arreglo para los viajes de 32 electrodos
arregloOD32 = [('F7','PO4'),('CP5','O2'),('P4','T7'),('AF3','CP6'),('F8','CP2'),('CP1','FC2'),('F3','O1')]


#prepCaminos(arregloOD8,0,gr)
prepCaminos(arregloOD32,1,gr)

grFloyd = WeightedGraphFloyd(directed = False)

#Matriz de conexion, 0 y 1
#graficas('Lectura_Stef.txt', 'mapa8electrodos.txt', grFloyd)
#graficas('Memoria_Stef.txt', 'mapa8electrodos.txt', grFloyd)
#graficas('Operaciones_Stef.txt', 'mapa8electrodos.txt', grFloyd)

#graficas('LecturaS0A.txt', 'mapa32electrodos.txt', grFloyd)
graficas('MemoriaS0A.txt', 'mapa32electrodos.txt', grFloyd)
#graficas('OperacionesS0A.txt', 'mapa32electrodos.txt', grFloyd)

print("Length of shortest paths Matriz Floyd")
print(floyd_marshall(grFloyd._adjacency_matrix))

#Parte 3

#Para prim se tiene que crear una nueva grafica que se llenara con los valores ddel arbol minimo
newGraph = WeightedGraph(directed = False)
#Se envia la funcion el grafico desde donde comenzar, una grafica ya al 100%, y la nueva grafica

#prim('Fz',gr, newGraph) #Para 8 electrodos
prim('FC5',gr, newGraph) #Para 32 electrodos


print("Grafica madre")
gr.print_graph()

print("Grafica PRIM")
#graficarGraficas8(newGraph)
graficarGraficas32(newGraph)

newGraph.print_graph()

#Parte 4
#Llamar a las funciones para hacer los cascos convexos
#grahamPoints = graham('mapa8electrodos.txt',newGraph)
#plotGraham('mapa8electrodos.txt', grahamPoints)

grahamPoints = graham('mapa32electrodos.txt',newGraph)
plotGraham('mapa32electrodos.txt', grahamPoints)

#Parte 5
#voronoi('mapa8electrodos.txt', gr)
voronoi('mapa32electrodos.txt', gr)