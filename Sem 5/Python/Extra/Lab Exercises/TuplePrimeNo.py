#Accept a tuple of 10 integers.Count even and odd numbers. Extract prime numbers into
#a new tuple.Display max, min, and sum of the new tuple.

nums_list = []
n = int(input("Enter the number for tuple :"))
for i in range(n):
    num = int(input("Enter the number : "))
    nums_list.append(num)

nums = tuple(nums_list)
print("Tuple Entered : ",nums)

even_count = 0
odd_count = 0

for n in nums:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Number : ",even_count)
print("Odd Number : ",odd_count)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2 , int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_list = []
for n in nums:
    if is_prime(n):
        prime_list.append(n)

prime_tuple = tuple(prime_list)
print("Prime Tuple : ",prime_tuple)

if len(prime_tuple) > 0:
    print("Max : ",max(prime_tuple))
    print("Min : ",min(prime_tuple))
    print("Sum : ",sum(prime_tuple))
else:
    print("No prime numbers found!")