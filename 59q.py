import re

text = input()

print(re.findall(r"\d+", text))

# findall - Find all matches and return them it returns list. /d  - finds the digits