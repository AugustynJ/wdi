import time
def print_prostok(T, n):
    for i in range(n):
        for j in range(i+1):
            print('{0:4}'.format(T[i][j]), end=" ")

        print("")
    print("\n\n")
    return None

def nowy_lepszy_print(T, n):
    for i in range(n):
        for j in range (i, n): print("   ", end="")
        for j in range(i+1):
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


def pascal_test (n):
    if(n <= 0): return None
    T = pascal(n)
    odp = []
    for i in range(n): odp.append(T[n-1][i])
    return odp

# n = int(input("Podaj ilość wierszy: "))
# n = 15
# T = pascal(n)
# print_prostok(T, n)
# nowy_lepszy_print(T, n)

# n = 15
# print(pascal_test(15), len(pascal_test(15)))
# n = int(input("Podaj ilość wierszy: "))
n = 15
T = pascal(n)
print_prostok(T, n)
nowy_lepszy_print(T, n)

