favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ["jen", "oscar", "julia", "edward", "tim"]

for gente in people:
    if gente  in favorite_languages.keys():
        print(f"Thanks for respond {gente.title()}")
    else:
        print(f"{gente.title()}, whats your favourite lenguage?")