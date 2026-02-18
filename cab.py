def calculate_fare(km, is_peak):
    base_fare = 50
    rate_per_km = 12
    fare = base_fare + (km * rate_per_km)
    
    if is_peak:
        fare *= 1.25 
        
    return fare

def fare_app():
    while True:
        try:
            distance = float(input("Enter distance in km: "))
            peak = input("Is it peak hour? (yes/no): ").lower() == 'yes'
            
            total = calculate_fare(distance, peak)
            print(f"Estimated Fare: ₹{total:.2f}")
            
            retry = input("Calculate another fare? (yes/no): ").lower()
            if retry != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter numbers for distance.")

