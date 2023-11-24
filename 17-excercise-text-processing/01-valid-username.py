def only_legal_chars(username):
    for letter in username:
        if letter.isdigit() or letter.isalpha() or letter == "-" or letter == "_":
            continue
        else:
            return False
    return True
    
usernames = input().split(", ")

for username in usernames:
    if len(username) >= 3 and len(username) <= 16 and only_legal_chars(username):
        print(username)