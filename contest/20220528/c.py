q = int(input())
s = []

for i in range(q):
    value_a = list(map(int,input().split()))
    
    if value_a[0] == 1:
        s.append(value_a[1])
    elif value_a[0] == 2:
        for j in range(value_a[2]):
            if value_a[1] in s:
                s.remove(value_a[1])
    elif value_a[0] == 3 and len(s) != 0:
        max_value = max(s)
        min_value = min(s)
        print(max_value - min_value)
