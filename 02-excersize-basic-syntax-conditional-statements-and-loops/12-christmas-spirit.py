quantity = int(input())
days = int(input())
budget = 0
points = 0

ornaments_price = 2
ornaments_poits = 5

skirt_price = 5
skirt_points = 3

garlands_price = 3
garlands_points = 10

lights_price = 15
lights_points = 17

for day in range(1, days + 1):
    if day % 2 == 0:
        budget += ornaments_price
        points += ornaments_poits
    if day % 3 == 0:
        budget += skirt_price + garlands_price
        points += skirt_points + garlands_points
    if day % 5 == 0:
        budget += lights_price
        points += lights_points