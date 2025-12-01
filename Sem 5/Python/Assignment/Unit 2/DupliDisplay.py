#Write a program to input a list of 10 names and check if there are any duplicate entries. If yes, display the duplicates.

names = []

for i in range(6):
    name = input("Enter a name:")
    names.append(name)

duplicates = []
for name in names : 
    if names.count(name) > 1 and name not in duplicates:
        duplicates.append(name)

if duplicates:
    print("Duplicate names are : ")
    print(duplicates)
else:
    print("No duplicate names are found!")