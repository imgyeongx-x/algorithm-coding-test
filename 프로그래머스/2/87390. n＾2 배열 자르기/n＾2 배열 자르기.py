def solution(n, left, right):
    answer = []
    
    li = []
    for i in range(left, right+1):
        a = (i//n)+1
        b = (i%n)+1
        answer.append(max(a, b))
    
    
    return answer