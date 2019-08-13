class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loggin_attempts = 0
    
    def describre_user(self):
        print(f"Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"age: {self.age}")
        print(f"Loggin attempts: {self.loggin_attempts}\n")
    
    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()} \n")
    
    def increment_loggin_attempts(self):
        self.loggin_attempts += 1
    
    def reset_loggin_attempts(self):
        self.loggin_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.priv = Privilege()

class  Privilege:
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        if self.privileges:
            print("Admin privileges:")
            for privilege in self.privileges:
                print(f"-{privilege}")


sudo = Admin("Xavier", "saviñon", 21)
sudo.priv.privileges = ["can add post", "can delete post", "can ban user"]

sudo.priv.show_privileges()