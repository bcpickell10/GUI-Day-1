# Frame Practice

from tkinter import *
from tkinter import ttk


root=Tk()\

frame1=ttk.Frame(root,relief="solid",padding=(12,12))
frame1.grid()


btn1=ttk.Button(frame1,text="Click here")
btn1.grid()


btn2=ttk.Button(frame1,text="Button2")
btn2.grid()


frame2=ttk.Frame(root,relief="solid",padding=(12,12))
frame2.grid()


btn3=ttk.Button(frame2,text="Button3")
btn3.pack()


btn4=ttk.Button(frame2,text="Button4")
btn4.pack()
root.mainloop()