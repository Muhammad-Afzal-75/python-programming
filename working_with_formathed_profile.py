

print("=== User profile system === ")

full_name = input("Enter your full name: ")
age = input("Enter your age: ")   
city = input("Enter your city: ")
profession = input("Enter your profession: ")   
hobby = input("Enter your hobby: ")
skills_raw = input("Enter your skills (comma-separated): ")

name = full_name.strip().title()
age = age.strip()
city = city.strip().title()
profession = profession.strip().title()
hobby = hobby.strip().title()
skills = [skill.strip().title() for skill in skills_raw.split(",")]

profile = f"""
       ~~~~~~~~~~~~~~~~~~~~~~~~
            User Profile:
        ~~~~~~~~~~~~~~~~~~~~~~~~
Name       : {name} 
Age        : {age}
City       : {city}
Profession : {profession}
Hobby      : {hobby}
Skills     : {', '.join(skills)}
""" 
print(profile)

