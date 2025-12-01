#Write a Python program that calculates the factorial of a number using a while loop.

num = int(input("Enter a number : "))

i = 1
factorial = 1
while i <= num:
    factorial *= i
    i += 1
    print(factorial)