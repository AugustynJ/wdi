import random
n = int(input("Podaj dlugosc: "))
a = int(input("Podaj dolny zakres: "))
b = int(input("Podaj górny zakres: "))

T = []

# Normalna treść z zadania:
for _ in range (0, n):
    T.append(random.randint(a, b))

# T[i] == i
# for i in range (0, n):
#     T.append(i)

# Tablica ,,na przemian"
# for i in range (0, n):
#     if(i%2): T.append(80)
#     else: T.append(86)

# Tablica stała
# for i in range (0, n):
#     T.append(420)

# Połowa ciąg, połowa stała
# T.append(-420)
# for i in range (1, int(n/2)): 
#     T.append(i)
# for i in range(int(n/2), n):
#     T.append(8086)


for i in range(0, n):
    print(i, T[i]),
print("\n\n")

# Właściwy program
if n == 1: 
    print("Ciąg jest jednoelementowy, nie posiada różnicy a jego suma to %d" %T[0])
    exit()

max_l = 2
max_pos = 0
l = 2
for i in range (2, n):
    if(T[i]-T[i-1] == T[i-1] - T[i-2]):
        l += 1
    else:
        if(l > max_l):
            max_l = l
            max_pos = i - l
        l = 2
    print(T[i], T[i]-T[i-1], T[i-1]-T[i-2], l)
if(l > max_l):
            max_l = l
            max_pos = i - l + 1
print("Najdluzszy podciag ma dlugosc: %d" %max_l)
print("Jego elementy: "),
for i in range (max_pos, max_pos+max_l):
    print("%d " %T[i]),
s = 0
for i in range (max_pos, max_pos+max_l):
    s += T[i]
print("Ich suma wynosi: %d" %s)