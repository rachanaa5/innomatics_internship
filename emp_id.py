class Employee:
    def __init__(self, name, emp_id, dep):
        self.name = name
        self.emp_id = emp_id
        self.dep = dep
    def display_id_card(self):
        print("Employee ID Card")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Department: {self.dep}")