number = int(input())

for number_of_stars in range(1, number + 1):
    for _ in range(number_of_stars):
        print("*", end="")
    print("")

for number_of_stars in range(number -1, 0, -1):
    for _ in range(number_of_stars):
        print("*", end="")
    print("")