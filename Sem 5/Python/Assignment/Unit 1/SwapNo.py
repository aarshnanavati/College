#Write a Python program to swap of two numbers.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Before swapping : a =",a, "b = ",b)

temp = a
a = b
b = temp

print("Agter swapping : a = ",a,"b= ",b)
