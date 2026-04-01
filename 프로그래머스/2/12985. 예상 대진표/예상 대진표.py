def solution(n,a,b):
    answer = 0

    ma = a
    mb = b
    while True:
        if ma == mb:
            break
        ma = (ma+1)//2
        mb = (mb+1)//2
        answer += 1

    return answer