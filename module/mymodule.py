# my own module
def add(a , b):
    return a + b

def subs(a , b):
    return a - b

def mul(a , b):
    return a * b 

def printEven(n):
    evenAns = []
    for i in range(1 , n+1):
        if i % 2 == 0:
            evenAns.append(i)
    return evenAns 

def printOdd(x):
    ans = []
    for i in range(1 , x+1):
        if i % 2 != 0:
            ans.append(i)
    return ans        



