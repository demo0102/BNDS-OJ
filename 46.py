from math import factorial as fact
def ncr(n, r):
    return fact(n)/(fact(r)*fact(n-r))
n = int(input())
r = int(input())
print(int(ncr(n, r)))
