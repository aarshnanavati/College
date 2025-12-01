# Implement an e-commerce hierarchy: User → Customer → PremiumCustomer. Add discounts and loyalty points calculations at each level.

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

class Customer(User):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.loyalty_points = 0

    def calculateDiscount(self,amount):
        return amount * 0.95
    
    def addLoyaltyPoints(self,amount):
        self.loyalty_points += int(amount // 100)

class PremiumCustomer(Customer):
    def calculateDiscount(self,amount):
        return amount * 0.85
    
    def addLoyaltyPoints(self,amount):
        self.loyalty_points += int(amount // 100)

if __name__ == "__main__":
    print("=== E-Commerce System ===")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    amount = float(input("Enter purchase amount: "))
    c1 = Customer(name, email)
    final_price = c1.calculateDiscount(amount)
    c1.addLoyaltyPoints(final_price)

    print(f"\nCustomer: {c1.name} ({c1.email})")
    print(f"Original Price: ₹{amount}")
    print(f"After Discount: ₹{final_price}")
    print(f"Loyalty Points: {c1.loyalty_points}")

 
    print("\n--- Premium Customer ---")
    name = input("Enter premium customer name: ")
    email = input("Enter premium customer email: ")
    amount = float(input("Enter purchase amount: "))
    c2 = PremiumCustomer(name, email)
    final_price = c2.calculateDiscount(amount)
    c2.addLoyaltyPoints(final_price)

    print(f"\nPremium Customer: {c2.name} ({c2.email})")
    print(f"Original Price: ₹{amount}")
    print(f"After Discount: ₹{final_price}")
    print(f"Loyalty Points: {c2.loyalty_points}")