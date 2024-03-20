from tkinter import *
from tkinter import ttk

root=Tk()

framePack=ttk.LabelFrame(root)
framePack.grid()
framePack.config(padding=(30,30))
framePack.config(text=".pack")
framePack.config(relief="solid")



frameGrid=ttk.LabelFrame(root)
frameGrid.grid(row=0,column=1)
frameGrid.config(height=100,width=200)
frameGrid.config(text=".grid")


framePlace=ttk.LabelFrame(root)
framePlace.grid(row=1,column=0)
framePlace.config(height=100,width=200)
framePlace.config(text=".place")


btn1=ttk.Button(framePack,text="Left Side")
btn1.pack()


root.mainloop()