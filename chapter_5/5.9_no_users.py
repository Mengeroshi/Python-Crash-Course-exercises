usernames = ["admin", "mengeroshi", "gartox", "satoshi", "mendax"]

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, great to see you again")
else:
    print("There's no users")