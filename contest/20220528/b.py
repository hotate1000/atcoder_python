h,w = map(int,input().split())
check_w1 = 0
check_h1 = 0
check_1_ok = 'False'
check_w2 = 0
check_h2 = 0

marubatu_list = []
for idh in range(h):
    marubatu = list(input())
    for idw,iw in enumerate(marubatu):
        if iw == 'o' and check_1_ok == 'False':
            check_w1 = idw
            check_h1 = idh
            check_1_ok = 'True'
        elif iw == 'o' and check_1_ok == 'True':
            check_w2 = idw
            check_h2 = idh
    marubatu_list.append(marubatu)

answer = abs(check_w2 - check_w1) + abs(check_h2 - check_h1)
print(answer)
