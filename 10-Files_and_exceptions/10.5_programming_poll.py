responses = "responses.txt"

while True:
    reasons_p = input("Why do you like programming? (Insert 'q' to finish): ")
    if reasons_p == "q":
        break
    else:
        with open(responses, "a") as archive_obj:
            archive_obj.write(f"{reasons_p}\n")