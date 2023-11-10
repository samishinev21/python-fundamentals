list = input()
words = list.split(" ")
result = {}
printing_result = []

for word in words:
    word = word.lower()

    if word in result:
        result[word] += 1
    else:
        result[word] = 1


for (word, times) in result.items():
    if times % 2 != 0:
        printing_result.append(word)

print(" ".join(printing_result))