book_shelf = input().split("&")

while True:
    command = input()
    
    if command == "Done":
        break

    tokens = command.split(" | ")

    if tokens[0] == "Add Book":
        if tokens[1] not in book_shelf:
            book_shelf.insert(0, tokens[1])
    elif tokens[0] == "Take Book":
        if tokens[1] in book_shelf:
            book_shelf.remove(tokens[1])
    elif tokens[0] == "Swap Books":
        if tokens[1] in book_shelf and tokens[2] in book_shelf:
            book_1_index = book_shelf.index(tokens[1])
            book_2_index = book_shelf.index(tokens[2])

            book_shelf[book_1_index], book_shelf[book_2_index] = book_shelf[book_2_index], book_shelf[book_1_index]
    elif tokens[0] == "Insert Book":
        if tokens[1] not in book_shelf:
            book_shelf.append(tokens[1])
    elif tokens[0] == "Check Book":
        index = int(tokens[1])
        if index >= 0 and index < len(book_shelf):
            print(book_shelf[index])

print(", ".join(book_shelf))