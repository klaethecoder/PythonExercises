import os, string
def renameFiles():
    contents = os.listdir(r"/Users/first/Desktop/prank")
    path = os.getcwd()
    os.chdir(r"/Users/first/Desktop/prank")
    for name in contents:
        os.rename(name, name.strip(string.digits))
    os.chdir(path)
    return contents
print(renameFiles())