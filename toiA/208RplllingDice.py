a,b = map(int, input().split())

a_min = 1 * a
a_max = 6 * a

if a_min <= b and b <= a_max:
    print('Yes')
else:
    print('No')
