result = ""

while True:
    result = ""
    str1 = input()

    if str1 == "end":
        break

    for ch in reversed(str1):
        result += ch

    print(f"{str1} = {result}")