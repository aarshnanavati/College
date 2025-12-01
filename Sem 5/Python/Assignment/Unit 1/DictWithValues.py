#Create a Python program that will have one fruit dictionary with fruit values.
#Display keys and values separately.

fruits = {}
n = int(input("How many fruits do you want to add : "))

for i in range(n):
    fruit = input("Enter the fruit name : ")
    color = input("Enter the fruit color : ")
    fruits[fruit] = color

print("\n fruits name : (keys)")
for key in fruits.keys():
    print(key)
print("\n Fruit color : (values)" )
for value in fruits.values():
    print(value)