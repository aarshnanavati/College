#Accept a number from the user and reverse it using a while loop (without converting it into a string).

num = int(input("Enter the number : "))
rev = 0

while num > 0 :
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number : ",rev)