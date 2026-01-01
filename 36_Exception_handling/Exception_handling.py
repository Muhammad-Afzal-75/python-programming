# Exception handling in Python

#basic try-except block

# try:
#     number = int(input("Enter a number: "))
#     print(10/number)
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")


# try-except-else-finally

# try:
#     f = open("36_Exception_handling/data.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found. Please check the file path.")
# else:
#     print("File read successfully.")
# finally:
   
#     print("File closed.")



# creeate a custom error

# age = 10
# if age<18:
#     raise Exception("Age is less than 18. Access denied.")

# try / except /  else


try:
    num = int(input("Enter a number: "))
except:
    print("This is not a valid number.")
else:
    print(f"You entered: {num}")


