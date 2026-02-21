def detect_duplicates(usernames):
    has_duplicates = "Yes" if len(usernames) != len(set(usernames)) else "No" 
    print(f"Duplicate Accounts Found: {has_duplicates}")

detect_duplicates(["user1", "user2", "user1"])