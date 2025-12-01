
def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(average(10,5))
print(average(3,6))