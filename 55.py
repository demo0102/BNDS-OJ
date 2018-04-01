n = int(input())
def factorize(n):
    divisor = []
    for i in range(1, int(n/2)+1):
        if not bool(n%i):
            divisor.append(i)
    return divisor
for i in factorize(n):
    print(i,end=' ')
print(n)
