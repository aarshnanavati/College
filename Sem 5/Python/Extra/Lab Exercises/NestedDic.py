#Create a nested dictionary that stores student names as keys, and their subjects
#and marks as sub-dictionaries. Add, update and delete subjects or marks.

students = {}
n = int(input("Enter the number for dictionary : "))

for i in range(n):
    key = input("Enter the key : ")
    value = input("Enter the value : ")
    students[key]=value

while True:
    print("\n--- Student Record Menu ---")
    print("1. Add/Update Subject & Marks")
    print("2. Delete Subject")
    print("3. View Records")
    print("4. Exit")

    choice = input("Enter your choice :")

    if choice == "1":
        name = input("Enter subject name : ")
        subject  = input("Enter subject name : ")
        marks = int(input("Enter marks: "))

        if name not in students:
            students[name] = {}

        students[name][subject] = marks
        print(f"{subject} updated for {name}")

    elif choice == "2":
        name = input("Enter student name :")
        if name in students:
            subject = input("Enter subject name to delete : ")
            if subject in students[name]:
                del students[name][subject]
                print(f"{subject} deleted for {name}")
            else:
                print("Subject not founc!")
        else:
            print("Student not found")

    elif choice == "3":
        for student, subject in students.items():
            print(f"\n{student}:")
            for subj, mark in subject.items():
                print(f"  {subj} → {mark}")

    elif choice == "4":
        print("Exiting...")
        break
    
    else:
        print("❌ Invalid choice, try again.")
            