import re

regex = r"(^|(?<=\s))([a-z]+[-._]*[a-z]*@[a-z]+[-_]*[a-z]*\.[a-z]+(\.[a-z]+)?)"
txt = input()

matches = re.findall(regex, txt)

for match in matches:
    print(match[1])