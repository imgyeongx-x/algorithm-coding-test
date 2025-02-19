def solution(cipher, code):
    answer = ''
    
    i = code - 1
    while i < len(cipher):
        answer+=(cipher[i])    
        i+=code;
    
    return answer