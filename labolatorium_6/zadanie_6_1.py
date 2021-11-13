import math
zakres = 10**2
P = []
P.append(0)
P.append(0)
P.append(1)
for i in range (3, zakres):
    flag = 1
    for j in range (2, math.floor(i**0.5 +1)):
        if(i%j == 0):
            P.append(0)
            flag = 0
            break
    if (flag == 1): P.append(1)

print(P)