import json

favourite_num = input("What's your favourite number?:" )
file_num = "number.json"

with open(file_num, "w") as file:
    json.dump(favourite_num, file)

