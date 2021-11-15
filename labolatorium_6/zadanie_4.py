zakres = 100
T = [0]*zakres
for i in range (1, 9): T[i*i+i+1] = 1
while True:
    try:
        n = int(input("Prosze podac liczbe naturalna:"))
        if n >= 0:
            break
    except:
        print("To musi byc liczba naturalna!")
flag = 0
for i in range (1, n):
    if(T[i] == 0): continue
    else:
        if(n%i == 0):
            flag = 1
            break
if(flag == 1): print("OK")
else: print("OKn't")