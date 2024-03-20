from tkinter import *
from tkinter import ttk


root=Tk()
root.geometry("300x300")

btn1=ttk.Button(root,text="1")
btn1.grid()

#can put the name of the side lowercase in quotes

btn2=ttk.Button(root,text="2")
btn2.grid(row=0,column=1)


btn3=ttk.Button(root,text="3")
btn3.grid(row=0,column=2)

root.mainloop()