#Write a Python program to accept marks for 5 subjects, calculate average, and assign grade (A/B/C/D/Fail).
#If any subject has marks <35, display “Fail due to subject back”.

marks = []
for i in range(5):
    score = int(input("Enter marks for subject {i} : "))
    marks.append(score)

if any(mark < 5 for mark in marks):
    print("Fail due to subject back")
else:
    avg = sum(marks) / 5    
    print("Average marks : ",avg)

    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 60:
        grade = 'C'
    elif avg >= 35:
        grade = 'D'
    else:
        grade = 'Fail'
    print("Grade : ", grade)