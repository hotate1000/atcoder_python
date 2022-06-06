n = int(input())
answer_list = '1 1'

for i in range(n):
    if i == 0:
        print('1')
    if i == 1:
        print('1 1')
    if i >= 2:
        c = list(answer_list.split()) 
        answer = '1 '
        for j,k in enumerate(c):
            if j <= (len(c)-2):
                test = int(c[j]) + int(c[j+1])
                answer = answer + str(test) + ' '
        answer = answer + '1'
        answer_list = answer
        print(answer)
