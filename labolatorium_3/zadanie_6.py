a=float(input(""))
b=float(input(""))

if a<0 and b<0:
    print("Obydwie liczby mniejsze od zera, koncze program")
elif a<0:
    a = abs(a)
elif b<0:
    b = abs(b)
suma = a+b
print ("Suma wynosi %0.2f" %suma)
roznica = abs(a-b)
print ("Roznica wynosi %0.2f" %roznica)
iloczyn = a*b
print ("Iloczyn wynosi %0.2f" %iloczyn)
if iloczyn == 10:
    print("Yay!")

flag = 1
if a==0 and b==0:
    print("Iloraz nie istnieje")
    flag = 0
elif a==0 or b==0:
    iloraz = 0
else:
    iloraz = a/b
if flag == 1:
    print("Iloraz wynosi %0.2f" %iloraz)

k1 = a ** 2
k2 = b ** 2
print("Kwadraty wynosza odpowiednio %0.2f i %0.2f" %(k1, k2))

p1 = a ** (1/2)
p2 = b ** (1/2)
print("Pierwiastki wynosza odpowiednio %0.2f i %0.2f" %(p1, p2))
