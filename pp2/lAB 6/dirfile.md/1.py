import os

def list_directories_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    print("\nAll directories and files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

path = '/Users/Renata2004/Desktop/py/pp2/lAB 6/dirfile'
list_directories_files(path)