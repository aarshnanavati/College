# Write a function to check whether a given number is prime or not.

def is_prine(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number : "))

if is_prine(num):
    print(num,"is prime number!")
else:
    print(num,"no is not prime!")