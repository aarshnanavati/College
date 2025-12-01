#  Define a class Teacher with the following specification:  Private members:     
# Name : 20 char subject: 10 char  Basic, DA,HRA : float Salary: float Calculate () -
# function computes the salary and returns it. Salary is sum of basic, DA and HRA Public member:
# Readdata() function accept the data values and invoke the calculate function

class Teacher:
    def __init__(self):
        self.__Name = ""
        self.__Subject = ""
        self.__Basic = 0.0
        self.__DA = 0.0
        self.__HRA = 0.0
        self.__Salary = 0.0

    def __calculate(self):
        self.__Salary = self.__Basic +self.__DA + self.__HRA
        return self.__Salary

    def readdata(self):
        self.__Name = input("Enter teacher Name: ")[:20]
        self.__Subject = input("Enter subject name: ")[:10]
        self.__Basic = float(input("Enter Basic salary: "))
        self.__DA = float(input("Enter DA: "))
        self.__HRA = float(input("Enter HRA:"))

        total = self.__calculate()
        print("Teacher Details:\n")
        print("Name: ",self.__Name)
        print("Subject : ",self.__Subject)
        print("Total :",total)

t1 = Teacher()
t1.readdata()