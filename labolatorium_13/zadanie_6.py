import time
def print_prostok(T, n):
    for i in range(n):
        for j in range(i+1):
            print('{0:4}'.format(T[i][j]), end=" ")
            time.sleep(0.1)
        print("")
    print("\n\n")
    return None

def nowy_lepszy_print(T, n):
    for i in range(n):
        for j in range (i, n): print("      ", end="")
        for j in range(i+1):
            time.sleep(0.1)
            print('{0:4}'.format(T[i][j]), end=" ")
        print("")
    print("\n\n")
    return None

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
n = 15
T = pascal(n)
print_prostok(T, n)
nowy_lepszy_print(T, n)