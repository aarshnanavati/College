#Create two sets: even and prime numbers between 1–20. Find union, intersection, difference, 
#and symmetric difference. Convert one to frozenset and try modifying it (handle the error).

even = set(map(int,input("Enter the even numbers ").split()))
prime = set(map(int,input("Enter the prime numbers : ").split()))

print("Even \n",even)
print("Prime \n ",prime)

print("Union \n ",(even|prime))
print("Intesection : \n ",(even & prime))
print("Difference (even - prime): \n",(even -  prime))
print("Difference (prime - even): \n",(prime -  even))
print("Symmetric Difference: ",(even ^ prime))

fprime = frozenset(prime)
print("Converted to frozenset \n",fprime)

try:
    fprime.add(23)
except AttributeError as e:
    print("\nError while modifying frozenset:", e)
    print("Frozenset is immutable — cannot add or remove elements.")