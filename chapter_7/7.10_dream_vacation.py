dream_v = {}

active = True

while active:
    name = input("What's your name?: ") 
    vacation = input("Where are your dream vacation?: ")

    dream_v[name] = vacation
    
    response = input("There are other person who wants to response the poll? (yes/no): ")
    if response == "no":
        active = False

for name, vacation in dream_v.items():
    print(f"{name.title()}'s dream vacation are on {vacation}")