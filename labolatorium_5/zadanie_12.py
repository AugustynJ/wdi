a=1
b=1
i=1
while a < 1000000:
    print ("F%d/F%d = %d/%d = %.10f" %(i+1, i, a, b, a/b))
    tmp = a
    a += b
    b = tmp
    #print (a)
    i += 1