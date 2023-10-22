usernames = input().split(", ")
blacklisted = []
lost = []

while True:
    command = input()
    if command == "Report":
        break
    
    tokens = command.split(" ")

    if tokens[0] == "Blacklist":
        if tokens[1] in usernames:
            blacklisted.append(tokens[1])
            print(f"{tokens[1]} was blacklisted.")
            usernames = list(map(lambda x: x.replace(tokens[1], "Blacklisted"), usernames))
        else:
            print(f"{tokens[1]} was not found.")

    elif tokens[0] == "Error":
        index = int(tokens[1])
        if index >= 0 and index < len(usernames):
            name = usernames[index]
            if name == "Blacklisted"  or name == "Lost":
                continue
            lost.append(name)
            usernames[index] = "Lost"
            print(f"{name} was lost due to an error.")
    
    elif tokens[0] == "Change":
        index = int(tokens[1])
        if index >= 0 and index < len(usernames):
            current_name = usernames[index]
            usernames[index] = tokens[2]

            print(f"{current_name} changed his username to {tokens[2]}.")

print(f"Blacklisted names: {len(blacklisted)}")
print(f"Lost names: {len(lost)}")
print(" ".join(usernames))