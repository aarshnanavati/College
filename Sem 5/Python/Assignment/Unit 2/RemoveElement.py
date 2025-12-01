#Create a list of 10 random numbers and remove all elements greater than the average of the list. Display final list.

nums = []

for i in range(10):
    num = int(input("Enter the number :  "))
    nums.append(num)

print("Original list : ",nums)

avg = sum(nums) / len(nums)
print("Average : ",avg)

final_list = []
for num in nums:
    if num <= avg:
        final_list.append(num)
print("Final List : ",final_list)