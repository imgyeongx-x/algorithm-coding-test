import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(now):
  visited[now] = True
  for i in arr[now]:
    if visited[i] != True:
      DFS(i)

for i in range(M):
  u, v = map(int, input().split())
  arr[u].append(v)
  arr[v].append(u)

cnt = 0

for i in range(1, N+1):
  if not visited[i]:
    cnt += 1
    DFS(i)

print(cnt)