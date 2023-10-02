factor = int(input())
count = int(input())
list = []

for n in range(1, count + 1):
    n = n * factor
    list.append(n)
print(list)