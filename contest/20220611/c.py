# import math

# x,a,d,n = map(int,input().split())

# list = []
# answer = -1
# for i in range(n):
#     list.append(a + d * i)

# if x >= 0:
#     for i in list:
#         if x >= math.fabs(i)-math.fabs(d)/2 and x <= math.fabs(i)+math.fabs(d)/2:
#             answer = math.fabs(x)-i
#             break
#     if answer == -1:
#         x1 = x - max(list)
#         x2 = x - min(list)
#         x_list = [math.fabs(x1),math.fabs(x2)]
#         answer = min(x_list)
# if x < 0:
#     for i in list:
#         if x >= math.fabs(i)-math.fabs(d)/2 and x <= math.fabs(i)+math.fabs(d)/2:
#             print(math.fabs(x)-i)
#             break
#     if answer == -1:
#         x3 = x - max(list)
#         x4 = x - min(list)
#         x_list = [math.fabs(x3),math.fabs(x4)]
#         answer = (min(x_list))
# print(int(answer))

x,a,d,n = map(int, input().split())

i = 0
if x != a:
    if d == 0:
        if x >= a:
            i = abs(x - a)
        else:
            i = abs(a - x)
    
    elif d > 0:
        if x < a:
            i = abs(a - x)
        elif x > (a+d*(n-1)):
            i = abs(x - (a+d*(n-1)))
        else:
            i = min(abs((x-a)%d),abs((a+d-x)%d))
            
    elif d < 0:
        if x > a:
            i = abs(x - a)
        elif x < (a+d*(n-1)):
            i = abs((a+d*(n-1)) - x)
        else:
            i = min(abs((a-x)%d),abs((x-a+d)%d))
print(i)
