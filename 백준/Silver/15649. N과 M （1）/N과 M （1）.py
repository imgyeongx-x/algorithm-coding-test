N, M = map(int, input().split())

visited = [False] * N
S = [0] * M

def backtrack(length):
  if length == M:
    print(" ".join(str(i+1) for i in S))
    return
  for i in range(0, N):
    if visited[i] == False:
      visited[i] = True
      S[length] = i
      backtrack(length+1)
      visited[i] = False

backtrack(0)