def check_rainfall(rainfall_data, required_level):
    average = sum(rainfall_data) / len(rainfall_data) 
    status = "Adequate Rainfall" if average >= required_level else "Inadequate Rainfall" 
    print(f"Average Rainfall: {int(average)}")
    print(f"Rainfall Status: {status}")

check_rainfall([80, 70, 65, 73], 70)