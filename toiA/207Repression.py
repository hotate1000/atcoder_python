# A207
list = input().split();
list = [int(i) for i in list];
new_list = sorted(list)
answer   = new_list[-1] + new_list[-2];
print(answer);
