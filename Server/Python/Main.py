print("Schlonging out Python Python\nVersion 0.1\nTest Server for Python\n\"Does not actually do anything yet!\"")

def post(self):
    print("posted")

def pull(self):
    print("pulled")



while (True):
    i = input()
    if (i=="post"):
        post()
    elif (i=="pull"):
        pull()
    elif (i=="?" or i=="help"):
        print("post and pull are the current valid commands")
    elif (i=="quit"):
        break
    else:
        print("not a valid command, try help for more options")

