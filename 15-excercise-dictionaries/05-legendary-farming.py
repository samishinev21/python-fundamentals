materials = {"fragments": 0, "motes": 0, "shards": 0}

while True:
    items = input().split(" ")
    winner_selected = False

    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i + 1].lower()

        if material in materials:
            materials[material] += quantity
        else:
            materials[material] = quantity

        if materials[material] >= 250:
            if material == "shards":
                print("Shadowmoure obtained!")
            elif material == "fragments":
                print("Valanyr obtained!")
            elif material == "motes":
                print("Dragonwrath obtained!")

            materials[material] -= 250
            winner_selected = True
            break

    if winner_selected:
        break
            
print(f"shards: {materials['shards']}")
print(f"fragments: {materials['fragments']}")
print(f"motes: {materials['motes']}")

for (material, quantity) in sorted(materials.items()):
    if material == "shards" or material == "fragments" or material == "motes":
        continue
    else:
        print(f"{material}: {quantity}")