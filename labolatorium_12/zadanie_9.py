import random
class pkt:
    def x(self, value):                                  #współrzędna x-owa
        self.data = value
    def y(self, value):                                  #współrzędna y-owa
        self.data = value

def pole(a, b, c):
    return 0.5*abs((b.x-a.x)*(c.y-b.y) - (b.y-a.y)*(c.x-b.x))

def zadanie(dane):
    for A in dane:
        for B in dane:
            for C in dane:
                if(A == B or B == C or C == A): continue #porównujemy tylko różne punkty
                if(A.x == B.x and A.y == C.y):
                    wewn = 0
                    for D in dane:
                        if(D == A or D == B or D == C): continue
                        P = pole(A, B, C)
                        P1 = pole(D, B, C)
                        P2 = pole(A, D, C)
                        P3 = pole(A, B, D)
                        if((P == (P1 + P2 + P3)) or min(P1, P2, P3) == 0):
                            wewn = 1
                            break
                    if(not wewn): return True
    return False


dane = []
# n = int(input("Podaj ilość punktów: "))
# for i in range (n):
#     A = pkt()
#     A.x = float(input("A_%d.x = " %(i+1)))
#     A.y = float(input("A_%d.y = " %(i+1)))
#     dane.append(A)

#Przykład 1
A = pkt()
A.x = 1
A.y = 10
dane.append(A)
B = pkt()
B.x = 2
B.y = 1
dane.append(B)
C = pkt()
C.x = 3
C.y = 9
dane.append(C)
D = pkt()
D.x = 4
D.y = 2
dane.append(D)
E = pkt()
E.x = 5
E.y = 8
dane.append(E)
F = pkt()
F.x = 6
F.y = 3
dane.append(F)
G = pkt()
G.x = 7
G.y = 7
dane.append(G)
H = pkt()
H.x = 8
H.y = 4
dane.append(H)
I = pkt()
I.x = 9
I.y = 6
dane.append(I)
J = pkt()
J.x = 10
J.y = 5
dane.append(J)
K = pkt()
K.x = 4
K.y = 6
dane.append(K)

#Przykład 2
# A = pkt()
# A.x = 0
# A.y = 0
# dane.append(A)
# B = pkt()
# B.x = 0
# B.y = 3
# dane.append(B)
# C = pkt()
# C.x = 3
# C.y = 0
# dane.append(C)
# D = pkt()
# D.x = 1
# D.y = 1
# dane.append(D)

for i in dane: print(i.x, i.y)
print(zadanie(dane))

#Wyjście przykładu 1:
# Spostrzeżenie: punkty (poza K) są ułożone na dwóch nierównoległych prostych
# Bez punktu K -> False
#        ponieważ każdy punkt ma różną współrzędną x-ową jak i y-ową
# Z punktem K -> To zależy...
#        (8, 2), (9, 2) -> False
#        (3, 3), (4, 6) -> True