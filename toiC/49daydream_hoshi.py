s = input()
answer = "YES"
while len(s) != 0:
    if len(s) < 5:
        answer = "NO"
        break
    if s[-5:] == "dream" or s[-5:] == "erase":
        s = s[:-5]
    elif s[-6:] == "eraser":
        s = s[:-6]
    elif s[-7:] == "dreamer":
        s = s[:-7]
    else:
        answer = "NO"
        break
print(answer)

# t_list = ["dream","dreamer","erase","eraser"]
# count = 0
# s = input()

# while count < len(t_list):
#     if s == '':
#         break
#     for i in t_list:
#         if s[-5:] == i:
#             s = s[:-5]
#             continue
#         if s[-6:] == i:
#             s = s[:-6]
#         if s[-7:] == i:
#             s = s[:-7]
#     count+=1
# if s == '':
#     print('YES')
# else:
#     print('NO')
