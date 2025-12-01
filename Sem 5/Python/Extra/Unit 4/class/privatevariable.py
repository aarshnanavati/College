class mclass:  
    __privateVariable1 = 2018;  
    def __privateMethod1(self):  
        print("I'm inside the class mainclass which this is private method")  
    def insideclass(self):  
        print("Private Variable: ")  
        self.__privateMethod1()  
class nclass(mclass):
	def display(self):
		mclass.__privateMethod1(self)
obj = nclass()  
obj.insideclass()  
obj.display()