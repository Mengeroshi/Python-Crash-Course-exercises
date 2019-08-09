multiple = input("Write a number and the program will tell if it's a multiple of ten: ")
multiple = int(multiple)

if multiple % 10 == 0:
    print(f"{multiple} is multiple of 10")
else:
    print(f"{multiple} it's not a multiple of 10")