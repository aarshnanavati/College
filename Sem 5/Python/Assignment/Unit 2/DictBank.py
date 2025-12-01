#Write a program that simulates a basic bank transaction system using dictionary: account numbers
#as keys and balance as values.Allow user to deposit, withdraw, and check balance.

# Create empty dictionary for accounts
accounts = {}

# Create accounts based on user input
num_acc = int(input("Enter number of accounts to create: "))
for i in range(num_acc):
    acc_no = int(input(f"Enter account number {i+1}: "))
    balance = float(input(f"Enter initial balance for account {acc_no}: "))
    accounts[acc_no] = balance

# Bank menu
while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you for using the bank system!")
        break

    acc_no = int(input("Enter account number: "))

    if acc_no not in accounts:
        print("Account not found!")
        continue

    if choice == 1:  # Deposit
        amount = float(input("Enter deposit amount: "))
        accounts[acc_no] += amount
        print("Deposit successful! New balance:", accounts[acc_no])

    elif choice == 2:  # Withdraw
        amount = float(input("Enter withdrawal amount: "))
        if amount <= accounts[acc_no]:
            accounts[acc_no] -= amount
            print("Withdrawal successful! New balance:", accounts[acc_no])
        else:
            print("Insufficient funds!")

    elif choice == 3:  # Check balance
        print("Account Balance:", accounts[acc_no])

    else:
        print("Invalid choice! Please try again.")
