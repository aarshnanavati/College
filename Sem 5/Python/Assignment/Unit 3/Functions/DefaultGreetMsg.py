# Write a function to greet a person by name, with a default greeting message if no name is given.

def greet(name = "Guest"):
    print("hello",name,"Welcome")

user_name = input("Enter your name : ")

if user_name.strip() == "":
    greet()
else:
    greet(user_name)