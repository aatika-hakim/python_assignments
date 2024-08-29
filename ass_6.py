from typing import Dict, Union, Optional

# Define a type alias for student data
StudentData = Dict[str, Union[str, Optional[int]]]
StudentsDict = Dict[int, StudentData]

def display_students(students: StudentsDict) -> None:
    """ Display all students in the database """
    if students:
        print("\n--- Student Database ---")
        for student_id, data in students.items():
            age = data['age'] if data['age'] is not None else "N/A"
            print(f"ID: {student_id}, Name: {data['name']}, Age: {age}, Grade: {data['grade']}")
    else:
        print("The database is empty.")

def add_student(students: StudentsDict) -> None:
    """ Add a new student to the database """
    while True:
        student_id = len(students) + 1
        name = input("Enter the student's name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        if any(student['name'].lower() == name.lower() for student in students.values()):
            print("This name is already in the database.")
            continue
        age_str = input("Enter the student's age: ").strip()
        grade = input("Enter the student's grade: ").strip()

        # Ensure age is an integer if provided
        age: Optional[int] = None
        if age_str:
            try:
                age = int(age_str)
            except ValueError:
                print("Invalid age. Age must be an integer.")
                continue

        students[student_id] = {'name': name, 'age': age, 'grade': grade}
        print(f"Added student {name} with ID {student_id}.")
        break

def update_student(students: StudentsDict) -> None:
    """ Update an existing student's details """
    student_id_str = input("Enter the ID of the student to update: ").strip()
    try:
        student_id = int(student_id_str)
    except ValueError:
        print("Invalid ID. ID must be an integer.")
        return

    if student_id in students:
        print(f"Updating details for student ID {student_id} ({students[student_id]['name']})")
        name = input("Enter the new name (leave blank to keep current): ").strip()
        if name:
            students[student_id]['name'] = name
        age_str = input("Enter the new age (leave blank to keep current): ").strip()
        if age_str:
            try:
                students[student_id]['age'] = int(age_str)
            except ValueError:
                print("Invalid age. Age must be an integer.")
                return
        grade = input("Enter the new grade (leave blank to keep current): ").strip()
        if grade:
            students[student_id]['grade'] = grade
        print(f"Updated student ID {student_id}.")
    else:
        print("Student ID not found.")

def delete_student(students: StudentsDict) -> None:
    """ Delete a student from the database """
    student_id_str = input("Enter the ID of the student to delete: ").strip()
    try:
        student_id = int(student_id_str)
    except ValueError:
        print("Invalid ID. ID must be an integer.")
        return

    if student_id in students:
        del students[student_id]
        print(f"Deleted student ID {student_id}.")
    else:
        print("Student ID not found.")

def manage_student_db() -> None:
    """ Main function to manage student database with CRUD operations """
    students: StudentsDict = {}
    
    print("Welcome to the Student Database Manager!")
    print("You can perform CRUD operations on the student database.")
    
    while True:
        print("\nOptions:")
        print("1. Add a new student")
        print("2. Update an existing student")
        print("3. Delete a student")
        print("4. Display all students")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            display_students(students)
        elif choice == '5':
            print("Exiting the Student Database Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Call the function to start the program
manage_student_db()
