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
        #self.printMatrixes()

    
    def insertEdge(self,edge):
        self.edges.append(edge)
        self.updateEdges()
    
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
        self.incidence_matrix = nx.incidence_matrix(self.G)
    
    def makeAdjacencyMatrix(self):
        self.adjacency_matrix = nx.adjacency_matrix(self.G)
    
    def deleteGraph(self):
        self.G = nx.DiGraph()
        del(self.nodes[:])
        del(self.edges[:])
        self.incidence_matrix = None
        self.adjacency_matrix = None
    
    def printMatrixes(self):
        print("Matriz de incidência")
        print(self.adjacency_matrix.toarray())
        print("Matriz de adjacência")
        print(self.incidence_matrix.toarray())

