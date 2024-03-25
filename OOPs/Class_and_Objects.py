class Details:
    name = "Rohan"
    age = 20
obj1 = Details()
print(obj1.name)
print(obj1.age)

#Output 
Rohan
20

#Self Parameter
class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()

#Output 
My name is Rohan and I'm 20 years old.
