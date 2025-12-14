import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = [0] + list(map(int, input().split()))

sumList = [0]*(N+1)
sumNum = 0

for i in range(1, N+1):
  sumList[i] = sumNum + li[i]
  sumNum += li[i]

for i in range(M):
  a, b = map(int, input().split())
  print(sumList[b] - sumList[a-1])