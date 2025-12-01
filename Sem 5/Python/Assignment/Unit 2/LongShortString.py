#Write a Python program that accepts 5 strings and displays the longest and shortest strings.

strings = []

for i in range(5):
    s = input("Enter the string : ")
    strings.append(s)

longest = strings[0]
shortest = strings[0]

for s in strings:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s

print("Longest String : ",longest)
print("Shortest String : ",shortest)