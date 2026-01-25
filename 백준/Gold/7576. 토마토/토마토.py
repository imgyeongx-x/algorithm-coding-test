import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
box = [[] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
tomatoes = deque()
day = 0

for i in range(N):
  box[i] = list(map(int, input().split()))

def BFS():
  global box
  global visited
  global day
  
  for i in range(N):
    for j in range(M):
      if box[i][j] == 1:
        tomatoes.append((i, j, 0))
        visited[i][j] = True
      if box[i][j] == -1:
        visited[i][j] = True
  
  while len(tomatoes) != 0:
    info = tomatoes.popleft()
    
    x = info[0]
    y = info[1]
    depth = info[2]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
      if (x + dx[i]) >= 0 and (x + dx[i]) < N and (y + dy[i]) >= 0 and (y + dy[i]) < M:
        if box[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == False:
          tomatoes.append((x+dx[i], y+dy[i], depth+1))
          visited[x+dx[i]][y+dy[i]] = True
          if day < depth+1:
            day = depth+1
  

BFS()

allTomato = True
for i in range(N):
  for j in range(M):
    if visited[i][j] == False:
      allTomato = False

if allTomato == False:
  print(-1)
else:
  print(day)