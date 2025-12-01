# Develop a Ride Sharing Application with classes Driver, Passenger, Ride, and Payment. 
# Include dynamic ride fare calculation based on distance and surge pricing, custom exceptions for
# invalid payment method or ride cancellation, and file handling to log completed rides using with.

class InvalidPayemenMethodError(Exception):
    pass
class RideCancellationError(Exception):
    pass

class Driver:
    def __init__(self,name,vehicle):
        self.name = name
        self.vehicle = vehicle

class Passenger:
    def __init__(self,name):
        self.name = name

class Ride:
    def __init__(self,driver,passenger,distance_km):
        self.driver = driver
        self.passenger = passenger
        self.distance = distance_km
        self.completed = False
        self.surge_multiplier = 1.0

    def apply_surge(self,multiplier):
        self.surge_multiplier = multiplier

    def calculate_fare(self):
        base_rate = 10
        fare = base_rate * self.distance * self.surge_multiplier
        return round(fare,2)
    
    def completedRide(self):
        self.completed = True

class Payement:
    def __init__(self,amount,method):
        self.amount = amount
        self.method = method

    def process_payment(self):
        valid_methods = ['cash','upi','card']
        if self.method not in valid_methods:
            raise InvalidPayemenMethodError(f"Invalid Payemnt {self.method}")
        print(f"Payment of Rs{self.amount} successful via {self.method}")

def log_ride(ride,fare):        
    try:
        with open("Rides.txt","a") as file:
            file.write(f"Driver : {ride.driver.name},"
                       f"Passenger: {ride.passenger.name},"
                       f"Distance : {ride.distance}km,"
                       f"Fare: Rs{fare}\n"
                       )
    except Exception as e:
        print("Enter logging ride: ",e)

if __name__ =="__main__":
    driver = Driver("Kashish","Virtus")
    passenger = Passenger("Yesha")

    try:
        distance = float(input("Enter ride distance "))
    except:
        print("Invalid Distance input")
        exit(1)

    ride = Ride(driver,passenger,distance)

    surge_input = input("Enter surge multiplier").strip()
    if surge_input:
        try:
            ride.apply_surge(float(surge_input))
        except:
            print("Invalid Multiplier")

    fare = ride.calculate_fare()
    print(f"Calculate Fare : Rs{fare}")

    payment_method = input("Enter payment method (cash/card/upi): ").strip()
    payment = Payement(fare, payment_method)

    try:
        # Process payment
        payment.process_payment()
        ride.completedRide()
        log_ride(ride, fare)
        print("Ride completed and logged successfully!")
    except InvalidPayemenMethodError as e:
        print("Payment failed:", e)
    except RideCancellationError as e:
        print("Ride cancelled:", e)
    except Exception as e:
        print("Unexpected error:", e)
