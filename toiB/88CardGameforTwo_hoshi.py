n = int(input())
a = list(map(int,input().split()))
alice = 0
bob = 0


a_sort = sorted(a, reverse=True)

for i,aa in enumerate(a_sort):
    if (i+1) % 2 == 1:
        alice += aa
    else:
        bob += aa

answer = alice - bob
print(answer)
