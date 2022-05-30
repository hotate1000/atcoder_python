n,k = map(int,input().split())
c = list(map(int,list(input().split())))

candy_list = {}

# 最大数の取得
for i in range(k):
    candy = c[i]
    if candy not in candy_list:
        candy_list[candy] = 1
    else:
        candy_list[candy] += 1
answer = len(candy_list)

# 最大数になるように削除と追加
for i in range(k,n):
    # 追加
    add_candy = c[i]
    if add_candy not in candy_list:
        candy_list[add_candy] = 1
    else:
        candy_list[add_candy] += 1
    # 削除
    delete_candy = c[i-k]
    if candy_list[delete_candy] == 1:
        del candy_list[delete_candy]
    else:
        candy_list[delete_candy] -= 1

    answer = max(answer, len(candy_list))

print(answer)
