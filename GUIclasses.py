from tkinter import *
from tkinter import ttk

root = Tk()

class GreetingApp:
    def __init__(self, master):
        self.label1 = ttk.Label(master)
        self.label1.config(text="Hello")
        self.label1.grid()
        
        self.btn1 = ttk.Button(master)
        self.btn1.config(text="Press Here", command=self.goodbye_method)
        self.btn1.grid()  # Corrected from self.btn.grid()

    def goodbye_method(self):
        self.label1.config(text="Goodbye")
    

app = GreetingApp(root)  # Pass root to the GreetingApp constructor
root.mainloop()
