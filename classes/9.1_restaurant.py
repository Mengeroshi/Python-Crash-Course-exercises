class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cusine: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.name.title()} is open")


my_rest = Restaurant("gusteaus", "french")

my_rest.describe_restaurant()
my_rest.open_restaurant()