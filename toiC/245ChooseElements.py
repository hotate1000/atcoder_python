n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# [False, False]の配列を5つ作成する
dp = [[False]*2 for i in range(n+1)]

# 一つ目の値をTrueに変換
dp[1][0] = True
dp[1][1] = True

# k差分以内の場合Trueに変換、Trueの時しか確認しない
# aとbの2回確認する
for i in range(1,n):
    if dp[i][0]:
        if abs(a[i-1]-a[i]) <= k:
            dp[i+1][0] = True
        if abs(a[i-1]-b[i]) <= k:
            dp[i+1][1] = True
    if dp[i][1]:
        if abs(b[i-1]-a[i]) <= k:
            dp[i+1][0] = True
        if abs(b[i-1]-b[i]) <= k:
            dp[i+1][1] = True
if dp[n][0] or dp[n][1]:
    print("Yes")
else:
    print("No")
