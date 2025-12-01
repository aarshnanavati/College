class Employee:
	'Class for all employees'   
	def __init__(self,name, salary):
		self.name = name
		self.salary = salary
	def displayEmployee(self):
		print("Name : ", self.name,  ", Salary: ", self.salary)
emp1 = Employee("Rahul",10000)
print(Employee.__doc__)
print(emp1.name)
emp1.displayEmployee()








'''
The first method __init__() is a special method, 
which is called class constructor or initialization 
method that Python calls when you create a new
instance of this class.

User declare other class methods like normal 
functions with the exception that the first argument
to each method is self. Python adds the self argument
to the list for user; user do not need to include it when 
you call the methods.
'''

