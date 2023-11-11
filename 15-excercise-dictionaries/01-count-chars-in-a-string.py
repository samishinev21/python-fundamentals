word = input()
stats = {}

for letter in word:
    if letter == " ":
        continue
    
    if letter in stats:
        stats[letter] += 1
    else:
        stats[letter] = 1

for (letter, occurrences) in stats.items():
    print(f"{letter} -> {occurrences}")