from tkinter import *
from tkinter import ttk

root=Tk()

class Surprise:
    def __init__(self,master):
        self.lbl1= ttk.Label(master,text="Label")
        self.lbl1.grid()
        self.btn1=ttk.Button(master,text="Click for a surprise!")
        self.btn1.grid()
        self.btn1.config(command=self.method1)
        self.btn2=ttk.Button(master,text='delete',command=self.deletemsg)
        self.btn2.grid()
    def method1(self):
        self.lbl1.config(text="Surprise!")
    def deletemsg(self):
        self.lbl1.config(text="")



application=Surprise(root)

root.mainloop()