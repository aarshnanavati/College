# Create a Vehicle base class with subclasses Car, Bike, and Truck. Each should override a method calculate_trip_cost(distance)
# using their own fuel efficiency.

class Vehicle:
    def __init__(self,fuel_price):
        self.fuel_price = fuel_price

    def calculate_trip_cost(self,distance):
        raise NotImplementedError("Subclasses must implement this method")
    
class Car(Vehicle):
    def calculate_trip_cost(self, distance):
       efficiency = 15  
       fuel_needed = distance / efficiency
       return fuel_needed * self.fuel_price

class Bike(Vehicle):
    def calculate_trip_cost(self, distance):
        efficiency = 40  
        fuel_needed = distance / efficiency
        return fuel_needed * self.fuel_price

class Truck(Vehicle):
    def calculate_trip_cost(self, distance):
        efficiency = 8  
        fuel_needed = distance / efficiency
        return fuel_needed * self.fuel_price
    
if __name__ == "__main__":
    print("=== Trip Cost Calculator ===")
    fuel_price = float(input("Enter fuel price per liter (₹): "))
    distance = float(input("Enter trip distance (km): "))

    car = Car(fuel_price)
    bike = Bike(fuel_price)
    truck = Truck(fuel_price)

    print(f"\nTrip Distance: {distance} km | Fuel Price: ₹{fuel_price}/L")
    print(f"Car Trip Cost   : ₹{car.calculate_trip_cost(distance):.2f}")
    print(f"Bike Trip Cost  : ₹{bike.calculate_trip_cost(distance):.2f}")
    print(f"Truck Trip Cost : ₹{truck.calculate_trip_cost(distance):.2f}")