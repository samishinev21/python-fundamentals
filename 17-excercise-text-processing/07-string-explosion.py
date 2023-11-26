txt = input()
strength = 0
result = ""

for i, sign in enumerate(txt):
    if sign == ">":
        strength += int(txt[i + 1])
        result += sign
    elif strength > 0:
        strength -= 1
        continue
    else:
        result += sign

print(result)