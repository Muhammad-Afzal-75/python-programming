#conditionals (if, elif, else) and loops (for, while) in Python


# Example of conditional statements
# age = 8
# if age >= 18:
#     print("You are an adult.")
# elif age > 12:
#     print("You are a teenager.")    
# else:
#     print("You are a child.")

    #Nested conditionals

    # UserName = "admin"
    # Password = "1234"

    # if UserName == "admin":
    #     if Password == "1234":
    #         print("Login Successfull.")
    #     else:
    #         print("Incorrect password.")
    # else:
    #     print("Unknown user.")  

        #login system
print("== Welcome to the Login page ==")

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

if input_username == "Afzal":
    if input_password == "123456":
        print("Login Successful.")
    else:
        print("Incorrect password.")
else:
    print("Unknown user.")


