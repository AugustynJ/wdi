import sys
n = int(input(""))

for i in range (0, n):
    spacje = n-i-1
    for j in range (0, spacje):
        sys.stdout.write(str(" "))
    if i == 0:
        sys.stdout.write(str("X"))
    for j in range (spacje, n+i):
        if j == spacje+1 or j == n+i-2:
            sys.stdout.write(str("O"))
        else:
            sys.stdout.write(str("*"))
    print ("")
