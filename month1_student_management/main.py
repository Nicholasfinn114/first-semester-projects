
from student_data import add_student, view_students, get_average_grade, students

def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average Grade")
    print("4. Exit")
    print("---------------------------------")

def main():
 

    print("Simulating student management interactions...")

   
    print(add_student("Alice", 20, 85.5))
    print(add_student("Bob", 22, 90.0))
    print(add_student("Charlie", 21, 78.0))
    print(add_student("Diana", 19, 92.5))
    print(add_student("Eve", 20, "invalid_grade")) 

    # View students
    print(view_students())

    # Calculate average grade
    avg_grade = get_average_grade()
    print(f"\nAverage grade of all students: {avg_grade:.2f}")

 
     while True:
         display_menu()
         choice = input("Enter your choice: ")
         if choice == '1':
             name = input("Enter student name: ")
             age = input("Enter student age: ")
             grade = input("Enter student grade: ")
             print(add_student(name, age, grade))
         elif choice == '2':
             print(view_students())
         elif choice == '3':
             avg = get_average_grade()
             print(f"Average grade: {avg:.2f}")
         elif choice == '4':
             print("Exiting Student Management System. Goodbye!")
             break
        else:
           print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
