#Main program to create main frame


#Area de imports do programa
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
#-------***********-----------#
from mainCanvas import makeCanvas as mc


class App(tk.Tk):
  def __init__(self):
    super().__init__()
    menu=tk.Menu(self)
    self.title("Graph Work")
    self.screen_width = self.winfo_screenwidth()
    self.screen_height = self.winfo_screenheight()
    self.geometry(str(self.screen_width)+"x"+str(self.screen_height))
    file_menu=tk.Menu(menu,tearoff=0)
    file_menu.add_command(label="New file", command = self.new_canvas)
    file_menu.add_command(label="Open", command = self.choose_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save", command = self.save_file)
    file_menu.add_command(label="Save as...", command = self.save_file)
    menu.add_cascade(labe="File",menu=file_menu)
    menu.add_command(label="About", command = self.create_aboutWindow)
    menu.add_command(label="Quit",command=self.leave_project)
    menu.add_command(label="Properties")
    self.config(menu=menu)
    
  #Função para abrir um arquivo  
  def choose_file(self):
    filetypes=(("Plain text files","*.txt"),
               ("Images","*.jpg *.gif *.png"),
               ("All files", "*"))
    filename=fd.askopenfilename(title="Open file",
               initialdir="/",
               filetypes=filetypes)
    if filename:
      print(filename)

  #Função para escolher um diretório 
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
  
  #Criação da Janela de about do programa
  def create_aboutWindow(self):
    aboutWindow = tk.Toplevel(self)
    display = tk.Label(aboutWindow, text = "Python work About Graphs\nGroup= Alex Junior Pereira\nLeonardo Henrique de Melo")
    display.pack()

  #Função para salvar um arquivo feito pelo programa
  def save_file(self):
    new_file=fd.asksaveasfile(title="Save file",
                defaultextension=".txt",
                filetypes=(("Text files","*.txt"),))
    if new_file:
      new_file.write()
      new_file.close()

  #Função para criar um novo canvas e colocá-lo na tela
  def new_canvas(self):
    #Criação do canvas no projeto 
    self.canvas = tk.Canvas(self, bg = "white", width = self.screen_width, height = self.screen_height)
    self.canvasOrg = mc(self, self.canvas)

  
app=App()
app.mainloop()
