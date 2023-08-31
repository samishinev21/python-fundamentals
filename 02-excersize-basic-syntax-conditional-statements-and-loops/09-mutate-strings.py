string_0 = input()
string_1 = input()

for i, letter in enumerate(string_1):
    string_0 = string_0[:i] + letter + string_0[i + 1:]
    print(string_0)