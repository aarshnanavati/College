#Create a dictionary with employee names and salaries. Increase salary by 10% if it's <50,000.
#Remove employees whose updated salary exceeds 1,00,000.

employees = {}
n = int(input("Enter the number of employees : "))

for i in range(n):
    emp_name = input("Enter the name of employees : ")
    emp_sal = float(input("Enter the salary of employees : "))
    employees[emp_name] = emp_sal

for emp_name in employees:
    if employees[emp_name] < 50000:
        employees[emp_name] += employees[emp_name] * 0.10

for emp_name in list(employees.keys()):
    if employees[emp_name] > 100000:
        del employees[emp_name]

print("Updated List")
for emp_name,emp_sal in employees.items():
    print(f"{emp_name} : {emp_sal:.2f}")