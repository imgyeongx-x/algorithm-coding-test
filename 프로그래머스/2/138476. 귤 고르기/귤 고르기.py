from collections import Counter

def solution(k, tangerine):
    answer = 0
    total = 0
    
    count = Counter(tangerine)
    count = count.most_common()
    
    for i in count:
        total += i[1]
        answer += 1
        if total >= k:
            break
    
    return answer