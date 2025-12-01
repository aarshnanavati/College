
festival = []
n = int(input("Enter the number of festivals you want to add: "))

for i in range(n):
    festival_name = input("Enter the festival name: ")
    festival.append(festival_name)
print("Your festival list:", festival)

# Print only first element of list
print("\n First festival in the list : ",festival[0])

# Print elements starting from 2nd till 3rd (index 1 to 2)
print("\n Festivals from 2nd to 3rd in the list : ",festival[1:3])

# Print elements starting from 2nd element till last
print("\n Festivals from 2nd to last in the list :",festival[1:])

# Print whole list 4 times
print("\n whole festival list 4 times : ",festival * 4)