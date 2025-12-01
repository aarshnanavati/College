#  Try, except, else and finally

"""
try - enters at the top and continues through the block
except-s - jump to there is an exception is thrown
else - run after the try block completes without exception thrown
finally - always run after the other blocks have completed
"""

print "(bfor) Exception demonstration\n"

while True:
        try:
                n = input("(try-) Please enter a Python value: ")
        except KeyboardInterrupt:
                print "(ex/k) You give up?"
                print "(ex/k) Won't break me that way"
        except Exception,e:
                print "(exce) Not acceptable!"
                print "(exce) Message: ",e
                print "(exce) Failure Type:",e.__class__.__name__
        else:
                print "(else) Input accepted"
                break
        finally:
                print "(finl) Tidying up\n"

print "(done) Value received:",n
