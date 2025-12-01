#Continuously accept numbers until user enters 0.Store in a list. 
#Print max, min, sum, and count of even numbers.

numbers = []

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break
    numbers.append(num)

if numbers:
    even_count = sum(1 for n in numbers if n % 2 == 0)
    print("Maximum numbers : ",max(numbers))
    print("Minimum number : ",min(numbers))
    print("Sum of the numbers : ",sum(numbers))
    print("Count of even numbers : ",even_count)
else:
    print("No numbers entered!")