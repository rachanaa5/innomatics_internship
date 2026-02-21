def check_exam_eligibility(attendance_list):
    percentage = (attendance_list.count("P") / len(attendance_list)) * 100
    status = "Eligible" if percentage >= 75 else "Not Eligible" 
    print(f"Attendance Percentage: {percentage}")
    print(f"Exam Eligibility: {status}")

check_exam_eligibility(["P", "P", "P", "A", "P"])