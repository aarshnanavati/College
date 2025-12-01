#Write a Python program to create a dictionary with 3 key-value pairs and print each key and its corresponding value.

myDict = {}

for i in range(3):
    key=input("Enter key :")
    value = input("Enter value :")
    myDict[key] = value

for key in myDict:
    print (f"{key}:{myDict[key]}")