import math
zakres = 10**4

#Tablica liczb pierwszych
P = []
P.append(0)
P.append(0)
P.append(1)
for i in range (3, zakres):
    flag = 1
    for j in range (2, math.floor(i**0.5 +1)):
        if(i%j == 0):
            P.append(0)
            flag = 0
            break
    if (flag == 1): P.append(1)


#Tablica wartości z zadania
T = [1]*zakres
T[0] = 0
for i in range (7, zakres):
    if(P[i] == 1):
        T[i] = 0
        continue
    for j in range (6, i):
        #print(j)
        if(P[j] == 0): continue
        if(i%j == 0):
            T[i] = 0
            break

praca = 1
while praca:
    while True:
        try:
            q = int(input("Podaj liczbę: "))
            
            if(type(q) != int): raise ValueError
            else: break
        except ValueError: print("To nie liczba!")
    odp = 0
    for i in range (1, q+1): odp += T[i]
    print("Odpowiedz wynosi: %d" %odp)
    praca = int(input("Czy chcesz podać liczbę ponownie?\n1 - tak\n0 - nie\nWybierz: "))
    