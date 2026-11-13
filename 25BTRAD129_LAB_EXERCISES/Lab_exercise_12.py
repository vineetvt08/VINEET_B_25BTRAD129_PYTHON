import json
import os

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("The student data file is empty or cannot be read.")
        return []

def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()
    student_id = input("Enter student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if any(s["id"] == student_id for s in students):
        print("A student with this ID already exists.")
        return
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    if not name or not course:
        print("Name and course cannot be empty.")
        return

    students.append({"id": student_id, "name": name, "course": course})
    save_students(students)
    print("Student record added successfully.")

def display_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    print("\nID\tName\t\tCourse")
    print("--------------------------------")
    for s in students:
        print(f'{s["id"]}\t{s["name"]}\t\t{s["course"]}')

def search_student():
    students = load_students()
    student_id = input("Enter student ID to search: ").strip()
    for s in students:
        if s["id"] == student_id:
            print("Record found:", s)
            return
    print("Student record not found.")

def update_student():
    students = load_students()
    student_id = input("Enter student ID to update: ").strip()
    for s in students:
        if s["id"] == student_id:
            new_name = input("Enter new name: ").strip()
            new_course = input("Enter new course: ").strip()
            if new_name:
                s["name"] = new_name
            if new_course:
                s["course"] = new_course
            save_students(students)
            print("Student record updated.")
            return

    print("Student record not found.")

while True:
    print("\nSTUDENT DATA MANAGER")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice. Please try again.")
