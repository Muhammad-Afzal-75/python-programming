
# def intro(name="Afzal"):
#     return f"Hello, {name}!"

# print(intro())

def calculate_charity(income):
    if income > 85000:
        return income * 0.025
    else:
        return 0.0   # income kam ho to charity 0

amount = calculate_charity(90000)
print(f"charity: PKR {amount:.2f}")



