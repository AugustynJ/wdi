s = input("Podaj ciąg znaków: ")
l = 0
p = 0
odp = ""
for i in range(0, len(s)):
    if(s[i] == '('): 
        l += 1
        odp += '('
    elif(s[i] == ')'): 
        p += 1
        odp += ')'
    if(l == p) and l != 0:
        print ("%s," %odp, end =""),
        odp = ""
print("")