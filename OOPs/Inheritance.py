#Day 61
'''
When a class derives from another class.
The child class will inherit all the public and protected properties and methods from the parent class.
In addition, it can have its own properties and methods,this is called as inheritance.

Python Inheritance Syntax
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
'''
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def ShowDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
    
class Programmer(Employee):
    def ShowLanguage(self):
        print("The default language is Python")
        
e1=Employee("Rohan Das",400)
e1.ShowDetails()
print()
e2=Programmer("Harry",4100)
e2.ShowDetails()
e2.ShowLanguage()

'''
Output:
The name of Employee: 400 is Rohan Das

The name of Employee: 4100 is Harry
The default language is Python
'''
