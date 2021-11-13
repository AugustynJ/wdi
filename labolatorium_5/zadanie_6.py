def isprime(n):
    if(n==0 or n==1): return 0
    i = 2
    flag = 0
    while(i*i <= n):
        if(n%i == 0):
            flag = 1
            return 0
        i += 1
    if(flag == 0): return 1


n = int(input(""))
if(isprime(n)==1): print("TAK")
else: print("NIE")
