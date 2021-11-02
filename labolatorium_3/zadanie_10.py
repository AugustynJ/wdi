import random
praca = 1
while(praca > 0):
    print("Podaj liczbe:")
    a = int(input(""))
    print("Podaj liczbe:")
    b = int(input(""))
    print("Jaką operację chcesz wykonać:")
    print("+ dodawanie")
    print("- odejmowanie")
    print("* mnożenie")
    print("/ dzielenie")
    print("** potęgowanie")
    print("^ pierwiastkowanie")
    print("x losowanie liczby z zakresu")
    op = input("")

    if(op == "+"): print (a+b)
    elif(op == "-"): print (a-b)
    elif(op == "*"): print (a*b)
    elif(op == "/"): print (a/b)
    elif(op == "**"): print (a**b)
    elif(op == "^"): print (a**(1/b))
    elif(op == "x"): print (random.randint(a, b))
    else: print("Niewłaściwa operacja!")

    print("Czy chcesz wprowadzić nowe dane?\nT/N")
    czy = input("")
    if(czy == "N"):
        print ("Zapraszamy ponownie!")
        praca = 0
    
