import math
def f(x):
    return float(x**2 - 2)

e = 0.00001
p = float(0.0)
k = float(2.0)
while(abs(p-k) > e):
    x = float((p+k)/2)
    if(f(x) == 0):
        break
    else:
        if(f(p)*f(x) < 0): k = x
        else: p = x
    print("%.10f" %x)
print("\n\n\n")


e = 0.00001
p = float(0.0)
k = float(-2.0)
while(abs(p-k) > e):
    x = float((p+k)/2)
    if(f(x) == 0):
        break
    else:
        if(f(p)*f(x) < 0): k = x
        else: p = x
    print("%.10f" %x)