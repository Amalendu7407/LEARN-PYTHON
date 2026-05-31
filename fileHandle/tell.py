file = open("fruit.txt" , "r")

print(file.tell())

file.read(2)
print(file.tell())