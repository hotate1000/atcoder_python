n, k = map(int, input().split())
a = list(map(int, input().split()))
m = []
for i in range(k):
    tmp = []
    j = 0
    while j*k < n-i:
        tmp.append(a[i+j*k])
        j += 1
    m.append(tmp)
for i in m:
    i.sort()
res = []
for i in range(n):
    j, kk = i%k, i//k
    res.append(m[j][kk])
    
for i in range(n-1):
    if res[i] > res[i+1]:
        print("No")
        exit()
print("Yes")
