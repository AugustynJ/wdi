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


# n = int(input("Podaj liczbę niewiadomych: "))
# M = [[0] * (n+1) for i in range(n)]
# for i in range(n):
#     for j in range (n):
#         M[i][j] = int(input("Podaj współczynnik stojący przy zmiennej a_%d w %d równaniu: " %(j+1, i+1)))
#     M[i][n] = int(input("Podaj wynik równania: "))

# Przyklad 1 dla (a_1, a_2, a_3, a_4, a_5, a_6) = (1, 2, 3, 4, 5, 6) 
# n = 6
# M = [[1, 1, 1, 1, 1, 1, 21], [2, 1, 3, 7, 6, 9, 125], [-2, -1, -1, -1, -1, -10, -76], [8, 0, 8, 6, 1, 1, 67], [6, 5, 4, 3, 2, 1, 56], [-1, 1, -1, 1, -1, 1, 3]] 

# Przyklad 2 dla (a_1, a_2, a_3) = (1, 1, 1)
n = 3
M = [[1, 2, 3, 6], [4, -5, 1, 0], [2, 1, 3, 6]] 

# Przykład 3 dla (a_1, a_2) = (1/6, -3/7)
# n = 2
# M = [[6, 7, -2], [3, 0, 0.5]]

# Przyklad 4 układ sprzeczny
# n = 2
# M = [[3, 4, 5], [3, 4, 9]]

# Przykład 5 układ nieoznaczony
# n = 2
# M = [[1, 2, 7], [2, 4, 14]]


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
        #print(Z)

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

##################################################################################
# Wyjście 1:
# Zmienna a_1 ma wartość: 1.00
# Zmienna a_2 ma wartość: 2.00
# Zmienna a_3 ma wartość: 3.00
#
# Wyjscie 2:
# Zmienna a_1 ma wartość: 1.00
# Zmienna a_2 ma wartość: 2.00
# Zmienna a_3 ma wartość: 3.00
# Zmienna a_4 ma wartość: 4.00
# Zmienna a_5 ma wartość: 5.00
# Zmienna a_6 ma wartość: 6.00
#
# Wyjście 3:
# Zmienna a_1 ma wartość: 0.17 
# Zmienna a_2 ma wartość: -0.43
#
# Wyjście 4:
# Brak rozwiązań!
#
# Wyjście 5:
# Układ jest nieoznaczony - rozwiązań jest nieskonczenie wiele