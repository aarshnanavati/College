#Accept a tuple of integers. Without converting to list, find the 3rd highest and 2nd lowest values.

t = []
n = int(input("Enter the numbers you want to add in tuple : "))

for i in range(n):
    num = int(input("Enter the numbers: "))
    t.append(num)

sorted_t = sorted(t)
second_lowest = sorted_t[1]
third_highest = sorted_t[-3]

print("2nd Lowest : ",second_lowest)
print("3rd Highest : ",third_highest)