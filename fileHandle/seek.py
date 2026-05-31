file = open("school.txt" , "r")
file.seek(7)

print(file.read())
file.close()