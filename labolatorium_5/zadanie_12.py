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


    '''
    X -> szukana wartosc
    A_{n+1} = A_{n} + A_{n-1}    | : A_{n}
    X = 1 + 1/X                  | *X      (X>0)
    X^2 - X - 1 = 0
    D = 1 + 4 = 5
    X = (1+sqrt(5))/2
    
    
    '''