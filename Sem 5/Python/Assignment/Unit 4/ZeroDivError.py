# Write a program to divide one number from another number with exception handling and show ZeroDivisionError

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2 :"))

    result = num1 / num2
    print("Result: ",result)

except ZeroDivisionError:
    print("Error : Division of zero is not allowed!")

finally:
    print("This block always executes")