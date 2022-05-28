n,a,b = map(int,input().split())
answer = 0

for i in range(n):
    c = i+1
    x = [int(j) for j in str(c)]
    y = sum(x)
    if a <= y and y <= b:
        answer += c
print(answer)
