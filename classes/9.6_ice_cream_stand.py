class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cusine: {self.cuisine_type}")
        print(f"costumers served: {self.number_served}")
        
    def open_restaurant(self):
        print(f"{self.name.title()} is open")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, plus_served):
        self.number_served += plus_served
    

class IceCreamStand(Restaurant):
    def __init__ (self, name, cuisine_type="ice cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []
    
    def flavors_availables(self):
        print(f"Flavors availables:")
        for flavor in self.flavors:
            print(f"-{flavor}")


helado = IceCreamStand("The little baby")

helado.flavors = ["strawberry", "vanilla", "chocolate"] 

helado.flavors_availables()
