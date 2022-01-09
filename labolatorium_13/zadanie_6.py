def printowanie(T, n):
    for i in range(n):
        for j in range(i+1):
            print('{0:3}'.format(T[i][j]), end=" ")
        print("")
    print("...\n")

def pascal (n):
    T = [[0] * (n) for i in range(n)]
    for i in range (n):
        T[i][0] = 1
        T[i][i] = 1
    for i in range (n):
        for j in range(1, i):
            T[i][j] = T[i-1][j] + T[i-1][j-1]
    return T

# n = int(input("Podaj ilość wierszy: "))
n = 5
T = pascal(n)
printowanie(T, n)