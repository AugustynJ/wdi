import sys
import math
n = int(input(""))

strona = -1
odl = -1
for i in range (0, n):
    spacje = n-i-1
    for j in range (0, spacje):
        sys.stdout.write(str(" "))

    if i == 0:
        sys.stdout.write(str("X"))
        print ("")
        continue

    for j in range (spacje, n+i):
        if j == n+1 - odl*strona:
            sys.stdout.write(str("o"))
        else:
            sys.stdout.write(str("*"))
    
    if i%2 == 1:
         odl = odl + 2
    strona = strona * (-1)
    print("")


for i in range (0, n -1):
    sys.stdout.write(str(" "))
print ("U")
