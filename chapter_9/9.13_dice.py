from random  import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        return(randint(1, self.sides))

dado6 = Dice()
lista_r = []

for roll  in range(10):
    
    result = dado6.roll_dice()
    
    lista_r.append(result)


print("10 rolls of 6 sided dice:")
print(lista_r)

#10 sided dice:
dado10 = Dice(sides=10)
lista_r = []

for roll  in range(10):
    
    result = dado10.roll_dice()
    
    lista_r.append(result)

print("10 rolls of 6 sided dice:")
print(lista_r)


#20 sided dice:
dado20 = Dice(sides=20)
lista_r = []

for roll  in range(10):
    
    result = dado20.roll_dice()
    
    lista_r.append(result)

print("10 rolls of 20 sided dice:")
print(lista_r)
