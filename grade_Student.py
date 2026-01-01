
print("=== Grade Student System ===")

subjects = ['Math', 'Science', 'English']
total= 0

for subject in subjects:
    marks = float(input(f"enter your grade for {subject}: "))
    total += marks

average = total / len(subjects)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Your average marks is : {average}")
print(f"Your grade is : {grade}")

