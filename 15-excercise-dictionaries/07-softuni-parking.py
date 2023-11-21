n = int(input())
registered = {}

for i in range(n):
    command = input()
    tokens = command.split(" ")

    action = tokens[0]
    name = tokens[1]

    if action == "register":
        plate_number = tokens[2]
        if name in registered:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            registered[name] = plate_number
            print(f"{name} registered {plate_number} successfully")

    elif action == "unregister":
        if name not in registered:
            print(f"ERROR: user {name} not found")
        else:
            del registered[name]
            print(f"{name} unregistered successfully")

for (name, plate) in registered.items():
    print(f"{name} => {plate}")