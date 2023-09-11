number = input()
largest = 0
smallest = 0
result = ""

while number != "":
    for n in number:
        n = int(n)
        if n > largest:
            largest = n

    number = number.replace(str(largest), "", 1)
    result += str(largest)
    largest = 0

print(int(result))