import math
zakres = 10**3

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
#for i in range (0, zakres): print(i, T[i])


praca = 1
while(praca > 0):
    q = int(input("Podaj liczbe:"))
    if(not(type(q) == int) or q<0):
        print("Coś popsułeś!")
        break
    a = 0
    for i in range (1, q+1): a += T[i]
    print("Odpowiedź to %d" %a)
    inp = ""
    while(inp != "Y" and inp != "N"):
        inp = input("Czy chcesz dalej kontynuować zapytania? [Y/N]")
        if(inp == "N"):
            praca = 0
            print("OK to do zobaczenia!")
            exit()
        elif(inp == "Y"): praca = 1
        else: print("Wprowadzono nieprawidłową wartość. Podaj ponownie: [Y/N]")
        #print(inp)