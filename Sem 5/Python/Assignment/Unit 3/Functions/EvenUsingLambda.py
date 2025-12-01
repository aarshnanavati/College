# 2.Write a Python program using lambda to filter all even numbers from a given list.

numbers = []
n = int(input("Enter the number for list : "))

for i in range(n):
    num = int(input("Enter the numbers : "))
    numbers.append(num)

even_numbers = list(filter(lambda x : x % 2 == 0 , numbers))

print("Original List : ",numbers)
print("Even numbers : ",even_numbers)