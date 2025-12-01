# Write a program to raise an exception if number is negative

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative Numbers are not allowed!")
    print("You entered positive number ",num)

except ValueError as e:
    print(e)