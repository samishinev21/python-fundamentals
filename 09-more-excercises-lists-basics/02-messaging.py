numbers_str = input()
text = input()
letters = []


numbers = numbers_str.split(" ")

for group_num in numbers:
    sum = 0
    for digit in group_num:
        sum += int(digit)
    if sum > len(text):
        position = sum % len(text)
    else:
        position = sum
    
    letters.append(text[position])
    text = text[:position] + text[position + 1:]

letters = "".join(letters)

print(letters)