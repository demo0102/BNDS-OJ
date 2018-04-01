k = int(input())
n = int(input())
sum = 0
for i in range(1, n+1):
    for j in range(1,5):
        if i%(10**j)//(10**(j-1)) == k:
            sum += 1
print(sum)
