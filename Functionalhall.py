# wap a program on functionalHall Booking System 


halls = {
    'A': {'capacity': 100, 'price_per_hour': 500, 'bookings': []},
    'B': {'capacity': 50, 'price_per_hour': 300, 'bookings': []},
    'C': {'capacity': 200, 'price_per_hour': 800, 'bookings': []},
}

booking_id_counter = 1000

while True:
    print("\n" + "="*50)
    print("         HALL BOOKING SYSTEM")
    print("="*50)
    print("1. View Available Halls")
    print("2. Book a Hall")
    print("3. View My Bookings")
    print("4. Cancel Booking")
    print("5. Exit")
    print("="*50)
    
    choice = input("Enter your choice (1-5): ").strip()
    
  
    if choice == '1':
        print("\n" + "-"*50)
        print("AVAILABLE HALLS")
        print("-"*50)
        for hall_name, details in halls.items():
            print(f"\nHall {hall_name}:")
            print(f"  Capacity: {details['capacity']} people")
            print(f"  Price per hour: Rs. {details['price_per_hour']}")
            print(f"  Total bookings: {len(details['bookings'])}")
            if details['bookings']:
                print(f"  Booked dates/times:")
                for booking in details['bookings']:
                    print(f"    - Booking ID: {booking['id']}, Date: {booking['date']}, Time: {booking['time']}-{booking['end_time']}, Guest: {booking['guest_name']}")
            else:
                print(f"  Status: AVAILABLE")
    
  
    elif choice == '2':
        print("\n" + "-"*50)
        print("BOOK A HALL")
        print("-"*50)
        print("Available Halls: A, B, C")
        hall_choice = input("Enter hall name (A/B/C): ").upper().strip()
        
        if hall_choice not in halls:
            print("Invalid hall selection!")
            continue
        
        guest_name = input("Enter your name: ").strip()
        if not guest_name:
            print("Name cannot be empty!")
            continue
        
        email = input("Enter your email: ").strip()
        phone = input("Enter phone number: ").strip()
        date = input("Enter booking date (DD-MM-YYYY): ").strip()
        time_slot = input("Enter time slot (HH:MM format, e.g., 09:00): ").strip()
        duration = input("Enter duration in hours: ").strip()
        
        try:
            duration = int(duration)
            if duration <= 0:
                print("Duration must be positive!")
                continue
        except ValueError:
            print("Invalid duration!")
            continue
       
        time_parts = time_slot.split(':')
        start_hour = int(time_parts[0])
        start_min = int(time_parts[1])
        end_hour = (start_hour + duration) % 24
        end_min = start_min
        end_time = f"{end_hour:02d}:{end_min:02d}"
        
   
        cost = halls[hall_choice]['price_per_hour'] * duration
        
        
        conflict = False
        for booking in halls[hall_choice]['bookings']:
            if booking['date'] == date:
                conflict = True
                break
        
        if conflict:
            print(f"Hall {hall_choice} is already booked on {date}!")
            continue
        
       
        print("\n" + "-"*50)
        print("BOOKING CONFIRMATION")
        print("-"*50)
        print(f"Hall: {hall_choice}")
        print(f"Capacity: {halls[hall_choice]['capacity']} people")
        print(f"Date: {date}")
        print(f"Time: {time_slot} to {end_time}")
        print(f"Duration: {duration} hours")
        print(f"Total Cost: Rs. {cost}")
        print("-"*50)
        
        confirm = input("Confirm booking? (Y/N): ").upper().strip()
        
        if confirm == 'Y':
            booking_id_counter += 1
            new_booking = {
                'id': booking_id_counter,
                'guest_name': guest_name,
                'email': email,
                'phone': phone,
                'date': date,
                'time': time_slot,
                'end_time': end_time,
                'duration': duration,
                'cost': cost
            }
            halls[hall_choice]['bookings'].append(new_booking)
            print(f"\n✓ Booking successful!")
            print(f"Your Booking ID: {booking_id_counter}")
            print(f"Confirmation email will be sent to {email}")
        else:
            print("Booking cancelled!")
    
  
    elif choice == '3':
        print("\n" + "-"*50)
        print("VIEW MY BOOKINGS")
        print("-"*50)
        search_name = input("Enter your name: ").strip()
        found = False
        
        for hall_name, details in halls.items():
            for booking in details['bookings']:
                if booking['guest_name'].lower() == search_name.lower():
                    found = True
                    print(f"\nHall {hall_name} - Booking ID: {booking['id']}")
                    print(f"  Name: {booking['guest_name']}")
                    print(f"  Email: {booking['email']}")
                    print(f"  Phone: {booking['phone']}")
                    print(f"  Date: {booking['date']}")
                    print(f"  Time: {booking['time']} to {booking['end_time']}")
                    print(f"  Duration: {booking['duration']} hours")
                    print(f"  Total Cost: Rs. {booking['cost']}")
        
        if not found:
            print(f"No bookings found for {search_name}!")
    
   
    elif choice == '4':
        print("\n" + "-"*50)
        print("CANCEL BOOKING")
        print("-"*50)
        booking_id_str = input("Enter your Booking ID: ").strip()
        
        try:
            booking_id_search = int(booking_id_str)
        except ValueError:
            print("Invalid Booking ID!")
            continue
        
        found = False
        for hall_name, details in halls.items():
            for i, booking in enumerate(details['bookings']):
                if booking['id'] == booking_id_search:
                    found = True
                    print(f"\nBooking Details:")
                    print(f"  Guest: {booking['guest_name']}")
                    print(f"  Hall: {hall_name}")
                    print(f"  Date: {booking['date']}")
                    print(f"  Time: {booking['time']} to {booking['end_time']}")
                    print(f"  Cost: Rs. {booking['cost']}")
                    
                    confirm_cancel = input("\nConfirm cancellation? (Y/N): ").upper().strip()
                    if confirm_cancel == 'Y':
                        refund = booking['cost']
                        details['bookings'].pop(i)
                        print(f"✓ Booking cancelled successfully!")
                        print(f"Refund Amount: Rs. {refund}")
                    else:
                        print("Cancellation aborted!")
                    break
            if found:
                break
        
        if not found:
            print("Booking ID not found!")
    
    
    elif choice == '5':
        print("\nThank you for using Hall Booking System!")
        print("="*50)
        break
    
    else:
        print("Invalid choice! Please try again.")