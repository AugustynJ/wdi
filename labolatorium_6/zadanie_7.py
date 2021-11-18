n = int(input(""))
odp = 1
for i in range (1, n+1):
    odp *= i
    while(odp%10 == 0): odp /= 10
    odp %= 10
print(int(odp))
jebac disa chuja zwisa
