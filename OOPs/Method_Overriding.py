#Day 74
'''
Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class.
The method in the derived class is said to override the method in the base class.
When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.
In Python, method overriding is a way to customize the behavior of a class based on its specific needs. 
'''

# Define a base class 'Shape' to represent geometric shapes.
class Shape:
    def __init__(self, x, y):
        # Initialize shape dimensions.
        self.x = x
        self.y = y

    def area(self):
        # Method to calculate and return the area of the shape.
        return self.x * self.y
    
# Define a subclass 'Circle' inheriting from 'Shape'.
class Circle(Shape):
    def __init__(self, radius):
        # Initialize the radius of the circle.
        self.radius = radius
    
    def area(self):
        # Method overriding: Calculate and return the area of the circle.
        return 3.14 * self.radius * self.radius

# Create an instance of 'Shape' representing a rectangle with dimensions 3x5.
rec = Shape(3, 5)
# Print the area of the rectangle.
print(rec.area())

# Create an instance of 'Circle' with radius 5.
c = Circle(5)
# Print the area of the circle.
print(c.area())

'''
Output:
15
78.5
'''
