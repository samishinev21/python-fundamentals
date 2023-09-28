n = int(input())
word = input()
massive = []

for _ in range(n):
    sentence = input()
    massive.append(sentence)

print(massive)

for sentence in massive:
    if not word in sentence:
        massive.remove(sentence)

print(massive)