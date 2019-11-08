#Arquivo que manipula as ações sobre o canvas


import tkinter as tk
import math
from functools import partial
import math
#-------***********-----------#
from mainAlgorithm import graphStructure as gS

class makeCanvas:
  #varivaeis usadas para o desenho dos nós 
  nodeColor = "blue"
  activeNodeColor = "grey"
  textColor = "white"
  
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
      self.item = self.canvas.create_oval(*bbox, fill=self.nodeColor, activefill=self.activeNodeColor, tags = "node")
      elem_value = self.insert_node(self.item)
      text = self.canvas.create_text(x,y,fill = "white", font = "Times 20 bold", text=str(elem_value), tags = "text")
      self.canvas.tag_bind(text, '<Enter>', self.textFocus)
      self.canvas.tag_bind(text, '<Leave>', self.textUnfocus)
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
    node = self.canvas.find_withtag(tk.CURRENT)

    if(node!=()):
      tag = self.canvas.itemcget(node, "tags").split(" ")[0]
      node = node[0]

      #assim ele pegara textos tambem
      if(tag=="text"):
        node=node-1

      #no caso de ser uma edge
      if(tag=="text" or tag=="node"):
        x0, y0, x1, y1 = self.canvas.coords(node)
      else:
        return True

      self.draw_Edge(node, x1, y1)
      return False

    return True
  
  #Desenha uma aresta de um grafo
  def draw_Edge(self, node, x1, y1):
    if not self.line_start:
      self.line_start = (x1-self.size,y1-self.size,self.node_list.index(node))
    else:
      x_origin,y_origin,node_origin = self.line_start
      
      #tirando edge do node
      angle = math.pi/2
      if((y1-self.size-y_origin)!=0):
        angle = math.atan((x1-self.size-x_origin)/(y1-self.size-y_origin))
      else:
        if(x_origin>x1-self.size):
          angle = -1*angle
      xoffset = self.size*math.sin(angle)
      yoffset = self.size*math.cos(angle)
      if(y1-self.size<y_origin):
        yoffset = -1*yoffset
        xoffset = -1*xoffset

      self.line_start=None
      line=(x_origin+xoffset,y_origin+yoffset,x1-self.size-xoffset,y1-self.size-yoffset)
      self.canvas.create_line(*line, fill = "black",tags = "line")
      self.graph.insertEdge((node_origin,self.node_list.index(node)))

  #Ao colocar mouse sobre o texto, trocar cor do node
  def textFocus(self, event):
    text = self.canvas.find_withtag(tk.CURRENT)
    if(text!=()):
      text=text[0]
      self.canvas.itemconfigure(text-1,fill=self.activeNodeColor)
  
  #Ao tirar mouse sobre o texto, voltar a cor do node
  def textUnfocus(self, event):
    text = self.canvas.find_withtag(tk.CURRENT)
    if(text!=()):
      text=text[0]
      self.canvas.itemconfigure(text-1,fill=self.nodeColor)

  def lineFocus(self, event):
    print("linha")
  
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
    self.item = self.canvas.create_oval(*bbox, fill=self.nodeColor, activefill=self.activeNodeColor, tags = tag1)
    elem_value = self.insert_node(self.item)
    text = self.canvas.create_text(x3,y3,fill = self.textColor, font = "Times 20 bold", text=str(elem_value), tags = tag2)
    self.canvas.tag_bind(text, '<Enter>', self.textFocus)
    self.canvas.tag_bind(text, '<Leave>', self.textUnfocus)

  #Carrega as arestas de um arquivo
  def load_line(self, x1,y1,x2,y2):
    line=(x1, y1,x2, y2)
    self.canvas.create_line(*line, fill = "black", tags = "line")
    #self.graph.insertEdge((node_origin,self.node_list.index(node)))
  
  #Apaga as o grafo escrito matemáticamente
  def delete_graph(self):
    del(self.node_list[:])
    self.graph.deleteGraph()

  #função que recebe as arestas
  def get_edge_list(self):
    return self.graph.edges

  #função que insere arestas
  def insert_edge(self, e1, e2):
    self.graph.insertEdge((e1,e2))

  #função update node color
  def update_node(self):
    all_items = self.canvas.find_withtag("node")
    for item in all_items:
      self.canvas.itemconfigure(item,fill=self.nodeColor)
  
  #função update text color
  def update_text(self):
    all_items = self.canvas.find_withtag("text")
    for item in all_items:
      self.canvas.itemconfigure(item,fill=self.textColor)