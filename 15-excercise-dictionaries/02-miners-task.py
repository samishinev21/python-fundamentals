command = ""
resources = {}

while True:
    command = input()

    if command == "stop":
        break

    quantity = int(input())

    if command in resources:
        resources[command] += quantity
    else:
        resources[command] = quantity

for (resource, quantity) in resources.items():
    print(f"{resource} -> {quantity}")