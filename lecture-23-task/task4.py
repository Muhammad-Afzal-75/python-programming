# numner guessing logic
import random

number = random.randint(1, 50)  # 1 se 50 ka random number
guess = 0

while guess != number:
    guess = int(input("Guess karo number (1-50): "))
    
    if guess < number:
        print("Bada number try karo")
    elif guess > number:
        print("Chhota number try karo")
    else:
        print("Sahi guess! You win!")
