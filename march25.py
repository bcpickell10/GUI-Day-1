# Creating functions
def numoperator (num1,num2,operator):
    if operator=='Multiply':
        return num1*num2
    if operator=="Add":
        return num1+num2
    

# Creating Classes    
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return self.first + "." + self.last + "@company.com"
    def fullname(self):
        return self.first+" "+self.last 
empl1 = Employee("Braden", "Pickell")
empl2 = Employee("Hillary","Cliffbar")
print(empl1.fullname())
print(empl2.email())
