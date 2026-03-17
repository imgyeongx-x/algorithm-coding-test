def solution(s):
    answer = [0,0]
    
    while s != "1":
        x = ""

        for i in s:
            if i == "1":
                x += i
            else:
                answer[1] += 1
        s = format(len(x), 'b')
        answer[0] += 1
        
        # s = bin(len(x))
    
    return answer