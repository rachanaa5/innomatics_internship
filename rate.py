class Movie:
    def __init__(self, name, rating):
        self.name=name
        self.rating=rating
    def display_details(self):
        print(f"Movie: {self.name}")
        print(f"Rating: {self.rating}/5")
mov = Movie("Inception", 4.8)
mov.display_details()