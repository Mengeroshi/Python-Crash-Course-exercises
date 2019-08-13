class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cusine: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.name.title()} is open")

my_rest_1 = Restaurant("mc donalds", "fast food")
my_rest_2 = Restaurant("boston", "gourmet")
my_rest_3 = Restaurant("chicago", "american pizza")

my_rest_1.describe_restaurant()
my_rest_1.open_restaurant()

my_rest_2.describe_restaurant()
my_rest_2.open_restaurant()

my_rest_3.describe_restaurant()
my_rest_3.open_restaurant()