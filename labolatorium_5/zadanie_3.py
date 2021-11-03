import math
n = int(input(""))
epsilon = 0.000001
a = n
b = 1
while(abs(a-b) > epsilon):
    a = (a+b)/2
    b = n/a
print(a)