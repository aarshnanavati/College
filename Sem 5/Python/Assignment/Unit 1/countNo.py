#Write a python program to Count the total number of digits in a number.

num = int(input("Enter a number : "))
count = 0
num = abs(num)

while num > 0:
    count += 1
    num = num // 10

print("Total number of digits : ",count)

