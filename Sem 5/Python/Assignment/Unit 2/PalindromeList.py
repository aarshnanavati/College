
list1 = []

n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    element = int(input("Enter elements: "))
    list1.append(element)

copy_list = list1.copy()
list1.reverse()

if(copy_list == list1):
    print("The given list is a palindrome")
else:
    print("The given list is not a palindrome")