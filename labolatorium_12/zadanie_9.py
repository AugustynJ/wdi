class pkt:
    def x(self, value):                                  #współrzędna x-owa
        self.data = value
    def y(self, value):                                  #współrzędna y-owa
        self.data = value

def pole(a, b, c):
    return 0.5*abs((b.x-a.x)*(c.y-b.y) - (b.y-a.y)*(c.x-b.x))

def zadanie(dane):
    i = 0
    for A in dane:
        for B in dane:
            for C in dane:
                if(A == B or B == C or C == A): continue #porównujemy tylko różne punkty
                i += 1
                if(A.x == B.x and A.y == C.y):
                    wewn = 0
                    for D in dane:
                        if(D == A or D == B or D == C): continue
                        P = pole(A, B, C)
                        P1 = pole(D, B, C)
                        P2 = pole(A, D, C)
                        P3 = pole(A, B, D)
                        if(P == (P1 + P2 + P3)):
                            wewn = 1
                            break
                    if(not wewn): return True
    print(i)
    return False


dane = []
n = int(input("Podaj ilość punktów: "))
for i in range (n):
    A = pkt()
    A.x = float(input("A_%d.x = " %(i+1)))
    A.y = float(input("A_%d.y = " %(i+1)))
    dane.append(A)

print(zadanie(dane))

