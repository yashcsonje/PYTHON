#Day 70
'''
The help() function is used to get help documentation for an object, including a description of its attributes and methods.
''' 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=Person("John",30)
print(help(Person))

'''
Output:
Help on class Person in module __main__:

class Person(builtins.object)
 |  Person(name, age)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
-- More  --
'''