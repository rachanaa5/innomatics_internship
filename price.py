class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def display_price_tag(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}")
prod = Product("Headphones", 2499)
prod.display_price_tag()