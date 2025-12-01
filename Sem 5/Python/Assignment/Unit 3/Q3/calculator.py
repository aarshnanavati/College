# . Write a Python program to create a module called calculator.py with add (), sub(), mul(), div()
# and call this module into another file named calc.py using from… import syntax.

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Division by zero is not allowed"    