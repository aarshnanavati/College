# Define variables
x = 10
y = 10
z = [10]

print("x =", x)
print("y =", y)
print("z =", z)

print("\n--- Identity Operator Demonstration ---")

# Using 'is'
print("x is y:", x is y)       # True, because small integers are cached
print("x is z[0]:", x is z[0]) # True, because z[0] == 10, and Python caches small integers

# Using 'is not'
print("x is not z:", x is not z)  # True, because x is int, z is list (different types/objects)

# Another example with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\nlist1 is list2:", list1 is list2)   # False (same values, different objects)
print("list1 is list3:", list1 is list3)     # True (same object)
print("list1 is not list2:", list1 is not list2)  # True
