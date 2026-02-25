def analyze_occupancy(total_seats, booked_seats_list):
    booked_count = len(booked_seats_list)
    occupancy_percent = (booked_count / total_seats) * 100 
    if occupancy_percent >= 90:
        status = "Housefull"
    elif occupancy_percent >= 70:
        status = "Almost Full"
    else:
        status = "Seats Available"  
    print(f"Occupancy: {int(occupancy_percent)}%")
    print(f"Show Status: {status}")
analyze_occupancy(200, [1]*150)