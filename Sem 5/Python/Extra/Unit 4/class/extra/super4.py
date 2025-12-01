class A:
	def __init__(self, a):
		self.a=a
	def disp(self):
		print(self.a)
		
class B(A):
	def __init__(self,a,b):
		A.__init__(self,a)
		self.b=b
	def prin(self):
		print(self.b)
		
b1=B(1,2)
b1.disp()
b1.prin()