#Day 86
'''
The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression.
This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.
'''
# Initialize an empty list to store the foods entered by the user
foods = list()

# Traditional approach without using the walrus operator
while True:
    # Prompt the user to input a food they like
    food = input("What food do you like?: ")
    
    # Check if the user wants to quit entering foods
    if food == "quit":
        break  # Exit the loop if the user inputs "quit"
    
    # Add the entered food to the list of foods
    foods.append(food)

# Print a message indicating that we're now using the walrus operator
print("\nNow using the walrus operator")

# Using the walrus operator to streamline the input process
foods = list()  # Reinitialize the list to store the foods
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)  # Append the entered food to the list

# At this point, the loop exits when the user inputs "quit"

'''
Output:
What food do you like?: Apple
What food do you like?: quit

Now using the walrus operator
What food do you like?: Banana
What food do you like?: quit
'''