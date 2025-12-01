# Build a BankAccount class with withdraw and deposit methods. Use assert to ensure withdrawal amount is 
# positive, raise to throw InsufficientBalanceError, and finally to log every transaction attempt to a text file.

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self,name,balance=0):
        self.name =  name
        self.balance = balance
        self.log_file = "transaction_log.txt"

    def deposit(self,amount):
        try:
            assert amount > 0,"Deposit amount must be positive"
            self.balance += amount
            print(f"Amount RS{amount} deposited successfully. Current Balance: Rs{self.balance}")
        except AssertionError as e:
            print("Error:",e)
        finally:
            self._log_transaction(f"Deposit Attempt: Rs{amount}, Balance: Rs{self.balance}")

    def withdraw(self,amount):
        try:
            assert amount > 0 , "Withdrawal amount must be positive"
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient Balance !")
            self.balance -= amount
            print(f"Amount RS{amount} withdrawn successfully. Current Balance: Rs{self.balance}")
        except InsufficientBalanceError as e:
            print("Error!",e)
        finally:
            self._log_transaction(f"Deposit Attempt: Rs{amount}, Balance: Rs{self.balance}")

    def _log_transaction(self,message):
        with open(self.log_file,"a") as file:
            file.write(f"{self.name} - {message}\n")

try:
  
    name = input("Enter your name: ")
    balance = float(input("Enter your opening balance: ₹"))


    account = BankAccount(name, balance)
    print(f"\nAccount created successfully for {name} with balance ₹{balance}\n")


    deposit_amount = float(input("Enter amount to deposit: ₹"))
    account.deposit(deposit_amount)

    withdraw_amount = float(input("Enter amount to withdraw: ₹"))
    account.withdraw(withdraw_amount)

    print(f"\n💰 Final Balance for {name}: ₹{account.balance}")
    print("------ End of Transaction ------")

except ValueError:
    print("⚠️ Invalid input! Please enter numeric values for amounts.")