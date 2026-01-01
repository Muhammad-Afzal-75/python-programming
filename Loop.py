# Loops are used to execute a block of code repeatedly until a certain condition is met.
# In Python, there are two main types of loops: for loops and while loops.
# Here are examples of both types of loops:

# Example of a for loop
for i in range(5):
    print("For Loop iteration:", i)

    for j in range(1, 4):
        print("  Nested For Loop iteration:", j)

        #loop through a list
        sample_list = ['a', 'b', 'c']
        for item in sample_list:
            print("    Item from list:", item)
            #nested loop
            for k in range(1, 6):
                for m in range(k):
                 print("*", end="")
                print()  # New line after each row of stars

# Multiplication table using nested for loops
 
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")        

# Example of a while loop
# This loop will run as long as the condition is true

count = 0
while count < 5:
    print("While Loop iteration:", count)
    count += 1  # Increment the counter to avoid infinite loop

# break / continue / pass statements in loops

for i in range(10):
    if i == 3:
        print("Skipping number 3")
        continue  # Skip the rest of the loop when i is 3
    if i == 7:
        print("Breaking the loop at number 7")
        break  # Exit the loop when i is 7
    print("Current number:", i)            
