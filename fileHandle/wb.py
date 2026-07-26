file = open("binary.bin" , "wb+")

file.write(b"hello hey")
print(file.read())