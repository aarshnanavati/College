
users= {}
n = int(input("Enter the accounts : "))

for i in range(n):
    username = input("Enter username : ")
    password = input("Enter password: ")
    users[username] = password

print("Users created.try to login")

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    attempts += 1
    username =  input("Enter username  : ").strip()
    password =  input("Enter Password : ").strip()

    if username in users and users[username] == password:
        print("Succesful!")
        break
    else:
        remaining =  max_attempts - attempts
        print("Incorrect username and pssword!")
        if remaining:
           print("Attempte left")
        else:
            print("Login successful")