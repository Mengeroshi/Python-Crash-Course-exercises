cats_doc = "cats.txt"
dogs_doc = "dogs.txt"

try:
    with open(cats_doc) as cat_arch:
        cats = cat_arch.readlines()
    with open(dogs_doc) as dog_arch:
        dogs = dog_arch.readlines()

except FileNotFoundError:
    print("el archivo no esta en la carpeta")
else:
    for cat in cats:
        print(cat.strip())

    for dog in dogs:
        print(dog.strip())
        