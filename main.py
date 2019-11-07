#Main program to create main frame


#Area de imports do programa
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
#-------***********-----------#
from mainCanvas import makeCanvas as mc


class App(tk.Tk):
  program_file = None

  def __init__(self):
    super().__init__()
    menu=tk.Menu(self)
    self.title("Graph Work")
    self.screen_width = self.winfo_screenwidth()
    self.screen_height = self.winfo_screenheight()
    self.geometry(str(self.screen_width)+"x"+str(self.screen_height))
    self.canvas = tk.Canvas(self, bg = "white", width = self.screen_width, height = self.screen_height)
    file_menu=tk.Menu(menu,tearoff=0)
    file_menu.add_command(label="New file", command = self.new_canvas)
    file_menu.add_command(label="Open", command = self.choose_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save", command = self.save_file)
    file_menu.add_command(label="Save as...", command = self.save_as)
    menu.add_cascade(labe="File",menu=file_menu)
    menu.add_command(label="About", command = self.create_aboutWindow)
    menu.add_command(label="Quit",command=self.leave_project)
    menu.add_command(label="Properties")
    self.config(menu=menu)
    self.new_canvas()
    
  #Função para abrir um arquivo  
  def choose_file(self):
    filetypes=(("Plain text files","*.txt"),
               ("Images","*.jpg *.gif *.png"),
               ("All files", "*"))
    filename=fd.askopenfilename(title="Open file",
               initialdir="/",
               filetypes=filetypes)
    inputFile = open(filename, "r")
    if(inputFile.readline() == "graph_reader:OK\n"):
      self.new_canvas()
      leitor = inputFile.readline()
      while True:
        leitor = inputFile.readline()
        if(leitor == "node_list\n"):
          break
        s = leitor.split()
        x1 = float(s[1])
        y1 = float(s[2])
        x2 = float(s[3])
        y2 = float(s[4])
        tag1 = s[5]
        if(tag1 == "node"):
          leitor = inputFile.readline()
          s = leitor.split()
          x3 = float(s[1])
          y3 = float(s[2])
          tag2 = s[3]
          self.canvasOrg.load_draw(x1,y1,x2,y2,tag1,x3,y3,tag2)
        else:
          self.canvasOrg.load_line(x1,y1,x2,y2)
      
      leitor = inputFile.readline()
      leitor = inputFile.readline()
      while True:
        leitor = inputFile.readline()
        if(leitor == "end"):
          break
        s = leitor.split('/')
        self.canvasOrg.insert_edge(int(s[1]), int(s[2]))
      
      inputFile.close()
      self.program_file = inputFile
      self.canvasOrg.graph.printMatrixes()

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

  #define a função save as
  def save_as(self):
    self.save_file(True)

  #Função para salvar um arquivo feito pelo programa
  def save_file(self, flag = False):
    if self.program_file == None or flag:
      new_file=fd.asksaveasfile(title="Save file",
                  defaultextension=".txt",
                  filetypes=(("Text files","*.txt"),))
      self.program_file = new_file
    
    if self.program_file:
      all_elements = self.canvas.find_all()
      
      with open(self.program_file.name, self.program_file.mode) as txt_file:
        txt_file.write("graph_reader:OK\n")
        txt_file.write("canvas\n")
        for elem in all_elements:
          txt_file.write(""+str(elem)+" ")
          for e in self.canvas.coords(elem):
            txt_file.write(str(e)+" ")
          for t in list(self.canvas.gettags(elem)):
            txt_file.write(t+" ")
          txt_file.write("\n")
        txt_file.write("node_list\n")
        for node in self.canvasOrg.get_node_list():
          txt_file.write(""+str(node)+" ")
        txt_file.write("\n")

        txt_file.write("edge_list\n")
        for edge in self.canvasOrg.get_edge_list():
          no1, no2 = edge
          txt_file.write("/"+str(no1)+"/"+str(no2)+"/\n")

        txt_file.write("end")

    self.program_file.close()

  #Função para criar um novo canvas e colocá-lo na tela
  def new_canvas(self):
    #Criação do canvas no projeto 
    self.canvas.delete("all")
    self.program_file = None
    self.canvasOrg = mc(self, self.canvas)
    self.canvasOrg.delete_graph()

  
app=App()
app.mainloop()
