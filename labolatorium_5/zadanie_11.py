def nwd (a, b):
    if(a == b): return a
    elif (a>b): return nwd(b, a-b)
    else: return nwd(a, b-a)

def nww (a, b):
    n = nwd(a, b)
    odp = a*b/n
    return odp

a = int(input(""))
b = int(input(""))
c = int(input(""))

print(nww(nww(a, b), c))