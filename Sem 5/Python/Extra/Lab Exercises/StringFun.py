#Write a python program to perform following operations on string. 
#• Reverse string and print it • count the occurance 
#• Check whether the string endswith particular substring or not • find substring

text = input("Enter a string:")

print("Reversed String : ",text[::-1])
count_string = input("Enter a substring to count its occurrence: ")
count = text.count(count_string)
print(f"Occurrence of '{count_string}': {count}")

ending = input("Enter a substring to check if the string ends with it: ")
if text.endswith(ending):
    print("The string ends with \n",ending)
else:
    print("The string does not end with \n",ending)

