import math

def prime(a):
    if (a == 0): return 0
    elif (a == 1): return 0
    elif (a == 2): return 1
    i = 2
    while(i*i <= a):
        if(a%i == 0): return 0
        i += 1
    return 1

praca = 1
while praca:
    while True:
        try:
            q = int(input("Podaj liczbę: "))
            
            if(type(q) != int): raise ValueError
            else: break
        except ValueError: print("To nie liczba!")
    odp = 0
    if(q <= 6): odp = q
    else:
        odp = 6
        for n in range (7, q+1):
            flag = 1
            if(prime(n) == 1): continue
            for i in range(7, n):
                if(prime(i) == 0): continue
                if(n%i == 0):
                    flag = 0
                    break
            if(flag): odp += 1
    print(odp)

    praca = int(input("Czy chcesz podać liczbę ponownie?\n1 - tak\n0 - nie\nWybierz: "))
    