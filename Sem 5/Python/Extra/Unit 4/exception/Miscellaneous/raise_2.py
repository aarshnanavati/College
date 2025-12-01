try:  
    a = int(input("Enter a : "))  
    b = int(input("Enter b : "))  
    if b is 0:  
        raise ArithmeticError;  
    else:  
        print("a/b = ",a/b) 
except ValueError:
	print("The values must be numbers")
except ArithmeticError:  
    print("The value of b can't be 0")