from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

def display_menu():
    """Display the main menu options"""
    return """
    === University Management System ===
    
    1. Add New Instructor
    2. Create New Course
    3. Register Student
    4. Enroll Student in Course
    5. Add Teaching Assistant
    6. Display All Enrollments
    7. Exit
    
    Please select an option (1-7): """

def university_demo():
    print("Welcome to the University Management System!")
    
    # Initialize storage
    enrollments = Enrollment()
    instructors = {}
    courses = {}
    students = {}
    teaching_assistants = {}

    while True:
        try:
            choice = input(display_menu())
            
            if choice == "1":
                instructor_name = input("Enter the instructor's name: ")
                course_name = input("Enter course to teach: ")
                
                # Create course first if it doesn't exist
                if course_name not in courses:
                    course = Course(course_name)  # Create course with name parameter
                    courses[course_name] = course
                    print(f"Created new course: {course_name}")
                
                # Create instructor and link to course
                instructor = Instructor(instructor_name, course_name)
                instructors[instructor_name] = instructor
                print(instructor.display_instructor_info())

            elif choice == "2":
                course_name = input("Enter the course name: ")
                course = Course(course_name)
                courses[course_name] = course
                print(f"Course '{course_name}' has been created.")

            elif choice == "3":
                student_name = input("Enter the student's name: ")
                course_name = input("Enter the course to register for: ")
                if course_name not in courses:
                    print("Error: Course does not exist!")
                    continue
                student = Student(student_name, course_name)
                students[student_name] = student
                student.register_students()
                print(student.display_student_info())

            elif choice == "4":
                student_name = input("Enter student name to enroll: ")
                course_name = input("Enter course name: ")
                instructor_name = input("Enter instructor name: ")
                if student_name not in students or course_name not in courses:
                    print("Error: Student or course not found!")
                    continue
                print(enrollments.enroll_student(student_name, course_name, instructor_name))

            elif choice == "5":
                ta_name = input("Enter the teaching assistant's name: ")
                course_name = input("Enter the course to assist: ")
                
                # Validate course exists
                if course_name not in courses:
                    print("Error: Course does not exist!")
                    continue
                
                # Create TA with required course parameter
                try:
                    ta = TeachingAssistant(ta_name, course_name, 50)  # Pass course_name as required by Instructor parent
                    teaching_assistants[ta_name] = ta
                    
                    # Get instructor information
                    instructor_name = input("Enter instructor name to assist: ")
                    if instructor_name in instructors:
                        print(ta.instructor_to_assist(instructor_name, course_name))
                        
                        # Add teaching performance grade
                        grade = float(input("Enter TA's teaching performance grade (0-100): "))
                        print(ta.student_to_teach(course_name, grade))
                        print(ta.display_info())
                    else:
                        print("Error: Instructor not found!")
                except ValueError as e:
                    print(f"Error: Invalid grade value - {e}")

            elif choice == "6":
                print("\nCurrent Enrollments:")
                print(enrollments.display_enrollments())

            elif choice == "7":
                print("Thank you for using the University Management System!")
                break

            else:
                print("Invalid option! Please select a number between 1 and 7.")

        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Add a pause between operations
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    university_demo()
