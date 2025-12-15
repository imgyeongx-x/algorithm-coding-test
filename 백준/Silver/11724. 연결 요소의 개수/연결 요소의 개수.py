import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
visited = [False] * (N+1)

def DFS(v):
  visited[v] = True
  for i in A[v]:
    if visited[i] == False:
      DFS(i)


for i in range(M):
  u, v = map(int, input().split())
  A[u].append(v)
  A[v].append(u)

cnt = 0

for i in range(1, N+1):
  if visited[i] == False:
    DFS(i)
    cnt+=1


print(cnt)