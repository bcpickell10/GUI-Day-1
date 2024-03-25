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

empl1 = Employee("Braden", "Pickell")
print(empl1.email())
