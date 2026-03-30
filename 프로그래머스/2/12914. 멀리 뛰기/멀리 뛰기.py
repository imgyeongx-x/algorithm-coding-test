def solution(n):
    answer = 0
    
    li = [0] * (n+1)
    li[1] = 1
    if n >= 2:
        li[2] = 2

    for i in range(3, n+1):
        li[i] = (li[i-1] + li[i-2]) % 1234567

    answer = li[n]
    return answer