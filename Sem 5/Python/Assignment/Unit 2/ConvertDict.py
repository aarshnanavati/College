#Create a program to input two lists and convert them into a dictionary using one as keys
#and one as values. Swap key-value pairs and display the reversed dictionary.

keys = input("Enter the key: ").split()
values = input("Enter the values : ").split()

if len(keys)!=len(values):
    print("Error the values are not matching!!")
else:
    original_dict = dict(zip(keys,values))
    print("\n Original Dictionary : ")
    print(original_dict)

    reversed_dict = {v:k for k,v in original_dict.items()}
    print("reversed dictionary : ")
    print(reversed_dict)   