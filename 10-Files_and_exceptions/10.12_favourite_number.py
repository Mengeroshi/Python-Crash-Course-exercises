import json

favourite_num = input("What's your favourite number?:" )
file_num = "number.json"

with open(file_num, "w") as file:
    json.dump(favourite_num, file)


file_num = "number.json"
with open(file_num) as file:
    fav_num =json.load(file)
    if fav_num == 

print(f"I know your favourite number is {fav_num} ")