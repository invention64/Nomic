print("Handling files and taking names\nVersion 0.2\nTest Server for Python\n\"Can atleast handle files\"")
length=0
def post(a):
    print("posted "+a)
    f = open("data.txt","a+")
    f.write(a+'\n')
    f.close()
def overwrite(a,line):
    print("posted " + a)
    f = open("data.txt","w")
    f.write(a)
    f.close()
def pull():
    print("pulled")
    f = open("data.txt","r+")
    return f.read()
def pullline(line):
    print("pulled line")
    f = open("data.txt","r+")
    for num in range(0,line):
        f.readline()
    return f.readline()

while (True):
    i = input()
    if (i.startswith("post ")):
        i=i.split(None,1)
        post(i[1])
    elif (i==("pull")):
        i=i.split(None,1)
        print(pull())
    elif (i.startswith("overwrite ")):
        i=i.split(None,1)
        overwrite(i[1])
    elif (i.startswith("pullLine ")):
        i=i.split(None,1)
        print(pullline(i[1]))
    elif (i=="?" or i=="help"):
        print("post, pull, overwrite, and pullLine are the current valid commands")
    elif (i=="quit"):
        break
    else:
        print("not a valid command, try help for more options")
    length=0
    while open("data.txt","r+").readline() != ' ':
        length+=1

