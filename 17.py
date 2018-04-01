from math import log10
a = int(input())
if a == 0:
    print(1)
else:
    print(int(log10(a) // 1 + 1))
