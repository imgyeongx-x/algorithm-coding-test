from collections import Counter

def solution(want, number, discount):
    answer = 0
    li = []
    for i in range(len(want)):
        for j in range(number[i]):
            li.append(want[i])
            
    cli = Counter(li)
    
    for i in range(0, len(discount) - sum(number)+1):
        cdis = Counter(discount[i:i+sum(number)])
        if len(cli - cdis) == 0:
            answer += 1
    
    return answer