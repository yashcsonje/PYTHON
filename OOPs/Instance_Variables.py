#Day 66
'''
Instance variables are defined at the instance level and are unique to each instance of the class.
They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
For example, an instance variable can be used to store the name of an employee in a class that represents an employee.
'''

class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane