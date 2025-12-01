# Write a function using *varargs to calculate the average of any number of numeric arguments.

def average(*args):
    if len(args) == 0:
        return 0
    return sum(args)/len(args)

print(average(10,5))
print(average(3,5,7))
print(average())