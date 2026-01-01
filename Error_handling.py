# grraceful failure: prevent program crash with error handling

try:
    num: int = int(input("Enter an integer: "))
    print(100/num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

else:
    print("Operation completed successfully.")
finally:
    print("Thank you for using the program.")
