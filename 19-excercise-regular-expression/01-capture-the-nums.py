import re

numbers = []
regex = r"\d+"

while True:
    string = input()
    if string:
        matches = re.findall(regex, string)

        numbers += matches
    else:
        break

print(" ".join(numbers))