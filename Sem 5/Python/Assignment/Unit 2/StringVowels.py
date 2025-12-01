#Write a program to input a tuple of strings and find how many strings contain only vowels.

n = int(input("Enter the number of strings : "))
t = ()

for i in range(n):
    s = input("Enter the string :")
    t += (s,)

vowels = "aeiouAEIOU"
count = 0

for word in t:
    if all(ch in vowels for ch in word) and word != "":
        count += 1
print("Number of strings only vowels :",count)