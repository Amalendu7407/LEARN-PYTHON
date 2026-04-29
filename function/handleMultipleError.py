try:
    x = int("xyz")
    l = [1]
    print(l[2])
except ValueError as v:
    print(v)
except IndexError as i:
    print(i)    