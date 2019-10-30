#Main program to create main frame

# Creating Menu Bar example

import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    menu=tk.Menu(self)
    self.title("Graph Work")
    file_menu=tk.Menu(menu,tearoff=0)
    file_menu.add_command(label="New file")
    file_menu.add_command(label="Open", command = self.choose_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save as...")
    menu.add_cascade(labe="File",menu=file_menu)
    menu.add_command(label="About")
    menu.add_command(label="Quit",command=self.leave_project) 
    self.config(menu=menu)
	
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
    mb.askokcancel
    print(response)
    self.destroy
		

app=App()
app.mainloop()
