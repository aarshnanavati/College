#Accept a tuple of integers. Print elements whose square is > 50 using list comprehension.

numbers = []

n = int(input("Enter the number : "))

for i in range(n):
    num = int(input("Enter the numbers in tuple : "))
    numbers.append(num)

numbers = tuple(numbers)
result = [x for x in numbers if x**2 > 50]

if result:
    print("Elements whose square is >50 : ",result)
else:
    print("Not found!")