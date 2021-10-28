import math
p = int(input(""))
k = int(input(""))
##print (p, k)
if abs(p-k)>20:
    sr = math.floor((p+k)/2)
    print(sr-2, sr-1, sr, sr+1, sr+2)
    exit(0)
else:
    ##pętla for
    for i in range(p, k+1):
        print (i)
    ##pętla while
    while p <= k :
        print(p)
        p = p+1
    print ("\n\n")
    

