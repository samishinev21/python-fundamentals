list = ["G", 5, "hjdjf", 86]

result = []
    
for thing in list:
    if thing.isalpha():
        result.append(thing)

print(result)