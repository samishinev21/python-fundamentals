numbers = input()
list = numbers.split(" ")

for i, n in enumerate(list):
    list[i] = int(n) * -1
print(list)