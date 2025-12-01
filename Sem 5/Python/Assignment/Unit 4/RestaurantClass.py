# Build a Restaurant ordering system. Create classes for MenuItem and Order. Allow adding menu items and computing the total bill with tax.
#  Access attributes via methods only (no direct attribute printing).

class MenuItem:
    def __init__(self,name,price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

class Order:
    Tax_rate = 0.1

    def __init__(self):
        self.__items = []

    def add_item(self,item):
        if isinstance(item,MenuItem):
            self.__items.append(item)
        else:
            raise ValueError("Only MenuItem instances can be added")
        
    def get_items(self):
        return self.__items
    
    def compute_subtotal(self):
        return sum(item.get_price() for item in self.__items)
    
    def compute_tax(self):
        return self.compute_subtotal() * Order.Tax_rate
    
    def compute_total(self):
        return self.compute_subtotal() + self.compute_tax()
    

if __name__ == "__main__":
    print("Welcome to the Restaurant Ordering System")

    menu = []
    n = int(input("Enter number of menu items: "))
    for i in range(n):
        name = input("Enter name of items:")
        price = float(input("Enter price of item: "))
        menu.append(MenuItem(name,price))

    order = Order()
    while True:
        print("\n Menu : ")
        for idx,item in enumerate(menu,start=1):
            print(f"{idx} . {item.get_name()} - rs{item.get_price()}")

        choice = int(input("Enter item number to add to order (0 to finis):"))
        if choice == 0:
            break
        elif 1 <= choice <= len(menu):
            order.add_item(menu[choice-1])
            print(f"{menu[choice - 1].get_name()} added to order")
        else:
            print("Invalid choice")

    print("--BILL--")
    for item in order.get_items():
        print(f"-{item.get_name()} : rs{item.get_price()}")

    print(f"\nSubtotal: ₹{order.compute_subtotal()}")
    print(f"Tax (10%): ₹{order.compute_tax():.2f}")
    print(f"Total Bill: ₹{order.compute_total():.2f}")
    print("----------------")
    print("🙏 Thank you for dining with us! 🙏")
