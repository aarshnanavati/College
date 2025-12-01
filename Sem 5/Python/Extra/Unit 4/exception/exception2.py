try:
	number = int(input("Enter a number between 1 - 10 "))
except ValueError:
	print("OHHHHH..... numbers only")
else:
	print("you entered number ", number)