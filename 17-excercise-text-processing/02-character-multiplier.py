txt = input().split(" ")
str1 = txt[0]
str2 = txt[1]
index = 0
total_sum = 0

for (letter_str1, letter_str2) in zip(str1, str2):
    index += 1

    total_sum += ord(letter_str1) * ord(letter_str2)

remaining_word = ""

if len(str1) == len(str2):
    pass
elif len(str1) > len(str2):
    remaining_word = str1[index:]
else:
    remaining_word = str2[index:]

for letter in remaining_word:
    total_sum += ord(letter)

print(total_sum)