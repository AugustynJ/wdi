def koniec(s, n):
    l = 0
    p = 0
    odp = ""
    for i in range(n, len(s)):
        if(s[i] == '('):
            l += 1
            odp += '('
        elif(s[i] == ')'):
            p += 1
            odp += ')'
        if(l == p) and (l != 0):
            return i+1
    return -1
    
    

#########################################
# wej = input("Podaj ciąg znaków: ")
def zadanie(wej):
    s = ""
    odp = ""
    for i in range(0, len(wej)):
        if(wej[i] == '(' or wej[i] == ')'):
            s += wej[i]
    i=0
    while(i < len(s)):
        if(s[i] != '('):
            i += 1
            continue
        ind = koniec(s, i)
        if(ind != -1):
            # print("\"", end="")
            for j in range(i, ind):
                odp += (s[j])
            # print("\", ", end="")
            odp += " "
            i = ind
        else: i += 1
    if(odp == ""): return None
    return odp

# print("")

