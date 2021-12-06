import math
P = []
P.append(0)
P.append(0)
P.append(1)
for i in range (3, 1000):
    flag = 1
    for j in range (2, math.floor(i**0.5 +1)):
        if(i%j == 0):
            P.append(0)
            flag = 0
            break
    if (flag == 1): P.append(1)

print(P[2])
n = int(input("Podaj rozmiar macierzy: "))
M = [[0]*n for i in range (n)]
for i in range (n):
    for j in range (n):
        M[i][j] = int(input("Podaj T %d, %d: " %(i, j)))

for i in range(n):
    for j in range(n):
        flag = 0
        m = M[i][j]
        for k in range(i, n):
            for l in range (j, n):
                print(m + M[k][l])
                if(P[m + M[k][l]] == 1):
                    flag = 1
                    break
        if(flag == 0): M[i][j] = 0
for i in range(n):
    for j in range (n):
        print (M[i][j], end =' ')
    print("") 
