class Delivery:
    def __init__(self, customer_name, address):
        self.customer_name=customer_name
        self.address = address
    def display_delivery_details(self):
        print("Delivery Details")
        print(f"Customer: {self.customer_name}")
        print(f"Address: {self.address}")

deliv = Delivery("Suman", "Hyderabad")
deliv.display_delivery_details()