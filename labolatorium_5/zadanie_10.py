def nwd (a, b):
    if(a == b): return a
    elif (a>b): return nwd(b, a-b)
    else: return nwd(a, b-a)
a = int(input(""))
b = int(input(""))
c = int(input(""))

print(nwd(nwd(a, b), c))