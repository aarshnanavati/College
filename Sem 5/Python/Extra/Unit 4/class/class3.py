class Student:  
	def __init__(self, rollno, name):  
		self.rollno = rollno  
		self.name = name  
	def displayStudent():  
		print("rollno : ", self.rollno,  ", name: ", self.name )
st1 = Student(1, "Rahul")  
st2 = Student(2, "Akshay")  
st1.displayStudent()  
st2.displayStudent()  
