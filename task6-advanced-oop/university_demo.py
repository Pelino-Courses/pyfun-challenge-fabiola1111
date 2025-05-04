from student import Student
from instructor import Instructor
from teaching_assistant import TeachingAssistant
from course import Course
from enrollment import Enrollment

def main():
    # Create people
    alice = Student("Alice", 20)
    bob = Student("Bob", 21)
    prof = Instructor("Dr. Green", 50, "Biology")
    ta = TeachingAssistant("Tom", 25, "Math")

    # Create courses
    bio = Course.create_lecture_course("Biology 101")
    lab = Course.create_lab_course("Chemistry Lab")

    # Enroll students
    Enrollment(alice, bio)
    Enrollment(bob, lab)
    Enrollment(ta, bio)

    print(alice)
    for course in alice:
        print(f" -> Enrolled in: {course}")

    print("\nStudents in Biology 101:")
    for student in bio:
        print(f" - {student.name}")

    print("\nCombined courses of Alice and Bob:")
    for course in alice + bob:
        print(f" * {course.title}")

if __name__ == "__main__":
    main()