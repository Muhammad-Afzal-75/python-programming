#prime num checker


num = int(input("enter your num: "))
if num <= 1:
    print(f"prime nahe h")
else:
    is_prime = True

    for i in range(2, num):
       if num % i == 0:
        is_prime = False
        break

    if is_prime:
       print(f"{num} prime num h")
    else:
       
       print(f"{num} prime num nahe h")


    




