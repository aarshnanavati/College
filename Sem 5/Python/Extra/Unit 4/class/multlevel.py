class X():
    def __init__(self,a):
        self.num = a
    def doubleup(self):
        self.num *= 2
 
class Y(X):
    def __init__(self,a):
        X.__init__(self,a)
    def tripleup(self):
        self.num *= 3
 
class Z(Y):
	def __init__(self,a):
		Y.__init__(self,a)
	def square(self):
		self.num =self.num*self.num
obj = Z(4)
print(obj.num)
obj.doubleup()
print(obj.num)
obj.tripleup()
print(obj.num)
obj.square()
print(obj.num)
