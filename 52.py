n = int(input())
for i in range(1, n+1):
    if (i%4 == 0) or (i%6 == 0):
        print(i,end=' ')

