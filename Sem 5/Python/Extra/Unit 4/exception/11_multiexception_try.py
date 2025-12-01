print("Selective trapping of user input errors")
first = 1
second = 2
third = 3
while 1:
    try:
        extra = int(input("What is the extra value? "))
        break
    except EOFError:
        print ("[EOF]\nNo data available. Default assumed")
        extra = 4
        break
    except (NameError,SyntaxError):
        print("Please don't do that. Please enter a number")
    except(StandardError, e):
        print("Strange input!")
        print("Exception type",e.__class__.__name__)
        print("Please try again")

total = first+second+third+extra
print(total)


