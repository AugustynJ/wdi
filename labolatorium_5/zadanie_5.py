a = 1
b = 1
print ("T[%d] = 1" %a)
print ("T[%d] = 1" %b)
while (a < 1000000):
    tmp = a
    a += b
    b = tmp
    print ("T[%d] = 1" %(a*b))
