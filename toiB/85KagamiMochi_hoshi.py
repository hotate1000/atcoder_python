n = int(input())
d = []

for i in range(n):
    dd = int(input())
    d.append(dd)
d = (sorted(set(d)))
print(len(d))
