archive = "guest_book.txt"

while True:
    name = input("What's your name, dude? (Insert 'q' to finish): ")
    if name == "q":
        break
    else:
        print(f"Hi {name}!!!!")
        with open(archive, "a") as object_arch:
            object_arch.write(f"{name}\n")

