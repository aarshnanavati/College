# Write a program that uses a lambda function and *args together to multiply all given numbers by 2.

def multiplyBy2(*args):
    return list(map(lambda x : x * 2 , args))

numbers = []
n = int(input("Enter the numbers for the list : "))

for i in range(n):
    num = int(input("Enter the numbers: "))
    numbers.append(num)

print("Doubled numbers : ",multiplyBy2(*numbers))