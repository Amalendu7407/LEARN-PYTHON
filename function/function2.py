# 3.5 passing parameters

# ****required argument****
# def hello(name , age):
#     print(name  , age)

# hello("ram" , 20)


# ****default argument****
# def hello(name, age=8): 
#     print(name  , age)

# hello("hori",21)

# def inta(principle , time , rate = 12):
#     ans = (principle * time * rate) /100
#     # print(ans)
#     return ans

# si_int = inta(500 ,2)
# print(si_int)



# ****keyword argument****
# def student(name , age):
#     print(f"my name is : {name}\nage is : {age}")

# student(name = "Ram" , age = 20)


# ****multiple argument****
# def student(name , age = 18):
#     print(name , age)

# student("ram")
# student("raja" , 22)
# student("sujay" , 25)


# ****composition****

# def add(a,b):
#     return a+b

# def square(x):
#     return x * x
# ans  = square(add(3,3))
# print(ans)

# scope of variables

# ****local variable****

# def local():
#     x = 5
#     print(x)

# local()

# ****global variable****
# a = 10
# def globalVariable():
#     print(a+10)

# globalVariable()
# print(a*5)

# mutable

# list  , dictionary , set

# listt = [1,2,3,4,5]
# print(listt)
# print("after change")
# listt[0] = 11
# print(listt)

#  dictionary

# d = {
#     "name"  : "ram",
#     "roll" : 102
# }
# print(d)
# print(" after change")
# d["roll"] = 103
# print(d)


# set 

# s = {1,2,3}
# print(s)
# s.add(4)
# print(s)


# immutable

# integer , string , tuple

# tup = (10,20,30,40,50)
# print(tup)
# tup[2] = 3
# print(tup)

# string

# s = "ratan" 
# print(s)
# s[0] = 'R' 
# print(s)

