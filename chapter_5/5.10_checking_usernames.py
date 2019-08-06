current_users = ["admin", "Mengeroshi", "gArtox", "Satoshi", "mendax"]
current_users_lower = [user.lower() for user in current_users]#remember that
new_users = ["mengeroshi", "szabo", "finney", "dai","satoshi"]

for new_user  in new_users:
    if new_user  in current_users_lower:
        print(f"{new_user} is already used. Enter another username")
    else:
        print(f"{new_user} available")

