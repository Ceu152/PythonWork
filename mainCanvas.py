#Arquivo que manipula as ações sobre o canvas


import tkinter as tk
import math
from functools import partial
#-------***********-----------#
from mainAlgorithm import graphStructure as gS

class makeCanvas:
  
  #Variveis que pertencem a todos os nós
  node_list = list()
  node_number = 0
  size = 30
  def __init__(self, root ,canvas):
    self.root = root
    self.canvas = canvas
    self.graph = gS() 
    self.canvas.pack()
    self.canvas.bind("<Button-1>", self.draw_item)
    self.line_start = None

  #Verifica se o clique foi em uma area livre e desenha um nó
  def draw_item(self, event):
    x, y = event.x, event.y
    if(self.verify_pos(x,y)):
      bbox = (x-self.size, y-self.size, x+self.size, y+self.size)
      self.item = self.canvas.create_oval(*bbox, fill="blue", activefill="grey", tags = "node")
      elem_value = self.insert_node(self.item)
      self.canvas.create_text(x,y,fill = "white", font = "Times 20 bold", text=str(elem_value), tags = "number")
      self.line_start = None
    
  #Define o tamanho dos nós
  def set_size(self, valor): 
    self.size = valor

  #Insere um nó na lista
  def insert_node(self,c_item):
      i = 0
      if(self.node_number > 0):
        elem = self.node_list[i]
        while (elem != -1 and i < self.node_number-1):
          elem = self.node_list[i]
          i += 1
        
        i+= 1

        if i < self.node_number-1:
          self.node_list[i] = i
        else:
          self.node_list.append(c_item)
          self.node_number += 1
      else:
          self.node_list.append(c_item)
          self.node_number += 1

      self.graph.insertNode(i)

      return i

  #Verifica se há um nó local
  def verify_pos(self, x, y):
    all_nodes = self.canvas.find_withtag("node")

    for node in all_nodes:
      x0, y0, x1, y1 = self.canvas.coords(node)
      if(x > x0 and x < x1 and y > y0 and y < y1):
        self.draw_Edge(node, x1, y1)
        return False

    return True
  
  #Desenha uma aresta de um grafo
  def draw_Edge(self, node, x1, y1):
    if not self.line_start:
      self.line_start = (x1-self.size,y1-self.size,self.node_list.index(node))
    else:
      x_origin,y_origin,node_origin = self.line_start
      self.line_start=None
      #calculate_angle(x_origin, y_origin, x1-self.size, y1-self.size)
      line=(x_origin,y_origin,x1-self.size,y1-self.size)
      self.canvas.create_line(*line, fill = "black", tags = "line")
      self.graph.insertEdge((node_origin,self.node_list.index(node)))
  
  #Calcular o angulo entre dois nós
  def calculate_angle(self,x1,y1,x2,y2):
    x = x2-x1
    y = y2-y1
    tetha = math.atan(abs(y/x))
    return tetha
  
  #Retorna a lista de nós nos grafos
  def get_node_list(self):
      return self.node_list

  #Carrega os nós de um arquivo
  def load_draw(self,x1,y1,x2,y2,tag1,x3,y3,tag2):
    bbox = (x1, y1, x2, y2)
    self.item = self.canvas.create_oval(*bbox, fill="blue", activefill="grey", tags = tag1)
    elem_value = self.insert_node(self.item)
    self.canvas.create_text(x3,y3,fill = "white", font = "Times 20 bold", text=str(elem_value), tags = tag2)

  #Carrega as arestas de um arquivo
  def load_line(self, x1,y1,x2,y2):
    line=(x1, y1,x2, y2)
    self.canvas.create_line(*line, fill = "black", tags = "line")
    #self.graph.insertEdge((node_origin,self.node_list.index(node)))
  
  #Apaga as o grafo escrito matemáticamente
  def delete_graph(self):
    del(self.node_list[:])
    self.graph.deleteGraph()