# . Write a function to calculate simple interest where the rate of interest has a 
# default value of 5%.

def simple_int(principal,time,rate = 5):
    si = (principal * rate * time) / 100
    return si

p = float(input("Enter the principal : "))
t = int(input("Enter the time : "))

print("Simple Interest : (default at 5% rate) = ",simple_int(p,t))