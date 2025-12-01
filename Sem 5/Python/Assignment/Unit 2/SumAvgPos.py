#Continuously accept integers until a negative number is entered.
#  Calculate sum, average, and count of positive numbers entered.

total = 0
count = 0

n = int(input("Enter the number : "))

for i in range(n):
    num = int(input("Enter the number : "))
    if n < 0:
        print("Negative numbers entered ")
        break
    else:
        total += num
        count += 1

if count > 0:
    average = total / count
    print("Sum : ",total)
    print("Average : ",(count/2))
    print("count",count)
else:
    print("The positive numbers entered!")