a,b,c = map(int,input().split())

if c <= b and b <= a:
    print('Yes')
elif a <= b and b <= c:
    print('Yes')
else:
    print('No')
