pizzas = ['mushrooms', 'peperoni', 'hawaian']

print("\nI really love the pizza\n")

friend_pizzas = pizzas[:]

pizzas.append("extra_cheese")

friend_pizzas.append("meat")

print(f"My favourite pizzas are:")
for pizza in pizzas:                   
    print(pizza.title())

print(f"\n My friend´s favourite pizzas are:")
for pizza in friend_pizzas:                   
    print(pizza.title())