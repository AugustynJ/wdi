import math
dane = open('D:\Git\Git\mingw64\wdi\labolatorium_10\dane.txt', 'r')

znaki = ['+', '-', '*', '/', '']
cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
trygo = dane.readlines()
wynik = 0
while(True):
    wyr = input("Podaj wyrażenie: ")
    i = 0
    f = ""
    x = ""
    while(i < len(wyr)):
        f = f + wyr[i]
        i += 1
        if(wyr[i] in cyfry): break
    while(i < len(wyr)):
        x = x + wyr[i]
        i += 1
        if(i == len(wyr)-1):
            x += wyr[i]
            break
    f += '\n'
    x += '\n'
    j = 0
    while(trygo[j] != f): j += 1
    while(trygo[j] != x): j += 1
    x = trygo[j+1]
    x = float(x)
    print(x)
    