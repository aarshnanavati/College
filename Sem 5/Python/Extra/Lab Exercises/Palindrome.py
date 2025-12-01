#Accept a number and check whether it is a palindrome using logic (no string conversion allowed).

num = int(input("Enter a number :"))
original = num
reverse_num = 0

while num > 0:
    digot = num % 10
    reverse_num = reverse_num * 10 + digot
    num //= 10

if original == reverse_num:
    print("Palindrome number : ")
else:
    print("Not Palindrome")