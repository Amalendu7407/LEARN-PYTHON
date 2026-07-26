file = open("school.txt" , "r")
file.seek(5)

print(file.read())
file.close()