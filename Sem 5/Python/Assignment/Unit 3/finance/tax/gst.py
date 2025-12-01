# Suppose you are building a package named finance with a sub-package tax containing: 
# income_tax.py → function calculate_tax(income) (10% tax if income > 50000 else 5%). 
# gst.py → function calculate_gst(amount) (18% GST). Write a program to import both modules and c
# ompute the final payable amount for a product and also calculate income tax for a given salary. 


def calculate_gst(amount):
    return amount * 0.18