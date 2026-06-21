#re stands for Regular Expression a Python module used for: searching text,finding patterns,matching strings. /w used to find word char


import re

email = input()

m = re.match(r"(\w+)@\w+\.com", email)

print(m.group(1))