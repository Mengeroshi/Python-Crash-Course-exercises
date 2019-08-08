favourite_places = {
    "glory" : ["home", "school", "church"],
    "xavier" : ["room", "internet", "tenejapan"],
    "satoshi" :["london", "privacy land", "press"],
    }

for name, places  in favourite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        print(place.title())