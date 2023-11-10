list = input()
ascii_dictionary = {}

letters = list.split(", ")

for letter in letters:
    transformed_letter = ord(letter)
    ascii_dictionary[letter] = transformed_letter

print(ascii_dictionary)