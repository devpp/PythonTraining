def createfile():
    fname = input("Enter the filename :")
    path = input("Enter the path :")  # C:\Users\P.Purushothaman\Desktop\
    content = input("Enter the contents :")

    if fname != "" and path != "" and content != "":
        file = open(path + fname + ".txt", "w")
        file.write(content)
        file.close()
    else:
        print("wrong inputs")


def readfile():
    fname = "task1"
    path = "C:\\Users\\P.Purushothaman\\Desktop\\"
    content = open("C:\\Users\\P.Purushothaman\\Desktop\\" + fname + ".txt" , "r")
    print(content.read())
    content.close()


createfile()
readfile()