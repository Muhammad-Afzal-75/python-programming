#find the conversion of input to number


num = int(input("Enter a number: "))
print(num, type(num))

num = float(input("Enter a number: "))
print(num, type(num))


num = eval(input("Enter a number: "))
print(num, type(num))

# get number

num = int(input("Enter a number: "))
print(num)
print(f"The number you entered is {num} and its type is {type(num)}") 

# get float number
num = float(input("Enter a float number: "))
print(num)
print(f"The float number you entered is {num} and its type is {type(num)}")
# get complex number
num = complex(input("Enter a complex number: "))
print(num)
print(f"The complex number you entered is {num} and its type is {type(num)}")
# get eval number
num = eval(input("Enter a number (int, float, or complex): "))
print(num)
print(f"The number you entered is {num} and its type is {type(num)}")
