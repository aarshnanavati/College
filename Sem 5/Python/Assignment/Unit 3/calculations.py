# Write a program to create function calculation () such that it can accept two variables and
# calculate addition and subtraction. Also, it must return both addition and subtraction in a
# single return call.

def calculation(a,b):
    addition = a + b
    subtraction = a - b
    return addition,subtraction

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add_result,sub_result = calculation(num1,num2)

print("Addition : ",add_result)
print("Subtraction : ",sub_result)