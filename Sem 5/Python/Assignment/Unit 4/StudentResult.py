# Create a StudentResult class that calculates grade percentages.
# Handle exceptions if marks entered exceed subject maximums or are negative.

class InvalidMarksError(Exception):
    """Custom exception for invalid marks (negative or beyond limit)."""
    pass


class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.max_marks = 100

    def calculate_result(self):
        try:
            total = 0
            for subject, mark in self.marks.items():
                if mark < 0:
                    raise InvalidMarksError(f"Marks for {subject} cannot be negative")
                elif mark > self.max_marks:
                    raise InvalidMarksError(f"Marks for {subject} cannot exceed {self.max_marks}")
                total += mark

            percentage = (total / (len(self.marks) * self.max_marks)) * 100
            print("\nStudent Name:", self.name)
            print("Total Marks:", total)
            print("Percentage:", round(percentage, 2))

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 40:
                grade = "C"
            else:
                grade = "Fail"

            print("Grade:", grade)

        except InvalidMarksError as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            print("------ End of Result Calculation ------")


try:
    name = input("Enter Student Name: ")
    subjects = ["Math", "Science", "English"]
    marks = {}

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks[subject] = mark

    student = StudentResult(name, marks)
    student.calculate_result()

except ValueError:
    print("Invalid input! Please enter numeric values only.")
