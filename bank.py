def validate_transaction(amount):
    limit = 50000 
    status = "Approved" if amount <= limit else "Rejected" 
    print(f"Transaction Amount: {amount}")
    print(f"Transaction Status: {status}")

validate_transaction(60000)