from lib2to3.pgen2.token import OP
import random
import os
dane = open('kolokwium\dane.txt', 'r')
class samochod:
    def __init__(self, marka, model, rocznik, silnik, przebieg, ilosc_wypozyczen, kolor):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.silnik = silnik
        self.przebieg = przebieg
        self.ilosc_wypozyczen = ilosc_wypozyczen
        self.kolor = kolor
    
    def wypisz(self):
        print('{:10s}'.format(self.marka), end=" ")
        print('{:10s}'.format(self.model), end=" ")
        print('{:8s}'.format(self.rocznik), end=" ")
        print('{:11s}'.format(self.silnik), end=" ")
        print('{:8s}'.format(self.przebieg), end=" ")
        print('{:16s}'.format(self.ilosc_wypozyczen), end=" ")
        print('{:12s}'.format(self.kolor), end="\n")

class opel(samochod):
    def __init__(self, marka, model, rocznik, silnik, przebieg, ilosc_wypozyczen, kolor):
        super().__init__(marka, model, rocznik, silnik, przebieg, ilosc_wypozyczen, kolor)

    def wypisz(self):
        super().wypisz()
        print("   >>> Uwaga! Opel to szybkie auto ;) <<<")

class uszkodzony(samochod):
    def __init__(self, marka, model, rocznik, silnik, przebieg, ilosc_wypozyczen, kolor):
        super().__init__(marka, model, rocznik, silnik, przebieg, ilosc_wypozyczen, kolor)

    def wypisz(self):
        super().wypisz()
        print("Uwaga! Powyzsze auto jest uszkodzone i nie mozna go wypozyczyc")

class wypozyczony(samochod):
    def __init__(self, marka, model, rocznik, silnik, przebieg, ilosc_wypozyczen, kolor):
        super().__init__(marka, model, rocznik, silnik, przebieg, ilosc_wypozyczen, kolor)

    def wypisz(self):
        super().wypisz()
        print("Uwaga! Powyzsze auto jest wypozyczone. Wybierz inne ;)")

def zamien(wpis, klasa_nowa):
    marka = wpis.marka
    model = wpis.model
    rocznik = wpis.rocznik
    silnik = wpis.silnik
    przebieg = wpis.przebieg
    ilosc = wpis.ilosc_wypozyczen
    kolor = wpis.kolor
    return klasa_nowa(marka, model, rocznik, silnik, przebieg, ilosc, kolor)


Naglowki = samochod("Marka",  "Model", "Rocznik", "Silnik", "Przebieg", "Ilosc_wypozyczen", "Kolor")
Baza = []
Ople = []
Uszkodzone = []
Wypozyczone = []
ilosc = 0
ilosc_opli = 0
ilosc_uszkodzonych = 0
ilosc_wypozyczonych = 0
fotelik_1 = random.randint(1, 10)
fotelik_2 = 0
while(fotelik_2 == fotelik_1): fotelik_2 = random.randint(1, 10)

for linia in dane:     # Zbieranie danych z bliku do Bazy
    ilosc += 1
    marka_s = ""
    i = 0
    while(linia[i] != ";"): 
        marka_s += linia[i]
        i += 1
    i += 1
    model_s = ""
    while(linia[i] != ";"): 
        model_s += linia[i]
        i += 1
    i += 1
    rocznik_s = ""
    while(linia[i] != ";"): 
        rocznik_s += linia[i]
        i += 1
    i += 1
    silnik_s = ""
    while(linia[i] != ";"): 
        silnik_s += linia[i]
        i += 1
    i += 1
    przebieg_s = ""
    while(linia[i] != ";"): 
        przebieg_s += linia[i]
        i += 1
    i += 1
    ilosc_s = ""
    while(linia[i] != ";"): 
        ilosc_s += linia[i]
        i += 1
    i += 1
    kolor_s = ""
    while(linia[i] != ";"): 
        kolor_s += linia[i]
        i += 1
    Baza.append(samochod(marka_s, model_s, rocznik_s, silnik_s, przebieg_s, ilosc_s, kolor_s))

for i in range(ilosc):
    if(Baza[i].marka == "Opel"):
        Ople.append(zamien(Baza[i], opel))
        ilosc_opli += 1

dzialanie = 1
print("WITAJ W NASZEJ WYPOZYCZALNI SAMOCHODOW!")
while(dzialanie):
    #os.system("cls")
    print("Co chcesz wykonac?")
    print("1 - Przeglad dostepnych samochodow")
    print("2 - Wypozycz auto")
    print("3 - Zwroc wypozyczony samochod")
    print("4 - Zglos uszkodzenie")
    print("5 - Pokaż tylko ople (bo to najlepsze auta)")
    print("6 - Auta tylko z fotelikami dla dzieci")
    print("0 - Zakoncz dzialanie")
    try: 
        operacja = int(input())
        if(operacja > 6): raise ValueError
    except:
        os.system("cls")
        print("Podana operacja nie jest poprawna!! ")
    
    if(operacja == 0):
        print("Dziekujemy za skorzystanie z naszych uslug!")
        exit(0)
    elif(operacja == 1):
        os.system("cls")
        print("Nr ", end="")
        Naglowki.wypisz()
        for i in range (ilosc):
            j = 0
            print('{:2d}'.format(i+1), end=" ")
            if(Baza[i].marka == "Opel" and (Baza[i] not in Uszkodzone) and (Baza[i] not in Wypozyczone)):
                Ople[j].wypisz()
                j += 1
            elif(Baza[i] in Wypozyczone): print("Samochod obecnie wypozyczony")
            elif(Baza[i] in Uszkodzone): print("Smochod obecnie uszkodzony")
            else: Baza[i].wypisz()
        print("\n")
        print("Nacinij ENTER aby powrocic do menu")
        ret = input("...")
        os.system("cls")
    elif(operacja == 2):
        os.system("cls")
        print("Nr ", end="")
        Naglowki.wypisz()
        for i in range(ilosc):
            print('{:2d}'.format(i+1), end=" ")
            Baza[i].wypisz()
        print("\n")
        print("wybierz numer wypozyzanego samochodu")
        nr_wypozyczonego = int(input("... "))
        Wypozyczone.append(Baza[nr_wypozyczonego-1])
        ilosc_wypozyczonych += 1
        os.system("cls")
    elif(operacja == 3):
        os.system("cls")
        
        if(ilosc_wypozyczonych == 0): 
            print("Nie ma zadnego wypozyczonego samochodu!")
            print("\n")
            print("Nacinij ENTER aby powrocic do menu")
            ret = input("...")
            os.system("cls")
        else:
            print("Nr ", end="")
            Naglowki.wypisz()
            for i in range(ilosc_wypozyczonych):
                print('{:2d}'.format(i+1), end=" ")
                Wypozyczone[i].wypisz()
            print("\n")
            print("wybierz numer zwracanego samochodu")
            nr_zwracanego = int(input("... "))
            del Wypozyczone[i-1]
            ilosc_wypozyczonych -= 1
            os.system("cls")
    elif(operacja == 4):
        os.system("cls")
        print("Nr ", end="")
        Naglowki.wypisz()
        for i in range(ilosc):
            print('{:2d}'.format(i+1), end=" ")
            Baza[i].wypisz()
        print("\n")
        print("Ktory samochod jest uszkodzony?")
        nr_uszkodzonego = int(input("... "))
        Uszkodzone.append(Baza[nr_uszkodzonego-1])
        ilosc_uszkodzonych += 1
        os.system("cls")
    elif(operacja == 5):
        os.system("cls")
        print("Nr ", end="")
        Naglowki.wypisz()
        j = 0
        for i in range (ilosc):
            if(Baza[i].marka == "Opel"):
                print('{:2d}'.format(j+1), end=" ")
                j += 1
                Baza[i].wypisz()

        print("\n")
        print("Nacinij ENTER aby powrocic do menu")
        ret = input("...")
        os.system("cls")
    elif(operacja == 6):
        os.system("cls")
        print("Nr ", end="")
        Naglowki.wypisz()
        print("1  ", end=" ")
        if(Baza[fotelik_1] in Wypozyczone): print("Samochod obecnie wypozyczony")
        elif(Baza[fotelik_1] in Uszkodzone): print("Smochod obecnie uszkodzony")
        else: Baza[fotelik_1].wypisz()
        print("2  ", end=" ")
        if(Baza[fotelik_2] in Wypozyczone): print("Samochod obecnie wypozyczony")
        elif(Baza[fotelik_2] in Uszkodzone): print("Smochod obecnie uszkodzony")
        else: Baza[fotelik_2].wypisz()
        print("\n")
        print("Nacinij ENTER aby powrocic do menu")
        ret = input("...")
        os.system("cls")