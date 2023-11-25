path = input().split("\\")
name, extension = path[len(path) - 1].split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")