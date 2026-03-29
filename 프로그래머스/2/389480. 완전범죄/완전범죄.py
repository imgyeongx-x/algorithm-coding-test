def solution(info, n, m):
    answer = n
    dp = [[0] * (m) for _ in range(len(info)+1)]
    
    for i in range(1, len(info)+1):
        a = info[i-1][0]
        b = info[i-1][1]
        
        for j in range(m):
            if j < b:
                dp[i][j] = dp[i-1][j] + a
                continue
            dp[i][j] = min(dp[i-1][j-b], dp[i-1][j]+a)
            
    answer = dp[-1][-1] if dp[-1][-1] < n else -1
    
    return answer
