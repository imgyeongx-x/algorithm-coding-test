from collections import deque

N, K = map(int, input().split())

visited = [0] * (100001)

def BFS():
  queue = deque()
  queue.append(N)

  while queue:
    x = queue.popleft()
    if x == K:
      print(visited[x])
      break
    for i in (x-1, x+1, x*2):
      if 0 <= i <=100000 and visited[i] == 0:
        visited[i] = visited[x] + 1
        queue.append(i)

BFS()