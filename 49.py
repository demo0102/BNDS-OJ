from fractions import gcd
n = int(input())
commonDivision = 0
for i in range(n):
    i = int(input())
    if commonDivision == 0:
        commonDivision = i
    else:
        commonDivision = gcd(i,commonDivision)
print(commonDivision)
