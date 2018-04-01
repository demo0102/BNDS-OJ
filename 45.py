n = int(input())
sum = 0
for i in range(0, 21):
    for j in range(0, 34):
        for k in range(0, 101):
            if (5*i + 3*j + k) == n:
                sum += 1
print(sum)
