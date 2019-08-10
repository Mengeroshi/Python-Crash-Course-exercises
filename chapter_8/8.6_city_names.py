def city_country(city, country):
    city_des = f"{city.title()}, {country.title()}"
    return city_des

city = city_country("monterrey", "mexico")
print(city)

city_2 = city_country("shenzen", "china")
print(city_2)

city_3 = city_country("berilin", "germany")
print(city_3)