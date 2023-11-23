replace_str = input()
word = input()

while replace_str in word:
    word = word.replace(replace_str, "")

print(word)