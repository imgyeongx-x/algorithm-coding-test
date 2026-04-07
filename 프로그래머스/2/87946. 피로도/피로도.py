def solution(k, dungeons):
    global answer, visited
    answer = 0
    visited = [False] * len(dungeons)
    
    DFS(k, answer, dungeons)
    
    return answer

def DFS(p, a, dungeons):
    global answer
        
    if a > answer:
        answer = a
            
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= p:
            visited[i] = True
            DFS(p-dungeons[i][1], a+1, dungeons)
            visited[i] = False