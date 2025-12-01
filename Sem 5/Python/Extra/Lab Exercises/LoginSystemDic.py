#Write a login system using a dictionary. Allow up to 3 login attempts and show success or
#failure with proper message.

# users = {}
# n = int(input("How many accounts do you want to add :"))

# for i in range(n):
#     username = input("Enter username  : ").strip()
#     password = input("Enter Password : ").strip()
#     users[username] = password

# print("Users created .  Now try to login \n")

# max_attempts = 3
# attempt = 0

# while attempt < max_attempts:
#     attempt += 1
#     username =  input("Enter username  : ").strip()
#     password =  input("Enter Password : ").strip()

#     if username in users and users[username] == password:
#         print("Login Successful!")
#         break
#     else:
#         remaining = max_attempts - attempt
#         print("Incorrect Username and Password:")
#         if remaining:
#             print("Attempts left",remaining)
#         else:
#             print("Login Failed")


users = {}
n = int(input("How many accounts do u want to add?"))

for i in range(1,n+1):
    username = input(f"Enter username {i} : ")
    password = input("Enter password for {username} : ")
    users[username] = password

print("Accounts created ! Now you can login")

for attempt in range(1,4):
    username = input("Enter your username:  ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
        break
    else:
        print("Invalid username or password. Please try again.")
        if attempt < 3 : 
            print(f"Attempt left  : {3 - attempt} \n")
        else:
            print("Login Failed! No attempts left.")