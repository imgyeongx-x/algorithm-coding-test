def solution(s):
    answer = ''
    JC = list(s.capitalize())
    
    index = 1
    while index < len(s):
        while JC[index] == ' ':
            index += 1
            if index >= len(s):
                break
            if 'a' <= JC[index] <= 'z':
                JC[index] = JC[index].swapcase()
        index += 1
    
    for i in JC:
        answer += i
            
    
    return answer