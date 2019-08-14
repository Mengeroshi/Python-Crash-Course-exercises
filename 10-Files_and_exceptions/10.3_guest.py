name = input("What's your name, dude?: ")

archive = "guest.txt"

with open(archive, "w") as object_arch:
    object_arch.write(name)
