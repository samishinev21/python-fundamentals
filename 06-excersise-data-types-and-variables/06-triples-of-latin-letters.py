num = int(input())

for n in range(num):
    for m in range(num):
        for v in range(num):
            print(f"{chr(97 + n)}{chr(97 + m)}{chr(97 + v)}")