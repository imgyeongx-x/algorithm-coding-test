from itertools import combinations

def solution(elements):
    answer = 0
    ele = elements + elements
    li = []
    
    for i in range(1, len(elements)+1):
        for j in range(len(ele)-i):
            s = sum(ele[j:j+i])
            li.append(s)
    li = set(li)
    answer = len(li)
    
    return answer