#Day 72
'''
The super() keyword in Python is used to refer to the parent class. 
It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.
However, sometimes you might want to use the parent class method in the child class. 
This is where the super() keyword comes in handy.
'''

# Define a base class 'Employee' with attributes name and id.
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

# Define a subclass 'Programmer' inheriting from 'Employee'.
# It adds an additional attribute 'lang' for programming language.
class Programmer(Employee):
  def __init__(self, name, id, lang):
    # Call the constructor of the base class 'Employee' using super().
    super().__init__(name, id)
    self.lang = lang

# Create an instance of 'Employee' with name "Rohan Das" and id "420".
rohan = Employee("Rohan Das", "420")

# Create an instance of 'Programmer' with name "Harry", id "2345", and language "Python".
harry = Programmer("Harry", "2345", "Python")

# Print attributes of 'Programmer' instance 'harry'.
print(harry.name)  # Output: Harry
print(harry.id)    # Output: 2345
print(harry.lang)  # Output: Python
