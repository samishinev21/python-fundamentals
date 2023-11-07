products = input().split(" ")
order = input().split(" ")

stock = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    stock[key] = int(value)

for product in order:
    items_in_stock = stock.get(product)
    
    if items_in_stock:
        print(f"We have {items_in_stock} of cheese left")
    else:
        print(f"Sorry, we don't have {product}")