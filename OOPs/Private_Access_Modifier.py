#Day 62
'''
By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class.
We cannot use private members outside of class.

In Python, private members of a class are indicated by prefixing their names with a double underscore (__). 
his convention signals that they should not be accessed or modified from outside the class, though technically they can still be accessed.
This is a convention rather than a strict rule, promoting encapsulation and abstraction within the class.
'''

class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())

'''
Output:
AttributeError: 'student' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
AttributeError: 'subject' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
'''