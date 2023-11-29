import re
names = input()
regex = "\\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\\b"
matches = re.findall(regex, names)
print(" ".join(matches))