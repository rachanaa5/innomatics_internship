def check_password_strength(password):
    has_digit = False
    has_special = False
    special_chars = "@#$"
    if len(password) < 8:
        return "Weak: Minimum 8 characters required."
    for char in password:
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True        
    if has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak: Must contain a digit and a special character (@, #, or $)."

print(check_password_strength("PassCode123#"))