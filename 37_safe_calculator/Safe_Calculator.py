"""
A Calculator that:
Never Crash
Logs Errors
Uses Try/Except
Uses File Handling
"""

# Logging Function
def log_error(message):
    with open("error_log.txt", "a") as f:
        f.write(message + "\n")


# Safe Calculator Function
def safe_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2

        elif operator == '-':
            result = num1 - num2

        elif operator == '*':
            result = num1 * num2

        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2

        else:
            raise ValueError("Invalid operator used.")

        print(f"The result is: {result}")

    except Exception as e:
        print("An error occurred. Please try again.")
        print("Error:", e)
        log_error(str(e))

    finally:
        print("Calculation completed.")


# Run Calculator in Loop
while True:
    print("\nWelcome to the Safe Calculator!")
    safe_calculator()

    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the Safe Calculator. Goodbye!")
        break
