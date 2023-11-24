txt = input()

digits = ""
letters = ""
others = ""

for sign in txt:
    if sign.isdigit():
        digits += sign
    elif sign.isalpha():
        letters += sign
    else:
        others += sign

print(digits)
print(letters)
print(others)