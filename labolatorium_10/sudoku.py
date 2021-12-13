import math

def printuj(T):
    for i in range(9):
        for j in range(9):
            print(T[i][j], end = ' ')
        print("")
    return None

def spr (w, k, T, P):
    for i in range(9):
        if(P[w][i] != 0):
            T[w][k][P[w][i]-1] = 0
    for i in range(9):
        if(P[w][i] != 0):
            T[w][k][P[i][k]-1] = 0
    w3 = math.floor(w/3)
    k3 = math.floor(k/3)
    for i in range(9):
        for j in range(9):
            if(math.floor(i/3) == w3) and (math.floor(j/3) == k3): 
                #if(w==6 and k==3): print(i, j, P[i][j])
                if(P[i][j] != 0):
                    T[w][k][P[i][j]-1] = 0
    return None



T = [[[1 for k in range(9)] for j in range(9)] for i in range(9)]

P = [
    [0, 0, 0, 0, 9, 0, 4, 0, 0],
    [0, 0, 0, 0, 4, 1, 7, 0, 2],
    [8, 0, 0, 6, 7, 0, 0, 3, 0],
    [0, 5, 0, 0, 0, 0, 9, 0, 0],
    [3, 1, 9, 0, 0, 0, 2, 7, 8],
    [0, 0, 2, 9, 0, 0, 0, 4, 0],
    [0, 7, 0, 0, 6, 9, 0, 0, 0],
    [5, 0, 4, 2, 8, 0, 0, 0, 0],
    [0, 0, 6, 0, 1, 0, 8, 0, 0],
]
zera = 0
for i in range(9):
    for j in range(9):
        if(P[i][j] == 0): zera += 1

while(zera > 0):
    for i in range(9):
        for j in range(9):
            if(P[i][j] == 0):
                spr(i, j, T, P)
    # print(zera)
    for i in range(9):
        for j in range(9):
            if(P[i][j] != 0): continue
            s = 0
            for k in range(9): s += T[i][j][k]
            if(s == 1):
                for k in range(9):
                    if(T[i][j][k] == 1):
                        #print("JD")
                        P[i][j] = k+1
                        zera -= 1
                        break
    #for i in range(9): print(T[6][3][i], end = ' ')
    if(zera == 44): 
        printuj(P)
        exit(0)