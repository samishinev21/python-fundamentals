lines = int(input())
loops = 0

for l in range(lines):
    loops += 1
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        break
    elif loops == lines:
        print("All numbers are even!")