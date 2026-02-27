class SmartLight:
    def __init__(self, name):
        self.name=name
        self.status="OFF"
    def set_status(self, action):
        if action.upper()=="ON":
            self.status="ON"
        else:
            self.status="OFF"
    def display_status(self):
        print(f"{self.name} is {self.status}")
light = SmartLight("Bedroom Light")
light.set_status("ON")
light.display_status()