n = int(input("Enter a number : "))
a = 0 
b = 1 
for i in range(n):
    print(a , end = " ")
    c = a + b
    a = b
    b = c
#  this is a line