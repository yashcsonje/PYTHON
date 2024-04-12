#Day 66
class Employee:
    # Class variables
    companyname="Apple" # Class variable to store the company name
    NoOfEmployees=0 # Class variable to keep track of the number of employees

    # Constructor
    def __init__(self,name):
        self.name=name # Instance variable to store the employee's name
        self.raise_amount=0.02 # Instance variable to store the raise amount
        Employee.NoOfEmployees +=1 # Increment the number of employees when a new instance is created

    # Method to display employee details
    def showdetails(self):
        print(f"""The name of the Employee is{self.name} and the raise amount is {self.NoOfEmployees} sized {self.companyname} is {self.raise_amount}.""")

# Creating an instance of Employee
emp1=Employee("Harry")
emp1.raise_amount=0.3  # Modifying the raise amount for emp1
emp1.companyname="Apple India" # Modifying the company name for emp1
emp1.showdetails() # Displaying details of emp1

# Modifying the class variable companyname
Employee.companyname="Google"
print(Employee.companyname)

# Creating another instance of Employee
emp2=Employee("Rohan")
emp2.companyname="Nestle"
emp2.showdetails()