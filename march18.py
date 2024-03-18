from tkinter import *
from tkinter import ttk

root= Tk()

btn1=ttk.Button(root)
btn1.config(text="Click here for nothing to happen.")

btn1.grid(row=0, column=0)

btn2=Button(root,text="Click here for nothing to happen again.")

btn2.grid(row=0,column=1)
root.mainloop()