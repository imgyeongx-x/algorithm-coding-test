def solution(s):
    answer = ''
    
    index = 0
    minN = float('inf')
    maxN = float('-inf')
    neg = 1
    st = ''
    num = 0
    
    while(index < len(s)):
        if s[index] == '-':
            neg = -1
        elif s[index] != ' ':
            st += s[index]
        else:
            num = int(st) * neg
            if num < minN:
                minN = num
            if num > maxN:
                maxN = num
            num = 0
            st = ''
            neg = 1
        index += 1
        
    num = int(st) * neg
    if num < minN:
        minN = num
    if num > maxN:
        maxN = num
        
    answer = str(minN) + ' ' + str(maxN)
                                     
    return answer