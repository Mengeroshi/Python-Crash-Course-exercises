restaurant_foods = ("spagetti", "meat", "lasagne", "pizza", "salad")
for food in restaurant_foods:
    print(food)
#restaurant_foods[3] = "brocoli"/TypeError: 'tuple' object does not support item assignment
restaurant_foods = ("spagetti", "meat", "lasagne", "ravioli", "fetucini")
print("\nNew Menu:")
for food in restaurant_foods:
    print(food)