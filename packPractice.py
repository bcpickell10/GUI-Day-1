from tkinter import *
from tkinter import ttk


root=Tk()
root.geometry("300x300")

btn1=ttk.Button(root,text="Left Side")
btn1.pack(side="left")

#can put the name of the side lowercase in quotes

btn2=ttk.Button(root,text="Top Side")
btn2.pack(side=TOP)

root.mainloop()