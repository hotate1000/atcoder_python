n,y = map(int,input().split())

yen_10000 = -1
yen_5000 = -1
yen_1000 = -1

for i in range(n+1):
    for j in range(n+1-i):
        k = n - i - j
        if i * 10000 + j * 5000 + k * 1000 == y:
            yen_10000 = i
            yen_5000 = j
            yen_1000 = k

print(str(yen_10000) + " " + str(yen_5000) + " " + str(yen_1000))
