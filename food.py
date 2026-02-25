def estimate_delivery_time(distance, traffic, weather):
    base_time = distance*5
    traffic_delay = 20 if traffic == "High" else 10 if traffic == "Medium" else 0
    weather_delay = 15 if weather == "Rainy" else 0
    tot_time = base_time + traffic_delay + weather_delay
    print(f"Estimated Delivery Time: {tot_time} minutes")
estimate_delivery_time(8, "High", "Rainy")