import math

a,b = map(int,input().split())
c = math.sqrt(a**2+b**2)

ac = a / c
bc = b / c

print('{:.12f}'.format(ac) + ' ' + '{:.12f}'.format(bc))
