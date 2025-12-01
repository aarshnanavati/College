try:
    n = int(input("enter n:"))
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter valid number!")

except:
    print("Enter a valid number!")
   
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")