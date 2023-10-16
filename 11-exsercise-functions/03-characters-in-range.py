start_chr = input()
end_chr = input()

def ascii_range(a, b):
    a_ascii = ord(a)
    b_ascii = ord(b)
    list = []

    for num in range(a_ascii + 1, b_ascii):
        list.append(chr(num))

    return " ".join(list)

print(ascii_range(start_chr, end_chr))