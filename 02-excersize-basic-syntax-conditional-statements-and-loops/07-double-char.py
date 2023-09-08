while True:
    word = input()
    if word == "End":
        break
    if word == "SoftUni":
        continue
    for letter in word:
        print(f"{letter}{letter}", end = "")
    print("")
