number_of_chars = int(input())
sum = 0

for _ in range(number_of_chars):
    char = input()
    sum += ord(char)
print(f"The sum equals: {sum}")