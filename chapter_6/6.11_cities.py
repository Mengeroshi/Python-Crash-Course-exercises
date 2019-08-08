cities = {
    "berlin":{
        "country" : "germany",
        "population" : 3_500_000,
        "fact" : "there are good beer",
        },
    "london":{
        "country" : "england",
        "population" : 8_100_000 ,
        "fact" : "best fish and chips ever",
        },
    "cdmx":{
        "country" : "mexico",
        "population" : 8_800_000,
        "fact" : "best tacos ever",
        },
    }

for city, city_info in cities.items():
    print(city)
    city_country = city_info["country"]
    population_country = city_info["population"]
    fact_country = city_info["fact"]
    
    print(f"Country: {city_country.title()}")
    print(f"Population: {population_country}")
    print(f"Fact: {fact_country}")