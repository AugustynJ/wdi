def alfabetyczne(s1, s2):
    odp = 1
    flag = 1
    for i in range (0, min(len(s1), len(s2))):
        i1 = 0
        i2 = 0
        j = 0
        while(A[j] != s1[i]):
            i1 += 1
            j += 1
        j = 0
        while(A[j] != s2[i]): 
            i2 += 1
            j += 1
        if(i1 > i2): 
            odp = 0
            flag = 0
            break
        elif(i1 < i2):
            flag = 0
            break
    if(len(s2) < len(s1) and flag): 
        odp = 0
    return odp   

T = ["abba", "banicja", "ban", "menel"]
a = "abcdefghijklmnopqrstuvwxyz"
A = list(a)
for i in range (1, len(T)):
    if(alfabetyczne(T[i-1], T[i]) == 0):
        print (False)
        exit(0)
print(True)
