import os

f = open(r"/Users/Renata2004/Desktop/py/pp2/lAB 6\dirfile.md/4.txt")
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")