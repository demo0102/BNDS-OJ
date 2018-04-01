k = int(input())
n = int(input())
sum = 0
for i in range(1, n+1):
    for j in str(i):
        if int(j) == k:
            sum += 1
print(sum)
