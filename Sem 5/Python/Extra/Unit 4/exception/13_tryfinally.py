
print("Trapping a runtime error")

first = 1
second = 2
third = 3
try:
	extra = input("What is the extra value? ")
except StandardError:
	print("That's not a number. I'll assume you mean 4")
	extra = 4
	total = first+second+third+extra
	print(total)
finally:
	print("You are entering right value")
