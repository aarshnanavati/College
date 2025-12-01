# Write a function to find the largest of three numbers.//WANR

def largest(a,b,c):
    if a>=b and a>=c:
      print(a,"is bigger")
   
    elif b>=a and b>=c:
        print(b,"is bigger")
      
    else:
        print(c,"is bigger")
        
    
a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
c = int(input("Enter a third number : "))

largest(a,b,c)
