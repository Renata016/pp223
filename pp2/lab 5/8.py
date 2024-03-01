import re

text = "MyNameIsRenata"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)