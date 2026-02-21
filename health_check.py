def check_app_health(error_count):
    if error_count == 0:
        status = "Healthy" 
    elif error_count <= 5:
        status = "Minor Issues" 
    else:
        status = "Critical Issues" 
    print(f"Error Count: {error_count}")
    print(f"System Status: {status}")

check_app_health(7)