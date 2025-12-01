#Write a program to manage a contact book using dictionary.
#Allow user to add, update, delete, and search contacts using menu-driven approach

contacts = {}

while True:
    print("1. Add \n")
    print("2. Update \n")
    print("3. Delete \n")
    print("4. Search \n")
    print("5. View All \n")
    print("6. Exit \n")
    ch = input("Enter your choice : ")

    if ch == '1':
        name = input("name")
        phone = input("phone")
        contacts[name] = phone
        print("Added.")
    
    elif ch == '2':
        name = input("Name to update: ")
        if name in contacts:
            contacts[name] =  input("New phone : ")
            print("Updated!")
        else:
            print("Not found!")

    elif ch == '3':
        name = input("Name to delete : ")
        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print ("Not found!")

    elif ch == '4':
        name = input("Name to search : ")
        print("Phone",contacts.get(name,"Not found"))
    
    elif ch == '5':
        print(contacts if contacts else "not found")
    
    elif ch == '6':
        break

    else:
        print("Invalid choice!")
