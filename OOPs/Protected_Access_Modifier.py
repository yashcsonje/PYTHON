'''
In object-oriented programming (OOP), "protected" refers to a member (method or attribute) of a class intended for access by the class itself and its subclasses.
In Python, the convention for denoting a member as protected is by prefixing its name with a single underscore (_).
For example, a method named _my_method in a class indicates that it should only be accessed by the class itself and its subclasses.
However, it's essential to understand that the single underscore is merely a naming convention and does not enforce protection or restrict access to the member.
To denote a variable as protected, follow the syntax of writing the variable name followed by a single underscore (_), like _varName.
'''

class Student:
    def __init__(self):
        self._name = "Yash"

    def _funName(self):      # protected method
        return "aawara_gardi"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())

'''
Output:
Yash
aawara_gardi
Yash
aawara_gardi
'''