while True:
    name  = input()
    count = len(name)

    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif count < 5:
        print(f"{name} goes to Gryffindor.")
    elif count == 5:
        print(f"{name} goes to Slytherin.")
    elif count == 6:
        print(f"{name} goes to Ravenclaw.")
    elif count > 6:
        print(f"{name} goes to Hufflepuff.")