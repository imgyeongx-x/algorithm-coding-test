def solution(brown, yellow):
    answer = []
    n = 3
    m = 3
    total = brown + yellow
    
    for n in range(3, total):
        if total % n == 0:
            m = total // n
            if n * m == total and n >= m and (n + m) == (brown + 4) / 2:
                break
        
    answer.append(n)
    answer.append(m)
    
    return answer