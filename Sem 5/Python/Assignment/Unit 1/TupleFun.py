#Create a Python program that will have one tuple of vegetables with values
#(‘Potato’, ‘Brinjal’,‘Tomato’,‘Cabbage’, ‘Cauliflower’).
#Perform following operations: • Print whole tuple 
#• Print only first element of tuple • Prints elements starting from 2ndtill4th
# Prints elements starting from 2ndelement till last 
#• Print whole tuple twice using appropriate operator."""
                                                                            
veg_list = []

n = int(input("Enter the number of vegetables you want to add: "))

for i in range(n):
    veg = input("Enter the vegetable name : ")
    veg_list.append(veg)

vegetable_tuple = tuple(veg_list)

print("Your vegetable tuple:", vegetable_tuple)
print("First element of tuple \n : ",vegetable_tuple[0])
print("\n Vegetables from 2nd to 4th in the tuple : ",vegetable_tuple[1:4])
print("\n vegetables from 2nd to last in the tuple : ",vegetable_tuple[1::])
print("\n printing whole tuple twice : ",vegetable_tuple * 2)
