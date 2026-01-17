import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

from collections import deque


def DFS(num): # 재귀
  global li
  global visited

  if visited[num] == True:
    return
  print(num, end=" ")
  visited[num] = True

  for i in li[num]:
    if visited[i] == False:
      DFS(i)


def BFS(num): # 큐
  global li
  global visited
  
  queue = deque()

  visited[num] = True
  print(num, end=" ")
  queue.append(num)
  
  while queue:
    v = queue.popleft()
    for w in li[v]:
      if visited[w] == False:
        visited[w] = True
        print(w, end=" ")
        queue.append(w)

N, M, V = map(int, input().split())

li = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
  a, b = map(int, input().split())
  li[a].append(b)
  li[b].append(a)

for i in li:
  i.sort()

DFS(V)

print()
visited = [False] * (N+1)

BFS(V)