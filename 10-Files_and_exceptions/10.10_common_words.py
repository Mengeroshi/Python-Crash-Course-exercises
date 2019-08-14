moby = "moby_dick.txt"

with open(moby, "r") as book:
    words = book.readlines()

#words = contents.split()
for line in words:

    lol += words.count("ahab")
    lol_2 += words.lower().count("ahab")

print(lol)