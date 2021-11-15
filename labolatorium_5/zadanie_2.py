zakres = 100
T = [0]*zakres
T[1] = 1
T[2] = 1
for i in range (3, zakres): T[i] = T[i-1] + T[i-2]
F = [0]*zakres
for i in range (1, zakres): F[i] = F[i-1] + T[i]
for i in range (0, zakres): print(i, F[i]) 
n = int(input("Podaj liczbe: "))
i = 0
flag = 0
while(F[i] < n): i += 1
while(i < zakres and flag == 0):
    for j in range (0, i):
        if(F[i] - F[j] == n):
            print ("Spełnia warunki zadania")
            flag = 1
            break
    i += 1
if(flag == 0): print("Nie spełnia warunków zadania")
