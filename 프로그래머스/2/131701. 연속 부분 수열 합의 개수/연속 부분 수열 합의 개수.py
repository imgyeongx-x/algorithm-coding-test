from itertools import combinations

def solution(elements):
    answer = 0
    ll = len(elements)
    s = set()
    
    for i in range(ll):
        ssum = elements[i]
        s.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j % ll]
            s.add(ssum)
    answer = len(s)
    
    return answer