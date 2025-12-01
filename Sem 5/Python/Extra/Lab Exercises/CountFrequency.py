#Accept 10 numbers. Create a second list with even numbers only.
#Count frequency of each even number using `count()` method.

number = []
for i in range(10):
    n = int(input("Enter number :"))
    number.append(n)

even_numbers = []
for n in number:
    if n % 2 == 0:
        even_numbers.append(n)

print("Even numbers",even_numbers)

print("Frequencies : ")
seen = []
for n in even_numbers:
    if n not in seen:
       print(n, "→", even_numbers.count(n))
       seen.append(n)
