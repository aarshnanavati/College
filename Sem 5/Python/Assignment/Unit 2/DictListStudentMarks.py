#Create a dictionary of student names and a list of their marks in 3 subjects. Calculate 
#and store the average for each student. Display the dictionary with names and averages.

students = {}
n = int(input("Enter number of students : "))

for i in range(n):
    name = input("Enter name of students : ")
    marks = []
    for j in range(3):
        mark = float(input("Enter marks for student"))
        marks.append(mark)

    average = sum(marks)/3
    students[name] = average

for name,average in students.items():
    print("Name : ",name)
    print("Average : ",average)