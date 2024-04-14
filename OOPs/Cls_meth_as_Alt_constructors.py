#Day 70
'''
However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.
One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary.
'''
class Employee:
    def __init__(self, name, salary):
        # Initialize the instance variables name and salary
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        # Class method to create an instance of Employee from a string
        # Split the string by "-" to separate name and salary
        name, salary = string.split("-")
        # Create and return a new instance of Employee using the extracted name and salary
        return cls(name, int(salary))

# Creating an instance of Employee using the standard constructor
e1 = Employee("Yash", 12000)
print(e1.name)  # Printing the name of e1
print(e1.salary)  # Printing the salary of e1

# Creating an instance of Employee using the class method fromStr
string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)  # Printing the name of e2
print(e2.salary)  # Printing the salary of e2

'''
Output:
Yash
12000
John
12000
'''