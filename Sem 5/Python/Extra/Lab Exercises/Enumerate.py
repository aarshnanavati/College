#Given a list of numbers, use `enumerate()` to print index and value. Use `all()` to check if 
#all elements are positive, and `any()` to check if any is a multiple of 7.

nums= []

n = int(input("Enter the number for list : "))
for i in range(n):
    num = int(input("Enter the number in list:"))
    nums.append(num)

print("Index and value : ")
for index,value in enumerate(nums):
    print(f"Index {index} : {value}")   

if all(x > 0 for x in nums):
    print("All values are Positive")
else:
    print("All values are not Positive")

if any(x % 7 == 0 for x in nums):

    print("✅ At least one element is a multiple of 7")

else:

    print("❌ No element is a multiple of 7")
