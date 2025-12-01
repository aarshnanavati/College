try:  
	a=8/0 
	print(a)
except ArithmeticError:  
	print("This statement is raising an exception, no. 1 cannot dvided by 0")
else:  
	print("Welcome")
