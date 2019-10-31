#Main program to create main frame

# Creating Menu Bar example

import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from mainCanvas import makeCanvas as mc

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    menu=tk.Menu(self)
    self.title("Graph Work")
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    self.geometry(str(screen_width)+"x"+str(screen_height))
    file_menu=tk.Menu(menu,tearoff=0)
    file_menu.add_command(label="New file")
    file_menu.add_command(label="Open", command = self.choose_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save as...")
    menu.add_cascade(labe="File",menu=file_menu)
    menu.add_command(label="About", command = self.create_aboutWindow)
    menu.add_command(label="Quit",command=self.leave_project) 
    self.config(menu=menu)
    
    #Criação do canvas no projeto 
    self.canvas = tk.Canvas(self, width = self.winfo_width(), height = self.winfo_height())
    self.canvasOrg = mc(self.canvas)
    
  def choose_file(self):
    filetypes=(("Plain text files","*.txt"),
               ("Images","*.jpg *.gif *.png"),
               ("All files", "*"))
    filename=fd.askopenfilename(title="Open file",
               initialdir="/",
               filetypes=filetypes)
    if filename:
      print(filename)

  def choose_directory(self):
    directory=fd.askdirectory(title="Open directory",
               initialdir="/")
    if directory:
      print(directory)
  
  #Criar uma janela que pede confirmação para sair.
  def leave_project(self):
    MsgBox  = tk.messagebox.askquestion('Exit Application', 'Are you sure?', icon = 'warning')
    
    if MsgBox == 'yes':
      self.destroy()
    else:
      tk.messagebox.showinfo('Return', 'You will return to the application')
  
  def create_aboutWindow(self):
    aboutWindow = tk.Toplevel(self)
    display = tk.Label(aboutWindow, text = "Python work About Graphs\nGroup= Alex Junior Pereira\nLeonardo Henrique de Melo")
    display.pack()
    
app=App()
app.mainloop()
