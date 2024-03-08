import os

path = r'/Users/Renata2004/Desktop/py/pp2/lAB 6/dirfile'
p = os.listdir(path)
for item in p:
    full_path = os.path.join(path, item)
    print('Exists:', os.access(full_path, os.F_OK))
    print('Readable:', os.access(full_path, os.R_OK))
    print('Writable:', os.access(full_path, os.W_OK))
    print('Executable:', os.access(full_path, os.X_OK))
    print()