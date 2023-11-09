stock = {}
command = input()

while command != "statistics":
    tokens = command.split(": ")
    key = tokens[0]
    value = tokens[1]

    if key in stock:
        stock[key] = stock[key] + int(value)
    else:
        stock[key] = int(value)

    command = input()

print("Products in stock:")

for (product, quantity) in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")