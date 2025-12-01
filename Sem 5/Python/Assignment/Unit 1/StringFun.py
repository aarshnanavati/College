#Write a python program to perform following operations on string.
#• Reverse string and print it • count the occurance 
#• Check whether the string endswith particular substring or not 
#•find substring'''

text = input("Enter a string : ")
reversed_text = text[::-1]
print("Reversed String: \n",reversed_text)

sub = input("Enter a substring to find its occurrence: ")
print("Orrcurance of string : ",text.count(sub))

end = input("Enter a substring to check if the string ends with it: ")
print("Ends with",end,"?",text.endswith(end))

find = input("ENter a substring to find its position: ")
print("Position : ",text.find(find))