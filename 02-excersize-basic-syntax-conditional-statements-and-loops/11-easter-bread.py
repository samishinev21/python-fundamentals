budget = float(input())
flour_price_per_kg = float(input())
pack_eggs_price = flour_price_per_kg * 75 / 100
milk_price = (flour_price_per_kg + (flour_price_per_kg * 25 / 100)) / 4 

price_bread = flour_price_per_kg + pack_eggs_price + milk_price
count_breads = budget // price_bread
colored_eggs = count_breads * 3
lost_eggs = count_breads - 2
colored_eggs -= lost_eggs
budget_left = budget - price_bread * count_breads

print(f"You made {int(count_breads)} loaves of Easter bread! Now you have {int(colored_eggs)} eggs and {budget_left:.2f}BGN left.")
