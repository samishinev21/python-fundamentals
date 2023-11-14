command = input()
contacts = {}

while not command.isnumeric():
    tokens = command.split("-")

    name = tokens[0]
    phonenumber = tokens[1]

    contacts[name] = phonenumber
    
    command = input()

for _ in range(int(command)):
    name = input()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")