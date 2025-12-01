# Create a TravelAgency class that manages multiple Trip objects.Each trip contains destination, cost,
#  and duration. Accept trips from the user and display the most expensive trip.

class Trip:
    def __init__(self,destination,cost,duration):
        self.destination = destination
        self.cost = cost
        self.duration = duration

    def __str__(self):
        return f"Destination :{self.destination} , cost: {self.cost } , Duration : {self.duration}days"

class TravelAgency:
    def __init__(self):
        self.trips = []

    def add_trip(self,trip):
        self.trips.append(trip)

    def most_expensive_trip(self):
        if not self.trips:
            return None
        return max(self.trips,key=lambda t: t.cost)
    
    def display_trips(self):
        print("All trips:")
        for trip in self.trips:
            print(trip)

if __name__ == "__main__":
    agency = TravelAgency()

    n = int(input("Enter the no of trips: "))
    for i in range(n):
        destination = input(f"Enter destination for the trip: ")
        cost = float(input("Enter cost: "))
        duration = int(input("Enter duration: "))
        trip = Trip(destination,cost,duration)
        agency.add_trip(trip)

    agency.display_trips()

    expensive = agency.most_expensive_trip()
    if expensive:
        print("\n Most Expensive Trip:")
        print(expensive)