n = int(input())
numbers = []
filtered = []

for _ in range(n):
    integer = int(input())
    numbers.append(integer)

command = input()

for integer in numbers:
    if command == "even":
        if integer % 2 == 0:
            filtered.append(integer)
    elif command == "odd":
        if not integer % 2 == 0:
            filtered.append(integer)
    elif command == "negative":
        if integer < 0:
            filtered.append(integer)
    elif command == "positive":
        if integer >= 0:
            filtered.append(integer)

print(filtered)