a=int(input("enter a integer"))
c=a/2
try:
	if c==0:
		raise Exception()
	else:
		print("Good")
except Exception as e:
	print("the error is", e.args)
