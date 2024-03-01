import re

def pattern(str):
    p = r'ab*' # для поиска паттерна, "a, ab, abbb ..., " 
    # здесь ab* означает что после 'a' должны быть 0 или больше 'b'
    if re.match(p, str):
        return True
    else:
        return False

str = str(input())
print(pattern(str))