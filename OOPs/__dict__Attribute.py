#Day 70
'''
The __dict__ attribute returns a dictionary representation of an object's attributes. 
It is a useful tool for introspection.
'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person("John",30)
print(p.__dict__)

'''
Output:
{'name': 'John', 'age': 30}
'''