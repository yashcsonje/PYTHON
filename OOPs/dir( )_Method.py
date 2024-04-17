#Day 71
'''
We must look into dir(), __dict__() and help() attribute/methods in python. 
They make it easy for us to understand how classes resolve various functions and executes code. 
In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help().

The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. 
It is a useful tool for discovering what you can do with an object.
'''

x=[1,2,3]
dir(x)
print(dir(x))

'''
Output:
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 
'insert', 'pop', 'remove', 'reverse', 'sort']
'''
