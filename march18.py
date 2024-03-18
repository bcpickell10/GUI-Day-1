from tkinter import *
from tkinter import ttk

root= Tk()

btn1=ttk.Button(root)
btn1.config(text="Click here for nothing to happen.")

btn1.grid()

btn2=Button(root,text="Click here for nothing to happen again.")

btn2.grid()
root.mainloop()