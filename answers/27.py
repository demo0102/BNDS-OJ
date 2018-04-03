n = float(input())
p = float(input())
from math import log
rate = 1 + 5/1000
print(int(log(p/n, rate)//1 + 1))
