def sandwich_items(*ingredients):
    print("Ingredients in sandwich: \n")
    
    for ingredient in ingredients:
        print(f"-addind {ingredient}")

sandwich_items("cheese", "meat", "garlic")
sandwich_items("garlic", "spam", "eggs")
sandwich_items("jam", "beans", "ketchup")