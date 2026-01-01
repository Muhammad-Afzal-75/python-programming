students = {}

while True:
    name = input("Enter your name(or 'exit' )")

    if name.lower() == "exit":
        break
    marks = int(input(f"enter marks {name}: "))
    students[name] = marks 

    print("\n=== Student Marks===")

    for name, mark in students.items():
        print(f"{name}:{marks}")

