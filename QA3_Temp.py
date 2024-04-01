from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Window Title")

class QuestionAnswer:
    def __init__(self,master,strQuestion,listAnswers,correctAnswer):
        self.correctAnswer=correctAnswer
        self.frameQA=ttk.Frame(master,relief="raised",padding=(5,5))
        self.frameQA.grid()
        self.label1=ttk.Label(self.frameQA,text=strQuestion)
        self.label1.grid()
        self.answerOptions=ttk.Combobox(self.frameQA)
        self.answerOptions.grid()
        self.answerOptions.config(values=listAnswers)
        self.testButton=ttk.Button(self.frameQA,text="Submit",command=self.checkAnswer)
        self.testButton.grid()
        self.labelfeedback=ttk.Label(self.frameQA)
        self.labelfeedback.grid()
    def checkAnswer (self):
        if self.answerOptions.get()==self.correctAnswer:
            self.labelfeedback.config(text="Correct!",foreground="green")
        else:
            self.labelfeedback.config(text="Incorrect.",foreground="red")
        


listAnswerFromQ1=["Green","Blue","Red","Yellow"]
strQuestion1="What is Braden Pickell's favorite color?"
bradensfavcolor="Green"
q1=QuestionAnswer(root,strQuestion1,listAnswerFromQ1,bradensfavcolor)

root.mainloop()