
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 70:
            return "C"
        elif self.__marks >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nRoll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.__marks)
        print("Grade:", self.calculate_grade())


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Invalid marks!")
            return

        student = Student(roll, name, marks)
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No student records found.")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        roll = input("Enter Roll Number to search: ")

        for student in self.students:
            if student.roll_no == roll:
                print("Student Found!")
                student.display()
                return

        print("Student not found.")


def main():
    system = StudentManagement()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.display_students()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
