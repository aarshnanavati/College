class BankAccount:
	def __init__(s):
		s.balance = 0

	def withdraw(s, amount):
		s.balance -= amount
		return s.balance

	def deposit(s, amount):
		s.balance += amount
		return s.balance
		
a = BankAccount()
b = BankAccount()
print(a.deposit(100))
print(b.deposit(50))
print(b.withdraw(10))
print(a.withdraw(10))
