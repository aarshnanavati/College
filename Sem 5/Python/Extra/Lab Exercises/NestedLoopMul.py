#Create a nested loop to generate a multiplication table from 1 to 10 (in matrix format).

for i in range(1,11):
    for j in range(1,11):
        print (f"{i*j:4}",end="")
    print()