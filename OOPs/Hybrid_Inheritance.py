#Day 81
'''
Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming.
It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.
In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

The syntax for implementing Hybrid Inheritance in Python is the same as for implementing Single Inheritance, Multiple Inheritance, or Hierarchical Inheritance.
class BaseClass1:
  # attributes and methods

class BaseClass2:
  # attributes and methods

class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods
'''

# Define the base class Human
class Human:
    def __init__(self, name, age):
        # Initialize name and age attributes
        self.name = name
        self.age = age
    
    def show_details(self):
        # Display details about the human
        print("Name:", self.name)
        print("Age:", self.age)
    
# Define the subclass Person, inheriting from Human
class Person(Human):
    def __init__(self, name, age, address):
        # Call the constructor of the parent class (Human) to initialize name and age
        Human.__init__(self, name, age)
        # Initialize address attribute
        self.address = address
    
    def show_details(self):
        # Call the show_details method of the parent class (Human) to display basic details
        Human.show_details(self)
        # Print address-specific detail
        print("Address:", self.address)

# Define a standalone class Program
class Program:
    def __init__(self, program_name, duration):
        # Initialize program_name and duration attributes
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        # Display details about the program
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)

# Define the subclass Student, inheriting from Person and Program
class Student(Person):
    def __init__(self, name, age, address, program):
        # Call the constructor of the parent class (Person) to initialize name, age, and address
        Person.__init__(self, name, age, address)
        # Initialize program attribute
        self.program = program

    def show_details(self):
        # Call the show_details method of the parent class (Person) to display basic details
        Person.show_details(self)
        # Call the show_details method of the program attribute to display program-specific details
        self.program.show_details()

# Create an instance of Program with program_name "Electrical" and duration "4 years"
program = Program("Electrical", "4 years")
# Create an instance of Student with name "Yash Sonje", age 20, address "123 Main St.", and program instance
student = Student("Yash Sonje", 20, "123 Main St.", program)
# Display details about the student
student.show_details()

'''
Output:
Name: Yash Sonje
Age: 20
Adress: 123 Main St.
Program Name: Electrical
Duration: 4 years
'''