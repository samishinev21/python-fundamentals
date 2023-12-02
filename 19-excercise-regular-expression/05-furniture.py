import re

sum = 0
purchase = {}

regex = r">>(\w+)<<(\d+(\.\d+)?)!(\d+)"

command = ""

while True:
    command = input()

    if command == "Purchase":
        break

    matches = re.findall(regex, command)

    for match in matches:
        purchase[match[0]] = float(match[1]) * float(match[3])

print("Bought furniture:")

for (item, price) in purchase.items():
    print(item)
    sum += price

print(f"Total money spend: {sum:.2f}")