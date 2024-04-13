#Day 69
'''
In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data.
A class method is a type of method that is bound to the class and not the instance of the class.
In other words, it operates on the class as a whole, rather than on a specific instance of the class.
Class methods are defined using the "@classmethod" decorator, followed by a function definition.
The first argument of the function is always "cls," which represents the class itself.

class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)
'''

class Employee:
  company = "Apple" # Class variable to store the company name

  # Method to display employee details
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  # Class method to change the company for all instances of the class
  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee() # Creating an instance of Employee
e1.name = "Yash" # Adding a name attribute to the instance e1

# Calling the show method to display the details of the instance e1
e1.show() 

# Calling the class method changeCompany to change the company for all instances
e1.changeCompany("Microsoft") 

# Calling the show method again to display the updated details
e1.show() 
print(Employee.company) # Printing the company variable directly from the class

'''
Output:
The name is Yash and company is Apple
The name is Yash and company is Microsoft
Microsoft
'''