import json

file_num = "number.json"
with open(file_num) as file:
    fav_num =json.load(file)

print(f"I know your favourite number is {fav_num} ")