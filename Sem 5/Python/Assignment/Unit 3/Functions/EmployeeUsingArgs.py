# Write a function using **varargs to print employee details like name, department, and salary.

def employeeDetail(*args):
    print("Employee Details : ")
    for detail in args:
        print(detail)

employeeDetail("Name : John Doe","Department: 11","Salary : 56000")