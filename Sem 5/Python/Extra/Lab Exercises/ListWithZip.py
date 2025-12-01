#Create two lists: one with keys and one with values. Combine them into a dictionary using 
#zip()` and update one of the values.

keys = input("Enter keys").split()
values = input("Enter values : ").split()

my_dict = dict(zip(keys,values))
print("Original Dictionary : ",my_dict)

key_to_update = input("Enter key to update: ")
value_to_update = input("Enter value to update :")

if key_to_update in my_dict:
    my_dict[key_to_update] = value_to_update
    print("Updated Successfully!!",my_dict)
else:
    print("Key not found!")
