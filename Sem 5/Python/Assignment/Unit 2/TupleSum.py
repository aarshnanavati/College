#Accept a tuple of integers and count how many elements are divisible by 3 but not by 5.
#  Also, calculate their sum.

tupleNum = []

n = int(input("Enter the number to add in tuple : "))

for i in range(n):
    num = int(input("Enter the number : "))
    tupleNum.append(num)
tupleNum = tuple(tupleNum)
count = 0
total = 0

for num in tupleNum:
    if num % 3 == 0 and num % 5 != 0:
        count += 1
        total += num

print("count of number is divisible by 3 but not by 5",count)
print("Sum of those numbers : ",total)
