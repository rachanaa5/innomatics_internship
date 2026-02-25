def parking_lot(capacity, logs):
    parked_vehicles=0
    for log in logs:
        if log=="IN":
            parked_vehicles+=1
        elif log=="OUT":
            parked_vehicles-=1
    status="FULL" if parked_vehicles>=capacity else "AVAILABLE"
    print(f"currently parked vehicles: {parked_vehicles}")
    print(f"parking status:{status}")

parking_lot(53,["IN","OUT","OUT","OUT","IN","IN","IN","OUT"])