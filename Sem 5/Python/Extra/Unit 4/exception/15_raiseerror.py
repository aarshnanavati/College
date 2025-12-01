x=int(input("Enter the integer value"))
if x < 5:
	raise Exception('x should not exceed 5. The value of x was {}'.format(x))


#The program comes to a halt and displays our exception to screen, offering clues about what went wrong.
