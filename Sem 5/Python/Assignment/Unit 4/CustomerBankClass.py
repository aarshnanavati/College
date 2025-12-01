# Write a python program to create a class Bank with following members:
#   Id- Private  Name -Protected  Balance – Public Member Functions: • 
#  Constructor to initialize balance as 1000. Create another class named Customer and add following methods:
#  withdraw()  - To withdraw money deposit() - To deposit money interest()  -  calculate interest
#  Call all the methods appropriately and print Id, Name and Balance.

class Bank:
    def __init__(self,cust_id,name):
        self.__id = cust_id
        self._name = name
        self.balance = 1000

    def display(self):
        print("\n----- Bank Account Details -----")
        print("Customer ID:", self.__id)
        print("Customer Name:", self._name)
        print("Current Balance:", self.balance)

class Customer(Bank):
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdraw : {amount} New Balance: {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited : {amount}.New Balance: {self.balance}")

    def interest(self,rate):
        interest_amt = (self.balance * rate) / 100
        self.balance += interest_amt
        print(f"Interest Added : {interest_amt} . New Balance : {self.balance}")

name = input("Enter Customer Name : ")
id = int(input("Enter ID:"))
c1 = Customer(name,id)

c1.display()

custDeposit = int(input("Enter Deposit Number: "))
custWithdraw = int(input("Enter Withdrawal Amount: "))
custInt = int(input("Enter Rate: "))
c1.deposit(custDeposit)
c1.withdraw(custWithdraw)
c1.interest(custInt)

c1.display()