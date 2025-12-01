# 7. Write a program to create a function employee () using the following conditions.
# a. It should accept the employee’s name and salary and display both.
# b. If the salary is missing in the function call, then assign default value 10000 to salary

def employee(name,salary=10000):
    print("Employee name: ",name)
    print("Employee salary: ",salary)

name = input("Enter employee name: ")
salary_input = input("Enter employee salary (press enter to use default 10000): ")

if salary_input.strip() == "":
    employee(name)
else:
    employee(name,float(salary_input))
