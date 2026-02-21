def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = (100 * 3) + ((units - 100) * 5)
    else:
        bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)
    
    if bill < 500:
        usage = "Low Usage"
    elif 500 <= bill <= 1500:
        usage = "Moderate Usage"
    else:
        usage = "High Usage"
        
    return bill, usage 

bill_amt, status = calculate_electricity_bill(250)
print(f"Total Bill: ₹{bill_amt}, Usage Level: {status}")