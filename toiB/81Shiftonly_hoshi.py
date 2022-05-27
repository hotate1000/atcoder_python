n = int(input())
a = list(map(int, input().split()))
count = 0
process = 'True'

while True:
    for i in range(n):
        if a[i] % 2 != 0 :
            process = 'False'
            break
        a[i] = a[i] / 2
    if process == 'False':
        break
    count += 1

print(count)
