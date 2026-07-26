file = open("school.txt" , "r+")

print(file.read())
new = file.write("\nNew msg")
file.close()