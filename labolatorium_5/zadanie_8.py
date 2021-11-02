import math
for n in range (2, 1000000):
    suma = 0
    p = math.floor(math.sqrt(n)+1)
    for i in range (1, p):
        if n%i == 0:
            suma += i
            suma += n/i
    if(suma == 2*n): print(n)
print("done")
