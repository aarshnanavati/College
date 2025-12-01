# Write a Python function to calculate the factorial of a number. Call the function formultiple test cases.
##WRWA

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

t = int(input("Enter the number of cases:"))

for i in range(t):
    num = int(input("Enter a number : "))
    print("Factorial of",num,"is : ",factorial(num))
