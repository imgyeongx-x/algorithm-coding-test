def solution(n):
    answer = n
    
    while True:
        answer = answer + 1
        
        n_bin = str(format(n, 'b'))
        a_bin = str(format(answer, 'b'))
        
        n_cnt = 0
        a_cnt = 0
        
        for i in n_bin:
            if i == "1":
                n_cnt += 1
                
        for i in a_bin:
            if i == "1":
                a_cnt += 1
                
        if n_cnt == a_cnt:
            break
            
    print(answer)
    return answer