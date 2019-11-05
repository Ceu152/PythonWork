#Arquivo que manipula as ações sobre o canvas


import tkinter as tk
from functools import partial

class makeCanvas:
  #Variveis que pertencem a todos os nós
  node_list = list()
  node_number = 0
  size = 30
  def __init__(self, root ,canvas):
    self.root = root
    self.canvas = canvas
    self.canvas.pack()
    self.canvas.bind("<Button-1>", self.draw_item)
    self.line_start = None

  def draw_item(self, event):
    x, y = event.x, event.y
    bbox = (x-self.size, y-self.size, x+self.size, y+self.size)
    self.item = self.canvas.create_oval(*bbox, fill="blue", activefill="grey")
    if(self.verify_pos()):
      elem_value = self.insert_node()
      self.canvas.create_text(x,y,fill = "white", font = "Times 20 bold", text=str(elem_value))
    else:
      self.canvas.delete(self.item)
    

  def set_size(self, valor): 
    self.size = valor

  def insert_node(self):
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
          self.node_list.append(i)
          self.node_number += 1
      else:
          self.node_list.append(i)
          self.node_number += 1

      return i

  def verify_pos(self):
    all_items = self.canvas.find_all()
    x0, y0, x1, y1 = self.canvas.coords(self.item)

    items = self.canvas.find_overlapping(x0, y0, x1, y1)

    for item in filter(lambda i: i is not self.item, items):
      if not self.line_start:
        self.line_start = (x1-self.size,y1-self.size)
        print(self.line_start)
      else:
        x_origin,y_origin = self.line_start
        self.line_start=None
        line=(x_origin,y_origin,x1-self.size,y1-self.size)
        self.canvas.create_line(*line, fill = "black")
      return False
      

    return True