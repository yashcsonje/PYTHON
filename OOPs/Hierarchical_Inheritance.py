#Day 81
'''
Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class.
In other words, a single base class acts as a parent class for multiple subclasses.
This is a way of establishing relationships between classes in a hierarchical manner.
'''

# Define the base class Animal
class Animal:
    def __init__(self, name):
        # Initialize the name attribute
        self.name = name
    
    def show_details(self):
        # Display details about the animal
        print("Name:", self.name)

# Define the subclass Dog, inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class (Animal) to initialize name
        Animal.__init__(self, name)
        # Initialize the breed attribute
        self.breed = breed

    def show_details(self):
        # Call the show_details method of the parent class (Animal) to display basic details
        Animal.show_details(self)
        # Print breed-specific detail
        print("Species: Dog")
        print("Breed:", self.breed)

# Define the subclass Cat, inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the parent class (Animal) to initialize name
        Animal.__init__(self, name)
        # Initialize the color attribute
        self.color = color

    def show_details(self):
        # Call the show_details method of the parent class (Animal) to display basic details
        Animal.show_details(self)
        # Print color-specific detail
        print("Species: Cat")
        print("Color:", self.color)

# Create an instance of Dog with name "Max" and breed "Golden Retriever"
dog = Dog("Max", "Golden Retriever")
# Display details about the dog
dog.show_details()

# Create an instance of Cat with name "Luna" and color "Black"
cat = Cat("Luna", "Black")
# Display details about the cat
cat.show_details()

'''
Output:
Name: Max
Species: Dog
Breed: Golden Retriever
Name: Luna
Species: Cat
Color: Black
'''