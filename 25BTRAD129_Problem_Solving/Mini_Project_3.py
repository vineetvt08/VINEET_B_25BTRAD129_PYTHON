students = {
    "Arun": ["P", "P", "A", "P", "P"],
    "Meena": ["P", "A", "P", "P", "A"],
    "Rahul": ["P", "P", "P", "P", "P"]
}

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
    elif name in students:
        print("Student already exists.")
    else:
        students[name] = []
        print("Student added successfully.")

def update_attendance():
    name = input("Enter student name: ").strip()
    if name not in students:
        print("Student not found.")
        return
    status = input("Enter attendance (P/A): ").strip().upper()
    if status in ("P", "A"):
        students[name].append(status)
        print("Attendance updated successfully.")
    else:
        print("Invalid status. Enter P or A.")

def display_attendance():
    print("\nATTENDANCE RECORD")
    print("-" * 55)
    print(f'{"Name":<15}{"Present":<10}{"Total":<10}{"Percentage":<12}')
    print("-" * 55)
    for name, records in students.items():
        total = len(records)
        present = records.count("P")
        percentage = (present / total * 100) if total > 0 else 0
        print(f"{name:<15}{present:<10}{total:<10}{percentage:.2f}%")

def check_low_attendance():
    threshold = float(input("Enter attendance threshold (%): "))
    print("\nStudents below the threshold:")
    found = False
    for name, records in students.items():
        total = len(records)
        present = records.count("P")
        percentage = (present / total * 100) if total > 0 else 0
        if percentage < threshold:
            print(f"{name}: {percentage:.2f}%")
            found = True
    if not found:
        print("No students are below the threshold.")

while True:
    print("\nATTENDANCE TRACKER")
    print("1. Add student")
    print("2. Update attendance")
    print("3. Display attendance")
    print("4. Check low attendance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        update_attendance()
    elif choice == "3":
        display_attendance()
    elif choice == "4":
        check_low_attendance()
    elif choice == "5":
        print("Attendance tracker closed.")
        break
    else:
        print("Invalid choice. Try again.")
