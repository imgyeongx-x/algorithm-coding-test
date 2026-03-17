def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        sum = 0
        a = i
        while a < n+1 and sum < n:
            sum += a
            a += 1
            if sum == n:
                answer+=1
    
    
    return answer