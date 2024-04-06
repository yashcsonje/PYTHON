#Day 62
'''
Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. 
Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.
Ex:
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
'''

class Student:
    def __init__(self, age, name):
        self.__age = age      # Private variable
        
    def __funName(self):      # Private method
        self.y = 34
        print(self.y)

class Subject(Student):
    pass

obj = Student(21, "Harry")
obj1 = Subject(25, "John")  # Instantiating Subject with required arguments

# Accessing private members using name mangling
print(obj._Student__age)    # Accessing __age variable
print(obj1._Student__age)   # Accessing __age variable of Subject
obj._Student__funName()     # Accessing __funName method

'''
Output:
21
25
34
'''
