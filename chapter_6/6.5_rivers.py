rivers = {
    "nile" : "egypt", 
    "amazonia" : "brazil", 
    "yangtse": "china"
    }
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value}")

print("\nRivers")
for keys in rivers.keys():
    print(keys.title())

print("\nCountries")
for value in rivers.values():
    print(value.title())
