
from finance.tax import income_tax,gst



salary = float(input("Enter the Salary :"))
product_price = int(input("Enter the product price: "))

tax_amount = income_tax.calculate_tax(salary)
gst_ampunt = gst.calculate_gst(product_price)
final_price = product_price + gst_ampunt

print(f"Salary: {salary}")
print(f"Income tax: {tax_amount}")

print(f"Product price: {product_price}")
print(f"GST amount: : {gst_ampunt}")
print(f"Final amount : {final_price}")