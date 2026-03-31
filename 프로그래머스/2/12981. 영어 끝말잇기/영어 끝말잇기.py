def solution(n, words):
    answer = []
    li = dict()
    i = 0
    for i in range(0, len(words), n):
        for j in range(0, n):
            s = i+j
            if s >= len(words):
                break
            if words[s] in li:
                answer = [j+1, (s//n)+1]
                return answer
            
            elif s != 0 and words[s-1][-1] != words[s][0]:
                answer = [j+1, (s//n)+1]
                return answer
            
            else:
                li[words[s]] = 1
    answer = [0, 0]
            
    return answer