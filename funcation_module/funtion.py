# def intro():
#     print("salam!")

# intro()

# def add(a, b):
#     print(a+b)

# add(5,8)

# def multiply(c, d):
#     return c*d
# result = multiply(5,7)
# print(result)


#default / keyword arguments

# def person(name = "guest"):
#     print(f"Salam!, {name}")
# person()
# person("afzal")


# def total(*numbers):
#     print(numbers)
#     print(sum(numbers))
# total(3,69, 50)    



# **kwargs mul keyword arg

# def person_detail(**details):
#     for key, value in details.items():
#      print(f"{key}:{value}")
# person_detail(name="ali", age=24, city="lodhran")     

#lambda expression


# lambda argument: expression


# add = lambda a, b: a+b
# print(add(5,15))

#sorting 

# studs = [("ali", 24), ("sara", 30), ("akbar", 25) ]

# studs.sort(key=lambda x: x[1])
# print(studs)

# recursion

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial (n-1)
# print(factorial(5))


#local or global variable

# def func():
#     x = 10
#     print(x)  
# func()      



#global
# x = 100
# def show():
#     print(x)
# show() 


#modify global varible inside function

count = 0 

def increment():

    global count
    count += 2
increment()
print(count)    







