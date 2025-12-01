#Given a list of integers, write a Python program to remove all duplicates without using set(), and preserve the original order.

number = []
num = int(input("Enter the numbers : "))
for i in range(num):
    element = int(input("Enter element : "))
    number.append(element)
unique = []
for num in number:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)