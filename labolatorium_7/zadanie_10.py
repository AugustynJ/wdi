import random
n = int(input("Podaj dlugosc: "))
a = int(input("Podaj dolny zakres: "))
b = int(input("Podaj górny zakres: "))

T = []

# Normalna treść z zadania:
# for _ in range (0, n):
#     T.append(random.randint(a, b))






# Połowa jest ciągiem, połowa jest stała
T.append(-420)
for i in range (1, int(n/2)): 
    T.append(i)
for i in range(int(n/2), n):
    T.append(8086)

for i in range(0, n):
    print(T[i]),
print("\n\n\n")
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
    print(T[i]-T[i-1], T[i-1]-T[i-2], l)
if(l > max_l):
            max_l = l
            max_pos = i - l
print("Najdluzszy podciag ma dlugosc: %d" %max_l)
print("Jego elementy: "),
for i in range (max_pos, max_pos+max_l):
    print("%d " %T[i]),
s = 0
for i in range (max_pos, max_pos+max_l):
    s += T[i]
print("Ich suma wynosi: %d" %s)