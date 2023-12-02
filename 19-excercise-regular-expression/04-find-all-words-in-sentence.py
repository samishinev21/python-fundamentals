import re

txt = input()
regex = input()

matches = re.findall(f"\\b{regex}\\b", txt, flags=re.IGNORECASE)

print(len(matches))