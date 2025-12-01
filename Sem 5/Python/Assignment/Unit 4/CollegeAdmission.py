# Develop a program to simulate a college admission system using classes Student, Course, and Admission.
# Allow students to apply for courses, validate their eligibility, and handle exceptions for invalid course 
# selections or missing prerequisites.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

class Course:
    def __init__(self,course_name,min_marks):
        self.course_name = course_name
        self.min_marks = min_marks

class Admission:
    def __init__(self):
        self.courses = {
            "BCA" : Course("BCA",55),
            "BBA" : Course("BBA",50),
            "BscIT" : Course("BscIT",60),
            "BA" : Course("BA",50)
        } 
    
    def apply_for_course(self,student,course_name):
        try:
            if course_name not in self.courses:
                raise ValueError("Invalid !")
            
            course = self.courses[course_name]

            if student.marks >= course.min_marks:
                print(f"Congragulations {student.name}! You are eligible for {course.course_name}")
            else:
                print(f"Sorry ! You are not eligible! you need atleast {course.min_marks} for {course.course_name}")

        except ValueError as e:
            print(f"Error!! {e}")

def main():
    name = input("Enter your name: ")
    try:
        marks = float(input("Enter your percentage marks: "))
        student = Student(name,marks)

        print("\nAvailable Courses: BCA, BBA, BSc, BA")
        course_name = input("Enter course you want to apply for: ").upper()

        admission = Admission()
        admission.apply_for_course(student,course_name)

    except:
        print("Invalid input")

if __name__ == "__main__":
    main()