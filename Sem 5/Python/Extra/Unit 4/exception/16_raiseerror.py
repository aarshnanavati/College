def demo_no_catch():
	n = int(input("Please enter an integer: "))
	print(n)
	if n==5:
		raise Exception('Entered value is equal to 5')
	else:
		print("Entered Value is Fine")
       	
try:	
	demo_no_catch()	
except Exception as e:
		#demo_no_catch()
		print('we caught an exception: Exception',e)

