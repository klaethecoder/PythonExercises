import os, string, random, time

def encrypt():
    path = os.getcwd()
    files = os.listdir(r"./Love")
    os.chdir(r"./Love")
    for file in files:
        one = random.choice(string.digits)
        two = random.choice(string.digits)
        # print("%s%s%s" % (one, two, file))
        os.rename(file, (one+two+file))
    os.chdir(path)

def decrypt():
    contents = os.listdir(r"./Love")
    path = os.getcwd()
    os.chdir(r"./Love")
    for name in contents:
        os.rename(name, name.strip(string.digits))
    os.chdir(path)

encrypt()
# decrypt()