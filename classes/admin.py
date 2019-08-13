from user import User

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