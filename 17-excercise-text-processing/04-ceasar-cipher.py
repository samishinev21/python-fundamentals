txt = input()
result = ""

for letter in txt:
    ascii_position = ord(letter) + 3

    result += chr(ascii_position)

print(result)