import re

string = input()
regex = r"\b_([A-Za-z]+)\b"

matches = re.findall(regex, string)

print(",".join(matches))