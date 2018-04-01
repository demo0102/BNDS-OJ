n = int(input())
sum = 0
for i in range(0, 201):
    for j in range(0, 41):
        for k in range(0, 21):
            if (i + 5*j + 10*k) == n:
                sum += 1
print(sum)
