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

  def draw_item(self, event):
    x, y = event.x, event.y
    bbox = (x-self.size, y-self.size, x+self.size, y+self.size)
    self.canvas.create_oval(*bbox, fill="blue", activefill="grey")
    elem_value = self.insert_node()
    self.canvas.create_text(x,y,fill = "white", font = "Times 20 bold", text=str(elem_value))

  def set_size(self, valor): 
    self.size = valor

  def insert_node(self):
      i = 0
      if(self.node_number > 0):
        elem = self.node_list[i]
        print(self.node_number)
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