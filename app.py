def check_appointment_eligibility(age):
    status = "Eligible" if age >= 18 else "Not Eligible" 
    print(f"Patient Age: {age}")
    print(f"Eligibility Status: {status}")

check_appointment_eligibility(21)