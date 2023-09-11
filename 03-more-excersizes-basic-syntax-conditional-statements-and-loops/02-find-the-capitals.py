word = input()
result = []

for i, w in enumerate(word):
    if w == w.upper():
        result.append(i)
print(result)