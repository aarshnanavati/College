#Given a list of integers, print the square of even numbers and 
#cube of odd numbers using `enumerate()` and list comprehension.

nums = list(map(int,input("Enter numbers : ").split()))
result = [n ** 2 if n % 2 == 0 else n ** 3 for i , n in enumerate(nums)]
print("Result : ",result)