import math
dane = open('/home/kuba/Documents/GitHub/wdi/labolatorium_10/dane.txt', 'r')

a = float("90.87\n")
znaki = ['+', '-', '*', '/', '']
cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
trygo = dane.readlines()
praca = 1
while(praca):
    dz = input("Podaj wyrażenie: ")
    i = 0
    f = ""
    x = ""
    while(i < len(dz)):
        f = f + dz[i]
        i += 1
        if(dz[i] in cyfry): break
    while(i < len(dz)):
        x = x + dz[i]
        i += 1
        if(dz[i] in znaki): break
        if(i == len(dz)-1):
            x += dz[i]
            break
    f += '\n'
    x += '\n'
    j = 0
    while(trygo[j] != f): j += 1
    while(trygo[j] != x): j += 1
    x = trygo[j+1]
    print (x)
        
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if(x == "pi/6"): rad = 1
    # elif(x == "pi/4"): x = 45
    # elif(x == "pi/3"): x = 60
    # elif(x == "pi/2"): x = 90
    # elif(x == "pi"):  x = 180
    # elif(x == "2*pi"): x = 360

    # if(f == "sin"):
    #     if(not rad):
    #         if(x == 0): print("sin 0 = 0", file = zapis)
    #         elif(x == 30): print("sin 30 = 1/2 = 0.5", file = zapis)
    #         elif(x == 45): print("sin 45 = sqrt(2)/2 = 0.707", file = zapis)
    #         elif(x == 60): print("sin 60 = sqrt(3)/2 = 0.866", file = zapis)
    #         elif(x == 90): print("sin 90 = 1", file = zapis)
    #         elif(x == 180): print("sin 180 = 0", file = zapis)
    #         elif(x == 360): print("sin 360 = 0", file = zapis)
    #     else:
    #         if(x == 0): print("sin 0 = 0", file = zapis)
    #         elif(x == 30): print("sin pi/6 = 1/2 = 0.5", file = zapis)
    #         elif(x == 45): print("sin pi/4 = sqrt(2)/2 = 0.707", file = zapis)
    #         elif(x == 60): print("sin pi/3 = sqrt(3)/2 = 0.866", file = zapis)
    #         elif(x == 90): print("sin pi/2 = 1", file = zapis)
    #         elif(x == 180): print("sin pi = 0", file = zapis)
    #         elif(x == 360): print("sin 2*pi = 0", file = zapis)
    # elif(f == "cos"):
    #     if(not rad):
    #         if(x == 0): print("cos 0 = 1", file = zapis)
    #         elif(x == 30): print("cos 30 = sqrt(3)/2 = 0.866", file = zapis)
    #         elif(x == 45): print("cos 45 = sqrt(2)/2 = 0.707", file = zapis)
    #         elif(x == 60): print("cos 60 = 1/2 = 0.5", file = zapis)
    #         elif(x == 90): print("cos 90 = 0", file = zapis)
    #         elif(x == 180): print("cos 180 = -1", file = zapis)
    #         elif(x == 360): print("cos 360 = 1", file = zapis)
    #     else:
    #         if(x == 0): print("cos 0 = 1", file = zapis)
    #         elif(x == 30): print("cos pi/6 = sqrt(3)/2 = 0.866", file = zapis)
    #         elif(x == 45): print("cos pi/4 = sqrt(2)/2 = 0.707", file = zapis)
    #         elif(x == 60): print("cos pi/3 = 1/2 = 0.5", file = zapis)
    #         elif(x == 90): print("cos pi/2 = 0", file = zapis)
    #         elif(x == 180): print("cos pi = -1", file = zapis)
    #         elif(x == 360): print("cos 2*pi = 1", file = zapis)
    # elif(f == "tan"):
    #     if(not rad):
    #         if(x == 0): print("tan 0 = 0", file = zapis)
    #         elif(x == 30): print("tan 30 = sqrt(3)/3 = 0.577", file = zapis)
    #         elif(x == 45): print("tan 45 = 1", file = zapis)
    #         elif(x == 60): print("tan 60 = sqrt(3) = 1.732", file = zapis)
    #         elif(x == 90): print("tan 90 nie istnieje", file = zapis)
    #         elif(x == 180): print("tan 180 = 0", file = zapis)
    #         elif(x == 360): print("tan 360 = 0", file = zapis)
    #     else:
    #         if(x == 0): print("tan 0 = 0", file = zapis)
    #         elif(x == 30): print("tan pi/6 = sqrt(3)/3 = 0.577", file = zapis)
    #         elif(x == 45): print("tan pi/4 = 1", file = zapis)
    #         elif(x == 60): print("tan pi/3 = sqrt(3) = 1.732", file = zapis)
    #         elif(x == 90): print("tan pi/2 nie istnieje", file = zapis)
    #         elif(x == 180): print("tan pi = 0", file = zapis)
    #         elif(x == 360): print("tan 2*pi = 0", file = zapis)
    # elif(f == "ctg"):
    #     if(not rad):
    #         if(x == 0): print("ctg 0 nie istnieje", file = zapis)
    #         elif(x == 30): print("ctg 30 = sqrt(3) = 1.732", file = zapis)
    #         elif(x == 45): print("ctg 45 = 1", file = zapis)
    #         elif(x == 60): print("ctg 60 = sqrt(3)/3 = 0.577", file = zapis)
    #         elif(x == 90): print("ctg 90 = 0", file = zapis)
    #         elif(x == 180): print("ctg 180 nie istnieje", file = zapis)
    #         elif(x == 360): print("ctg 360 nie istnieje", file = zapis)
    #     else:
    #         if(x == 0): print("ctg 0 nie istnieje", file = zapis)
    #         elif(x == 30): print("ctg pi/6 = sqrt(3) = 1.732", file = zapis)
    #         elif(x == 45): print("ctg pi/4 = 1", file = zapis)
    #         elif(x == 60): print("ctg pi/3 = sqrt(3)/3 = 0.577", file = zapis)
    #         elif(x == 90): print("ctg pi/2 = 0", file = zapis)
    #         elif(x == 180): print("ctg pi = 0", file = zapis)
    #         elif(x == 360): print("ctg 2*pi = 0", file = zapis)