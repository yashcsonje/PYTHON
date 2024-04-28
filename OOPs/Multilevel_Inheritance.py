#Day 80
'''
Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class.
This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.
In Python, multilevel inheritance is achieved by using the class hierarchy.
The syntax for multilevel inheritance is quite simple and follows the same syntax as single inheritance.

class BaseClass:
    # Base class code
    
class DerivedClass1(BaseClass):
    # Derived class 1 code
    
class DerivedClass2(DerivedClass1):
    # Derived class 2 code
In the above example, we have three classes: BaseClass, DerivedClass1, and DerivedClass2.
The DerivedClass1 class inherits from the BaseClass, and the DerivedClass2 class inherits from the DerivedClass1 class.
This creates a hierarchy where DerivedClass2 has access to all the attributes and methods of both DerivedClass1 and BaseClass.
'''
# Define the base class Animal
class Animal:
    def __init__(self, name, species):
        # Initialize name and species attributes
        self.name = name
        self.species = species
        
    def show_details(self):
        # Print details about the animal
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
# Define the subclass Dog, inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class (Animal) to initialize name and species
        Animal.__init__(self, name, species="Dog")
        # Initialize breed attribute
        self.breed = breed
        
    def show_details(self):
        # Call the show_details method of the parent class (Animal) to display basic details
        Animal.show_details(self)
        # Print breed-specific detail
        print(f"Breed: {self.breed}")
        
# Define the subclass GoldenRetriever, inheriting from Dog
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        # Call the constructor of the parent class (Dog) to initialize name and breed
        Dog.__init__(self, name, breed="Golden Retriever")
        # Initialize color attribute
        self.color = color
        
    def show_details(self):
        # Call the show_details method of the parent class (Dog) to display basic details
        Dog.show_details(self)
        # Print color-specific detail
        print(f"Color: {self.color}")

# Create an instance of GoldenRetriever with name "Tommy" and color "Black"
o = GoldenRetriever("Tommy", "Black")

# Call the show_details method of the GoldenRetriever instance to display all details
o.show_details()

# Output the method resolution order (MRO) for the GoldenRetriever class
print(GoldenRetriever.mro())

'''
Output:
Name: Tommy
Species: Dog
Breed: Golden Retriever
Color: Black
[<class '__main__.GoldenRetriever'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]
'''