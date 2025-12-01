#Given a list of integers, write a Python program to remove all duplicates without using set(), and preserve the original order.

numbers = []
n = int(input("How many numbers do you want to add? "))

for i in range(n):
    num = int(input("Enter a number : "))
    numbers.append(num)
unique_numbers = []

for num in numbers : 
    if num not in unique_numbers:
        unique_numbers.append(num)
print("List after removing duplicates:", unique_numbers)