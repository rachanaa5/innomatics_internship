def manage_registrations(capacity, total_registrations):
    if total_registrations > capacity:
        confirmed = capacity
        waitlisted = total_registrations - capacity 
        status = "Closed"
    else:
        confirmed = total_registrations
        waitlisted = 0
        status = "Open"
    print(f"Confirmed Registrations: {confirmed}")
    print(f"Waitlisted Users: {waitlisted}")
    print(f"Registration Status: {status}")
manage_registrations(100, 105)