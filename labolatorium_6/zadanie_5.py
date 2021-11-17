import math
def int_to_bin(n):
    odp = ""
    while(n > 0):
        odp = str(int(n%2)) + odp
        n /= 2
        n = math.floor(n)
    return odp

print(int_to_bin(21))
n = int(input("Podaj liczbe: "))
n_str = str(n)
rev = n_str[::-1]
pal = n_str == rev
b = str(format(n, 'b'))
brev = b[::-1]
pal_bin = b == brev


print(n, n_str, rev, pal)
print(b, brev, pal_bin)