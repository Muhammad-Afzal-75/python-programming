

num = int(input("Enter your num: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(f"{num}! = {fact}")
