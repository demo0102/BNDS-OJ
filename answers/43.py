def primes(n):
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if \
             all( d % od != 0 for od in divisors if od != d ) ]
n = int(input())
for i in primes(n):
    print(i,end=' ')
print('')
