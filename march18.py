from tkinter import *
from tkinter import ttk

root= Tk()

btn1=ttk.Button(root)
btn1.config(text="Button 1")

btn1.grid(row=0, column=0)

btn2=Button(root,text="Button 2")

btn2.grid(row=1,column=1)

btn3=Button(root,text="Button 3")

btn3.grid(row=2,column=2)

btn4=Button(root,text="Button 4")

btn4.grid(row=3,column=3)
root.mainloop()