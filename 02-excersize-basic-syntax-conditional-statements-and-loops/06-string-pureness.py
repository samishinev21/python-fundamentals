number_of_strings = int(input())

for _ in range(number_of_strings):
    string = input()
    for letter in string:
        if letter == "," or letter == "_" or letter == ".":
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
