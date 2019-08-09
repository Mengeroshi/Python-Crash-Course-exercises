

active = True

while active:
    topping = input("Insert the toppings you want for your pizza: ")
    if topping == "quit":
        active = False
    else:
        print(f"You add {topping} to your pizza"