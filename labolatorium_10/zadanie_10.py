dane = open('/home/kuba/Documents/GitHub/wdi/labolatorium_10/dane.txt', 'r')
zapis = open('/home/kuba/Documents/GitHub/wdi/labolatorium_10/wyniki.txt', 'w')

for _ in range(0, 5):
    a = dane.readline()
    f = ""
    i = 0
    while(a[i] != " "): 
        f += a[i]
        i += 1

    x = ""
    rad = 0
    i += 1
    while(i < len(a)-1):
        x += a[i]
        i += 1
    
    print(x)
    if(x == "pi/6"): 
        x = 30
        rad = 1
    elif(x == "pi/4"): 
        rad = 1
        x = 45
    elif(x == "pi/3"): 
        rad = 1
        x = 60
    elif(x == "pi/2"): 
        rad = 1
        x = 90
    elif(x == "pi"): 
        rad = 1
        x = 180
    elif(x == "2*pi"): 
        rad = 1
        x = 360
    x = int(x)
    if(f == "sin"):
        if(not rad):
            if(x == 0): print("sin 0 = 0", file = zapis)
            elif(x == 30): print("sin 30 = 1/2 = 0.5", file = zapis)
            elif(x == 45): print("sin 45 = sqrt(2)/2 = 0.707", file = zapis)
            elif(x == 60): print("sin 60 = sqrt(3)/2 = 0.866", file = zapis)
            elif(x == 90): print("sin 90 = 1", file = zapis)
            elif(x == 180): print("sin 180 = 2", file = zapis)
            elif(x == 360): print("sin 360 = 0", file = zapis)
        else:
            if(x == 0): print("sin 0 = 0", file = zapis)
            elif(x == 30): print("sin pi/6 = 1/2 = 0.5", file = zapis)
            elif(x == 45): print("sin pi/4 = sqrt(2)/2 = 0.707", file = zapis)
            elif(x == 60): print("sin pi/3 = sqrt(3)/2 = 0.866", file = zapis)
            elif(x == 90): print("sin pi/2 = 1", file = zapis)
            elif(x == 180): print("sin pi = 2", file = zapis)
            elif(x == 360): print("sin 2*pi = 0", file = zapis)
    elif(f == "cos"):
        if(not rad):
            if(x == 0): print("cos 0 = 1", file = zapis)
            elif(x == 30): print("cos 30 = sqrt(3)/2 = 0.866", file = zapis)
            elif(x == 45): print("cos 45 = sqrt(2)/2 = 0.707", file = zapis)
            elif(x == 60): print("cos 60 = 1/2 = 0.5", file = zapis)
            elif(x == 90): print("cos 90 = 0", file = zapis)
            elif(x == 180): print("cos 180 = -1", file = zapis)
            elif(x == 360): print("cos 360 = 1", file = zapis)
        else:
            if(x == 0): print("cos 0 = 1", file = zapis)
            elif(x == 30): print("cos pi/6 = sqrt(3)/2 = 0.866", file = zapis)
            elif(x == 45): print("cos pi/4 = sqrt(2)/2 = 0.707", file = zapis)
            elif(x == 60): print("cos pi/3 = 1/2 = 0.5", file = zapis)
            elif(x == 90): print("cos pi/2 = 0", file = zapis)
            elif(x == 180): print("cos pi = -1", file = zapis)
            elif(x == 360): print("cos 2*pi = 1", file = zapis)

    