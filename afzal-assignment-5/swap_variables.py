#swap_variables tow
# Get user input for two variables

a = input("Enter the value for variable a: ")
b = input("Enter the value for variable b: ")

print(f"Before swapping: a = {a}, b = {b}")

# Swap the values of the two variables
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")



