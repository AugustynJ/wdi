def minor(M, n, k):
    T = [[0]*(n-1) for i in range (n-1)]
    kM = 0
    kT = 0
    while(kT < n-1):
        if(kM == k): kM += 1
        for i in range(n-1):
            T[i][kT] = M[i+1][kM]
        kT += 1
        kM += 1
    return det(T, n-1)


def det(M, n):
    if(n == 2): return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    else:
        s = 0
        for i in range (n):
            if(i%2): s -= M[0][i] * minor(M, n, i)
            else: s += M[0][i] * minor(M, n, i)
    return s


n = int(input("Podaj liczbę niewiadomych: "))
M = [[0] * (n+1) for i in range(n)]
for i in range(n):
    for j in range (n):
        M[i][j] = int(input("Podaj współczynnik stojący przy zmiennej a_%d w %d równaniu: " %(j+1, i+1)))
    M[i][n] = int(input("Podaj wynik równania: "))
# M = [[3, 7, 1, 11], [4, 8, 2, 12], [6, 9, 5, 13], [14, 15, 16, 10]]
W = [[0] * n for i in range(n)]
for i in range (n):
    for j in range (n):
        W[i][j] = M[i][j]

#####################################################################################################################
if(det(W, n) != 0):
    for z in range (n):
        Z = [[0] * n for i in range(n)]
        kM = 0
        kZ = 0
        while(kZ < n):
            if(kM != z): 
                for i in range(n):
                    Z[i][kZ] = M[i][kM]
            else:
                for i in range(n):
                    Z[i][kZ] = M[i][n]
            kM += 1
            kZ += 1

        print("Zmienna a_%d ma wartość: %.2f" %(z+1, det(Z, n)/det(W, n)))
else:
    for z in range (n):
        Z = [[0] * n for i in range(n)]
        kM = 0
        kZ = 0
        while(kZ < n):
            if(kM != z): 
                for i in range(n):
                    Z[i][kZ] = M[i][kM]
            else:
                for i in range(n):
                    Z[i][kZ] = M[i][n]
            kM += 1
            kZ += 1
        if(det(Z, n) != 0):
            print("Brak rozwiązań!")
            exit(0)
    print("Układ jest nieoznaczony - rozwiązań jest nieskonczenie wiele")