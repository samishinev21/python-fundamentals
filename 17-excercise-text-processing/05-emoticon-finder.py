txt = input()

for i, sign in enumerate(txt):
    if sign == ":":
        print(":" + txt[i + 1])