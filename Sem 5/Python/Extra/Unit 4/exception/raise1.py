try:  
        a=10  
        print(a)
        raise NameError("Raise Exception")  
except NameError as e:  
        print("An exception occurred")  
        print(e)  

'''
To raise an exception, raise statement is used. It is followed by exception class name.
Exception can be provided with a value that can be given in the parenthesis. (here, Raise Exception)
To access the value "as" keyword is used. "e" is used as a reference variable which stores the value of the exception.
'''