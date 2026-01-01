

# import math
# print(math.sqrt(25))
# print(math.pi)
# print(math.factorial(5))


#date and time module


# import datetime

# now = datetime.datetime.now()
# print("current Time: ", now)

# print("years: ", now.year)
# print("month: ", now.month)
# print("day: ", now.day)


#random module

# import random

# print(random.randint(1, 10))
# print(random.choice(['apple', 'banana', 'cherry']))
# print(random.random())  # random float between 0.0 to 1.0


# import Mymodule

# print(Mymodule.add(5, 10))
# print(Mymodule.greet("Alice"))

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())





