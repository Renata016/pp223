import re

text = "Hello My name, is. Renata"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)