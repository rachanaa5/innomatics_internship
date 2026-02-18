def check_eligibility(attendance):
    present_days = 0
    for day in attendance:
        if day == "P":
            present_days += 1
            
    percentage = (present_days / len(attendance)) * 100
    
    if percentage >= 75:
        return f"Attendance: {percentage}% - Eligible"
    else:
        return f"Attendance: {percentage}% - Not Eligible"

log = ["P", "P", "A", "P", "P", "P", "A", "P"]
print(check_eligibility(log))