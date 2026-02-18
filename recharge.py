def validate_recharge():
    valid_plan=[199,299,399,599]
    while True:
        try:
            plan=int(input("Enter the reacharge plan:"))
            if plan <50:
                print("reacharge plan should be above 50")
                continue
            if plan in valid_plan:
                print(f"Reacharge plan of {plan} is successfully reccharged")
                break            
            else:
                print(f"Invalid recharge plan.")
            except ValueError:
print("please enter a valid numeric amount")
