# n,w = map(int,input().split())
# a = list(map(int,input().split()))
# s = set()

# for i in range(len(a)):
#     if a[i] <= w:
#         s.add(a[i])

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] + a[j] <= w:
#             s.add(a[i] + a[j])

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         for k in range(j+1, len(a)):
#             if a[i] + a[j] + a[k] <= w:
#                 s.add(a[i] + a[j] + a[k])

# print(len(s))

n,w = map(int,input().split())
a = list(map(int,input().split()))
a.extend((0,0))
s = set()

for i in range(len(a)-2):
    for j in range(i+1, len(a)-1):
        for k in range(j+1, len(a)):
            if a[i] + a[j] + a[k] <= w:
                s.add(a[i] + a[j] + a[k])

print(len(s))

