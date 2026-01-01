import random

def save_history(text):
    with open("final_project/history.txt", "a") as file:
        file.write(text + "\n")

def random_number():
    try:
        num = random.randint(1, 100)
        print("Random Number:", num)
        save_history(f"Random Number Generated: {num}")
    except Exception as e:
        print("Error:", e)

def dice_roll():
    try:
        num = random.randint(1, 6)
        print("Dice rolled:", num)
        save_history(f"Dice Rolled: {num}")
    except Exception as e:
        print("Error:", e)

def coin_toss():
    try:
        result = random.choice(["Head", "Tail"])
        print("Coin Toss Result:", result)
        save_history(f"Coin Toss: {result}")
    except Exception as e:
        print("Error:", e)

def password_generator():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        password = ""

        for i in range(length):
            password += random.choice(chars)

        print("Generated Password:", password)
        save_history(f"Password Generated (length {length}): {password}")

    except ValueError:
        print("Please enter a valid positive number!")

while True:
    try:
        print("\n=== Random Utilities Tool ===")
        print("1. Random Number Generator")
        print("2. Dice Roller")
        print("3. Coin Toss")
        print("4. Password Generator")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            random_number()
        elif choice == '2':
            dice_roll()
        elif choice == '3':
            coin_toss()
        elif choice == '4':
            password_generator()
        elif choice == '5':
            print("Thank you for using Random Utilities Tool!")
            break
        else:
            print("Invalid choice! Try again.")

    except Exception as e:
        print("Unexpected error:", e)
