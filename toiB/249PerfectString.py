s = input()
ss = list(s)
answer_list = {}
answer = 'Yes'

if s.islower() or s.isupper():
    answer = 'No'

for i,x in enumerate(ss):
    if x not in answer_list:
        answer_list[x] = 1
    else:
        # answer_list[x] += 1
        answer = 'No'
        break

print(answer)
