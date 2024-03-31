#Day 62
'''
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
Types of access specifiers
1. Public access modifier
2. Private access modifier
3. Protected access modifier

All the variables and methods (member functions) in python are by default public. 
Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
'''

class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)

'''
Output:
21
Harry
'''