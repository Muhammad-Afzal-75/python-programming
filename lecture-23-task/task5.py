#password validator


password = input("Enter Password")

if(len(password)> 8 and
   any(ch.isdigit() for ch in password) and
   any(ch.isupper() for ch in password) and
   any(ch.islower() for ch in password)
   ):
    print("strong password")
else:
    print("weak password")