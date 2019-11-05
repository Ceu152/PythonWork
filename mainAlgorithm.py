#Arquivo que realiza o processamento sobre grafos
import numpy as np
import networkx as nx

class graphStructure:
    nodes = []
    edges = []
    oriented = False

    def __init__(self):
        self.G = nx.DiGraph()
        #self.updateNodes()
        #self.updateEdges()
      

    def insertNode(self,node):
        self.nodes.append(node)
        self.updateNodes()
        print(self.nodes)
        #self.printMatrixes()

    
    def insertEdge(self,edge):
        self.edges.append(edge)
        self.updateEdges()
        print(self.edges)
    
    #def deleteNode():
    
    #def deleteEdge():

    def updateNodes(self):
        self.G.add_nodes_from(self.nodes)
        self.makeIncidenceMatrix()
        self.makeAdjacencyMatrix()

    def updateEdges(self):
        self.G.add_edges_from(self.edges)
        self.makeIncidenceMatrix()
        self.makeAdjacencyMatrix()

    def makeIncidenceMatrix(self):
        self.incidence_matrix = -nx.incidence_matrix(self.G)
    
    def makeAdjacencyMatrix(self):
        self.adjacency_matrix = -nx.adjacency_matrix(self.G)
    
    def deleteGraph(self):
        self.G = None
        self.makeIncidenceMatrix()
        self.makeAdjacencyMatrix()
    
    def printMatrixes(self):
        print("Matriz de incidência")
        print(self.adjacency_matrix.toarray())
        print("Matriz de Incidência")
        print(self.incidence_matrix.toarray())

