# . Write a Python program to create a module called calculator.py with add (), sub(), mul(), div()
# and call this module into another file named calc.py using from… import syn

from calculator import add,sub,mul,div

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition: ",add(num1,num2))
print("Subtraction : ",sub(num1,num2))
print("Multiplication : ",mul(num1,num2))
print("Division : ",div(num1,num2)) 
