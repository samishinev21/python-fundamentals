year = int(input())

while True:
    yearstr = str(year)

    for i, digit in enumerate(yearstr):
        if digit in yearstr[i + 1:]:
            break
    else:
        print(year)
        break
    year += 1