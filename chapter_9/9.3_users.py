class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describre_user(self):
        print(f"Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"age: {self.age}")
    
    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()} \n")


mgrsh = User("javier", "saviñon", 21)
mgrsh.describre_user()
mgrsh.greet_user()

mandax = User("julian", "assange", 40)
mandax.describre_user()
mandax.greet_user()