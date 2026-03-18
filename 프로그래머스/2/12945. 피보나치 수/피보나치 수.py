def solution(n):
    answer = 0
    
    F = [0] * (n+1)
    F[0] = 0
    F[1] = 1
    
    i = 2
    while i <= n:
        F[i] = (F[i-1] + F[i-2]) % 1234567
        i+=1
        
    answer = (F[n]) % 1234567
    
    return answer