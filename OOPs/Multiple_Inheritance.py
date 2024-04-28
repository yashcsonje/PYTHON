#Day 79
'''
Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. 
This can be useful in situations where a class needs to inherit functionality from multiple sources.

In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.
class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body
In this example, the ChildClass inherits attributes and methods from all three parent classes: ParentClass1, ParentClass2, and ParentClass3.

It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes.
The MRO determines the order in which parent classes are searched for attributes and methods.
'''

# Define the Employee class representing an employee.
class Employee:
    def __init__(self, name):
        # Initialize the name attribute.
        self.name = name

    def show(self):
        # Display the name attribute.
        print(f"The name is {self.name}")

# Define the Dancer class representing a dancer.
class Dancer:
    def __init__(self, dance):
        # Initialize the dance attribute.
        self.dance = dance

    def show(self):
        # Display the dance attribute.
        print(f"The dance is {self.dance}")

# Define the DancerEmployee class inheriting from both Employee and Dancer.
class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        # Initialize attributes for both employee and dancer.
        self.dance = dance
        self.name = name

# Create an instance of DancerEmployee with dance as "Kathak" and name as "Shivani".
o = DancerEmployee("Kathak", "Shivani")

# Print the name and dance attributes.
print(o.name)    # Output: Shivani
print(o.dance)   # Output: Kathak

# Call the show method of DancerEmployee instance o.
o.show()         # Output: The name is Shivani (because Employee's show method is called by default)

# Call the show method of Dancer class explicitly with o as argument.
Dancer.show(o)  # Output: The dance is Kathak

# Print the method resolution order (MRO) of DancerEmployee class.
print(DancerEmployee.mro())

'''
Output:
Shivani
Kathak
The name is Shivani
The dance is Kathak
[<class '__main__.DancerEmployee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>]
'''