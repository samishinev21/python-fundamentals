txt = input()
result = ""
last_letter = ""

for letter in txt:
    if last_letter != letter:
        result += letter
    
    last_letter = letter

print(result)