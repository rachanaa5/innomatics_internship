class Contact:
    def __init__(self, name, phone):
        self.name=name
        self.phone=phone
    def display_contact(self):
        print("Contact Saved")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
con = Contact("Anita", "9876543210")
con.display_contact()