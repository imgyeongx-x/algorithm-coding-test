import sys
input = sys.stdin.readline

worm = 0

def DFS(num):
  global worm
  
  visited[num] = True
  worm += 1

  for i in li[num]:
    if visited[i] == False:
      DFS(i)

N = int(input())
connected = int(input())
li = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(connected):
  a, b = map(int, input().split())
  li[a].append(b)
  li[b].append(a)

DFS(1)

print(worm-1)