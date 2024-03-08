import os
p=(r"/Users/Renata2004/Desktop/py/pp2/lAB 6/dirfile/delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")