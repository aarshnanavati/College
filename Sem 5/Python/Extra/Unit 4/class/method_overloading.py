# Is there any way to impelement function overloading
# How overriding works? 
#Python does not support function overloading
class cal:
	def area(self,l):
		a=l*l
		print(a)
	def area(self,l,b):
		a=l*b
		print(a)

obj=cal()
#obj.area(10)
obj.area(5,4)	