a,b,k = map(int,input().split())
answer = 0
count = 0

while a < b:
    a = a * k
    count += 1

print(count)
