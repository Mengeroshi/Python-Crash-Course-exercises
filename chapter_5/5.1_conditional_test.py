car = "LAMBO"
print("is car  == lambo? I think it's true")
print(car.lower()=="lambo")
print("is car == ferrari? I think it's false")
print(car=="ferrari\n")

color = "green"
print("is green  == color? I think it's true")
print(color.upper()=="GREEN")
print("is color == pink? I think it's false")
print(color=="pink\n")

lambo_price = 1_000_000
ferrari_price = 2_000_000
cheyene_price = 500_000
print(ferrari_price>lambo_price)
print(ferrari_price<lambo_price)
print ((ferrari_price>cheyene_price) and (lambo_price<cheyene_price))
print ((ferrari_price>cheyene_price) or (lambo_price<cheyene_price))

print("\nListas")
pizzas = ['mushrooms', 'peperoni', 'hawaian']
print("peperoni" in pizzas)
print("lobster" not in pizzas)