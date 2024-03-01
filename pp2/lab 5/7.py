import re

def snakeToCamel(text):
    words = text.split('_')
    CamelString= words[0]
    for char in words[1:]:
        CamelString += char.capitalize()
    return CamelString

text = "my_snake_case_string"
print(snakeToCamel(text))


    