class StudentGradingSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):
        """Add or update a student's marks in the dictionary."""
        if not (0 <= marks <= 100):
            print(f"\n[Error] Marks for '{name}' must be between 0 and 100.")
            return False

        self.students[name] = marks
        print(f"\n[Success] Recorded marks for '{name}': {marks}")
        return True

    def calculate_grade(self, marks):
        """Determine letter grade using conditional statements."""
        if marks >= 90:
            return 'A', 'Excellent'
        elif marks >= 80:
            return 'B', 'Good'
        elif marks >= 70:
            return 'C', 'Satisfactory'
        elif marks >= 60:
            return 'D', 'Needs Improvement'
        else:
            return 'F', 'Failing'

    def display_results(self):
        """Display all students, their marks, calculated grades, and status."""
        if not self.students:
            print("\n[Info] No student records found.")
            return

        print("\n" + "=" * 65)
        print(f"{'STUDENT NAME':<20} | {'MARKS':<6} | {'GRADE':<6} | {'STATUS':<20}")
        print("=" * 65)

        total_marks = 0
        for name, marks in self.students.items():
            grade, status = self.calculate_grade(marks)
            total_marks += marks
            print(f"{name:<20} | {marks:<6} | {grade:<6} | {status:<20}")

        print("=" * 65)
        average_marks = total_marks / len(self.students)
        print(f"Class Average Marks: {average_marks:.2f}\n")

def main():
    system = StudentGradingSystem()
    while True:
        print("\n--- STUDENT GRADING SYSTEM MENU ---")
        print("1. Add / Update Student Marks")
        print("2. View All Results & Class Average")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            name = input("Enter Student Name: ").strip()
            try:
                marks = float(input("Enter Marks (0-100): "))
                system.add_student(name, marks)
            except ValueError:
                print("\n[Error] Please enter a valid numerical value for marks.")

        elif choice == '2':
            system.display_results()

        elif choice == '3':
            print("\nExiting Student Grading System. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
