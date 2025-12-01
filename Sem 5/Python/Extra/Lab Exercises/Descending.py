#Accept 10 integers. Remove duplicates, sort in descending order, 
#print the second highest and second lowest unique value, and average of top 5 values.

nums = []
for i in range(10):
    n = int(input("Enter the number : "))
    nums.append(n)

unique_nums = sorted(set(nums),reverse=True)

if len(unique_nums) >= 2:
    second_highest = unique_nums[1]
    second_lowest = unique_nums[-2]
else:
    second_highest = second_lowest = True

top_5 = unique_nums[:5]
avg_top = sum(top_5) / len(top_5)

print("Second Highest : ",second_highest)
print("Second Lowest : ",second_lowest)
print("Average of top 5 : ",avg_top)