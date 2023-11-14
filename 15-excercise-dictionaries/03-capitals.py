countries = input().split(", ")
cities = input().split(", ")

result = {}

for (country, city) in zip(countries, cities):
    result[country] = city

for (country, city) in result.items():
    print(f"{country} -> {city}")