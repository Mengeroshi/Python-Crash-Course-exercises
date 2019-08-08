favourite_numbers = {
   "mengeroshi": [7, 8, 9],
   "gloria": [15, 16, 17],
   "mandax": [13, 14, 15],
   "satoshi": [21, 22, 23], 
    }

for name, numbers  in favourite_numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(number)