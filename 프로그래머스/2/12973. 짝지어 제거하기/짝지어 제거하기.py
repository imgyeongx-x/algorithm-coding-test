from collections import deque

def solution(s):
    answer = 0
    queue = deque()
    for i in range(len(s)):
        if i == 0:
            queue.append(s[i])
        elif len(queue) != 0 and queue[-1] == s[i]:
            queue.pop()
        else:
            queue.append(s[i])
    
    if len(queue) == 0:
        answer = 1
    

    return answer