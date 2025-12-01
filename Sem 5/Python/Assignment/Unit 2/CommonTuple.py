#Write a program to find common elements between two tuples without converting them to lists or sets.

t1 = ()
t2 = ()
n = int(input("Enter the number of tuples you want to add: "))

for i in range(n):
    num = int(input("Enter the number : "))
    t1 += (num,)

for i in range(n):
    num = int(input("Enter the number :"))
    t2 += (num,)

common = []

for item1 in t1:
    for item2 in t2:
        if item1 == item2:
            common += (item1,)

print("Common elements : ",common)