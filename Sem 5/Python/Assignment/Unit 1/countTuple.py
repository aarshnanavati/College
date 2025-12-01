#Write a Python program that counts how many times a value appears in a tuple.

myTuple = ()
num = int(input("Enter the number of elements in the tuple: "))

for i in range(num):
    element = int(input("Enter elements : "))
    myTuple += (element,)

value = int(input("Enter the value to count: "))
count = myTuple.count(value)
print(count)