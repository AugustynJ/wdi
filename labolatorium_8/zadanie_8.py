def zadanie(s):
    l = 0
    p = 0
    flaga = 0
    odp = ""
    for i in range(0, len(s)):
        if(s[i] == '('): 
            l += 1
            odp += '('
        elif(s[i] == ')'): 
            p += 1
            odp += ')'
        if(l == p) and l != 0:
            if(flaga == 0):
                print ("%s" %odp, end ="")
                flaga = 1
            else: print (", %s" %odp, end ="")
            odp = ""


s = input("Podaj ciąg znaków: ")

zadanie(s)
print("")