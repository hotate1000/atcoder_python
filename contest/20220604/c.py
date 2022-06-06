n,k = map(int,input().split())
a = list(map(int,list(input().split())))

sort_by = sorted(a)
kai = 'Yes'

def kai_test():
    global kai
    for i in a:
        if a[i] != sort_by[i]:
            kai = 'No'
            break
    return

for i,j in enumerate(a):
    if i <= (len(a)-3):
        if i == len(a) -3:
            kai_test()
            break
        if a[i] > a[i+k]:
            a[i],a[i+k] = a[i+k],a[i]
print(kai)
