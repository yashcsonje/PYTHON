#A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. 
#When the constructor accepts arguments along with self, it is known as parameterized constructor.These arguments can be used inside the class to assign the values to the data members.

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group
obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

#Output: Crab belongs to the Crustaceans group.