quantities = {}
prices = {}

while True:
    command = input()
    if command == "buy":
        break
    
    tokens = command.split(" ")

    name = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])

    if name in quantities:
        quantities[name] += quantity
    else:
        quantities[name] = quantity

    prices[name] = price

for name in quantities.keys():
    total_price = prices[name] * quantities[name]
    print(f"{name} -> {total_price:.2f}")