#Day 77
'''
Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types.
This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.
Operator overloading allows you to create more readable and intuitive code.

For instance, consider a custom class that represents a point in 2D space.
You could define a method called 'add' to add two points together, but using the + operator makes the code more concise and readable:
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # prints 4, 6

You can overload an operator in Python by defining special methods in your class. 
These methods are identified by their names, which start and end with double underscores (__).
'''

class Vector:
    def __init__(self, i, j, k):
        # Initialize a Vector object with components i, j, and k.
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        # String representation of the Vector object.
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, other):
        # Overloaded addition operator (+) for Vector objects.
        # Returns a new Vector object with components sum of corresponding components.
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

# Instantiate two Vector objects v1 and v2.
v1 = Vector(3, 5, 6)
# Print the string representation of v1.
print(v1)

v2 = Vector(1, 2, 9)
# Print the string representation of v2.
print(v2)

# Add the two Vector objects v1 and v2 and store the result in result.
result = v1 + v2
# Print the string representation of the result.
print(result)
# Print the type of the result.
print(type(result))


'''
Output:
3i + 5j + 6k
1i + 2j + 9k
4i + 7j + 15k
<class '__main__.Vector'>
'''
