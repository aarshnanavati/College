# Simulate an online ticket booking system where user inputs seat numbers. Handle errors for 
# invalid seat number range, already booked seats, and invalid data types.

total_seats = list(range(1,11))
booked_seats = []

def book_ticket():
    print("Welcome to Online Ticket Booking System")
    print("Available seats: ",[seat for seat in total_seats if seat not in booked_seats])

    try:
        seat_no = int(input("Enter seat number you want to book(1-10): "))

        if seat_no not in total_seats:
            raise ValueError("Invalid seat number!Please choose between (1-10)")
        
        if seat_no  in booked_seats:
            raise Exception("Seat already book!Please choose another seat.")
        
        booked_seats.append(seat_no)
        print(f"Seat {seat_no} booked successfully!")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
    except:
        print("Invalid number!Try Again")

while True:
    book_ticket()
    choice =  input("Do you want to book another seat? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Final Booked Seats: ",book_ticket)
        print("Thank You for using our booking system!")
        break