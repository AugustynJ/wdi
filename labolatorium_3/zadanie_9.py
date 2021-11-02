praca = 1
saldo = 1000
PIN = 2137
while (praca > 0) :
    print("Wybierz operacje:")
    print("I - wplata")
    print("O - wyplata")
    print("S - sprawdz saldo")
    print("E - zakoncz")
    op = (input(""))
    if op != "E":
        print("Podaj PIN:")
        pin = int(input(""))
        while(pin != PIN):
            print("PIN nieprawidlowy")
            print("Wprowadz PIN ponownie:")
            pin = int(input(""))
    
    if op == "I":
        print("Podaj kwotę wpłaty")
        kwota = int(input(""))
        saldo += kwota
    elif op == "O":
        print("Podaj kwotę wypłaty")
        kwota = int(input(""))
        saldo -= kwota
    elif op == "S":
        print("Twoje saldo wynosi: %d" %saldo)
    elif op == "E":
        praca = 0
    else: print("Niewalsciwa operacja!\nPowtórz próbę.")
    if op != "E":
        print("Co chcesz zrobic w kolejnym kroku?")

print("Zapraszamy ponownie")
    
