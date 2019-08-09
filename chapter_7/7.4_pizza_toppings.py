topping = ""
while topping != "quit":
    topping = input("Insert the toppings you want for your pizza: ")
    if topping != "quit":
        print(f"You add {topping} to your pizza")