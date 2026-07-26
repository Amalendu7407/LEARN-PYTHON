# file = open("school.txt" , "a+")

# file.write("python is a easy language\n")
# file.seek(0)
# print(file.read())
# file.close()

fileobject=open("school.txt","r")
str = fileobject.readline()
while str:
    print(str)
    str=fileobject.readline()
fileobject.close()