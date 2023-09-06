budget = float(input())
flour_price_per_kg = float(input())
pack_eggs_price = flour_price_per_kg * 75 / 100
milk_price = (flour_price_per_kg + (flour_price_per_kg * 25 / 100)) / 4 

price_bread = flour_price_per_kg + pack_eggs_price + milk_price
count_breads = budget // price_bread
colored_eggs = count_breads * 3
print(count_breads)
print(colored_eggs)
