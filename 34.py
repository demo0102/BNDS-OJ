# 这题可以使用辗转相除法，但是那样就有点小题大做了，我这里采用暴力
a = int(input())
b = int(input())
c = int(input())
found = False
for i in range(7, 101):
    if (i%3 == a) and (i%5 == b) and (i%7 == c):
        print(i)
        found = True
if found == False:
    print('none')
