num_words = int(input())
synonyms = {}

for n in range(num_words):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for (word, words) in synonyms.items():
    print(f"{word} - {', '.join(words)}")