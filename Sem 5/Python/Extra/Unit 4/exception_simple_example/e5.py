try:
    n = input("enter n:")
    res = 100 / n
    
except:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")