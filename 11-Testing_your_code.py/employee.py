class Employee:
    def __init__(self, first, last, anual_salary):
        self.first = first
        self.last = last
        self.anual_salary = anual_salary
    
    def give_rise (self, rise=5000):
        self.anual_salary += rise