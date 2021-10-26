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
roznica = a-b
print ("Roznica wynosi %0.2f", %roznica)
