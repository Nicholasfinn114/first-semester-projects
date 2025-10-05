

students = [] 

def add_student(name, age, grade):
    try:
        student_info = {"name": name, "age": int(age), "grade": float(grade)}
        students.append(student_info)
        return f"Student {name} added successfully!"
    except ValueError:
        return "Error: Age must be an integer and Grade must be a number."


def view_students():
   
    if not students:
        return "No students to display."

    student_list_str = "\n--- Student List ---\n"
    for i, student in enumerate(students):
        student_list_str += f"{i+1}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}\n"
    student_list_str += "--------------------"
    return student_list_str


def get_average_grade():
    """
    Calculates and returns the average grade of all students.
    """
    if not students:
        return 0.0 # No students, average is 0

    total_grades = sum(student['grade'] for student in students)
    average = total_grades / len(students)
    return average


