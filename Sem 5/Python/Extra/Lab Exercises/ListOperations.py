#Demonstrate list operations: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, 
#`reverse()`, `sort()` in descending order.

my_list = []
n = int(input("Enter the numbers for list : "))

for i in range(n):
    nums = int(input("Enter the numbers in list : "))
    my_list.append(nums)
print("List : ",my_list)

num_to_append = int(input("Enter the number to append : "))
my_list.append(num_to_append)
print("After Append : ",my_list)

num_to_extend = list(map(int,input("Enter the number to extend : ").split()))
my_list.extend(num_to_extend)
print("After Extend : ",my_list)

pos = int(input("Insert at specific position : "))
value = int(input("Insert the value : "))
my_list.insert(pos,value)
print("After insert : ",my_list)

value_to_remove = int(input("Enter value to be removed : "))
if value_to_remove in my_list:
    my_list.remove(value_to_remove)
    print("After remove : ",my_list)
else:
    print("Value not found!")

value_to_pop = int(input("Enter index to pop: "))
if 0 <= value_to_pop < len(my_list):
    popped = my_list.pop(value_to_pop)
    print("After pop :",my_list)
else:
    print("Invalid value!")

print("Reversing  : ",(my_list.reverse()))

my_list.sort(reverse=True)
print("After Descending : ",my_list)