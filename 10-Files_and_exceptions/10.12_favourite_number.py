import json
try:
    file_num = "C:\\Users\DopellGanger1\Desktop\Python Crash Course\\10-Files_and_exceptions\\number.json"
    with open(file_num) as file:
        fav_num =json.load(file)

except FileNotFoundError: 
    favourite_num = input("What's your favourite number?:" )
    file_num = "C:\\Users\DopellGanger1\Desktop\Python Crash Course\\10-Files_and_exceptions\\number.json"
    with open(file_num, "w") as file:
        json.dump(favourite_num, file)
    print("I will remember your favourite number")
    
else:
    print(f"I know your favourite number is {fav_num} ")
