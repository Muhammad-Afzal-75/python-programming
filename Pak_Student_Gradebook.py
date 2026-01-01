def add_student(records):
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    if roll_number in records:
        print("A student with this roll number already exists.\n")
        return

    marks = []
    subjects = ['Math', 'Science', 'English']

    for subject in subjects:
        while True:
            try:
                m = int(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer for marks.")

    records[roll_number] = {"name": name, "marks": marks}
    print("Student added successfully.\n")


def view_gradebook(records):
    if not records:
        print("No student records found.\n")
        return

    print("\n----- Gradebook -----")
    for roll_number, data in records.items():
        avg = sum(data["marks"]) / len(data["marks"])
        grade = (
            'A' if avg >= 90 else
            'B' if avg >= 80 else
            'C' if avg >= 70 else
            'D' if avg >= 60 else
            'F'
        )
        print(f"Roll Number: {roll_number}, Name: {data['name']}, Average: {avg:.2f}, Grade: {grade}")
    print()


def main():
    records = {}
    print("Welcome to the Student Gradebook System\n")

    while True:
        print("1. Add Student")
        print("2. View Gradebook")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student(records)
        elif choice == '2':
            view_gradebook(records)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
